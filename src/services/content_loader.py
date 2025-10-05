"""
Content loading services for different types of URLs.
"""
from typing import List, Any, Optional
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from config.settings import Config
from src.utils.url_utils import is_youtube_url


class ContentLoaderError(Exception):
    """Custom exception for content loading errors."""
    pass


class ContentLoader:
    """Service class for loading content from various sources."""
    
    def __init__(self):
        self.config = Config()
    
    def load_youtube_content(self, url: str) -> List[Any]:
        """
        Load content from YouTube URL.
        
        Args:
            url (str): YouTube URL to load content from
            
        Returns:
            List[Any]: List of loaded documents
            
        Raises:
            ContentLoaderError: If content loading fails
        """
        try:
            # Try loading with video info first
            loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
            docs = loader.load()
            return docs
        except Exception:
            try:
                # Fallback to loading without video info
                loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
                docs = loader.load()
                return docs
            except Exception as e:
                raise ContentLoaderError(f"Failed to load YouTube content: {str(e)}")
    
    def load_website_content(self, url: str) -> List[Any]:
        """
        Load content from website URL.
        
        Args:
            url (str): Website URL to load content from
            
        Returns:
            List[Any]: List of loaded documents
            
        Raises:
            ContentLoaderError: If content loading fails
        """
        try:
            loader = UnstructuredURLLoader(
                urls=[url],
                ssl_verify=False,
                headers=self.config.DEFAULT_HEADERS
            )
            docs = loader.load()
            return docs
        except Exception as e:
            raise ContentLoaderError(f"Failed to load website content: {str(e)}")
    
    def load_content(self, url: str) -> List[Any]:
        """
        Load content from URL (auto-detects type).
        
        Args:
            url (str): URL to load content from
            
        Returns:
            List[Any]: List of loaded documents
            
        Raises:
            ContentLoaderError: If content loading fails
        """
        if is_youtube_url(url):
            return self.load_youtube_content(url)
        else:
            return self.load_website_content(url)
    
    def validate_documents(self, docs: List[Any]) -> bool:
        """
        Validate that documents contain content.
        
        Args:
            docs (List[Any]): List of documents to validate
            
        Returns:
            bool: True if documents are valid and contain content
        """
        if not docs or len(docs) == 0:
            return False
        
        # Check if any document has meaningful content
        for doc in docs:
            if hasattr(doc, 'page_content') and doc.page_content.strip():
                return True
        
        return False