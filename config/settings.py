"""
Configuration settings for the Content Summarizer application.
"""
import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Application configuration class."""
    
    # API Configuration
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
    
    # App Configuration
    APP_TITLE: str = "Content Summarizer"
    APP_ICON: str = "📝"
    PAGE_LAYOUT: str = "wide"
    
    # UI Configuration
    SIDEBAR_STATE: str = "collapsed"
    
    # Processing Configuration
    SUMMARY_WORD_COUNT: int = 300
    MAX_RETRIES: int = 3
    TIMEOUT_SECONDS: int = 30
    
    # Content Types
    SUPPORTED_CONTENT_TYPES: Dict[str, str] = {
        "youtube": "🎥 YouTube Video",
        "website": "🌐 Website Article"
    }
    
    # Headers for web scraping
    DEFAULT_HEADERS: Dict[str, str] = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate required configuration."""
        if not cls.GROQ_API_KEY:
            return False
        return True
    
    @classmethod
    def get_app_config(cls) -> Dict[str, Any]:
        """Get Streamlit app configuration."""
        return {
            "page_title": cls.APP_TITLE,
            "page_icon": cls.APP_ICON,
            "layout": cls.PAGE_LAYOUT,
            "initial_sidebar_state": cls.SIDEBAR_STATE
        }