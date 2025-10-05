"""
AI-powered summarization service.
"""
from typing import List, Any, Dict
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from config.settings import Config


class SummarizationError(Exception):
    """Custom exception for summarization errors."""
    pass


class SummarizationService:
    """Service class for AI-powered content summarization."""
    
    def __init__(self):
        self.config = Config()
        self.llm = None
        self._initialize_llm()
    
    def _initialize_llm(self):
        """Initialize the LLM with proper error handling."""
        if not self.config.GROQ_API_KEY:
            raise SummarizationError("Groq API Key not found in environment variables")
        
        try:
            self.llm = ChatGroq(
                model=self.config.GROQ_MODEL,
                groq_api_key=self.config.GROQ_API_KEY
            )
        except Exception as e:
            raise SummarizationError(f"Failed to initialize Groq API: {str(e)}")
    
    def create_prompt_template(self, word_count: int = None) -> PromptTemplate:
        """
        Create a prompt template for summarization.
        
        Args:
            word_count (int, optional): Target word count for summary
            
        Returns:
            PromptTemplate: Configured prompt template
        """
        word_count = word_count or self.config.SUMMARY_WORD_COUNT
        
        prompt_text = f"""
        Provide a comprehensive and well-structured summary of the following content in approximately {word_count} words. 
        Focus on the main points, key insights, and important details. Structure your response with clear paragraphs
        and maintain the most crucial information while making it concise and readable.

        Content: {{text}}

        Summary:
        """
        
        return PromptTemplate(template=prompt_text, input_variables=["text"])
    
    def summarize_content(self, documents: List[Any], word_count: int = None) -> Dict[str, Any]:
        """
        Summarize content from documents.
        
        Args:
            documents (List[Any]): List of documents to summarize
            word_count (int, optional): Target word count for summary
            
        Returns:
            Dict[str, Any]: Summary result with metadata
            
        Raises:
            SummarizationError: If summarization fails
        """
        if not self.llm:
            raise SummarizationError("LLM not properly initialized")
        
        if not documents:
            raise SummarizationError("No documents provided for summarization")
        
        try:
            prompt = self.create_prompt_template(word_count)
            chain = load_summarize_chain(self.llm, chain_type="stuff", prompt=prompt)
            
            result = chain.invoke({"input_documents": documents})
            
            return {
                "summary": result["output_text"],
                "document_count": len(documents),
                "model_used": self.config.GROQ_MODEL,
                "word_count_target": word_count or self.config.SUMMARY_WORD_COUNT
            }
            
        except Exception as e:
            raise SummarizationError(f"Failed to generate summary: {str(e)}")
    
    def is_available(self) -> bool:
        """
        Check if the summarization service is available.
        
        Returns:
            bool: True if service is available
        """
        return self.llm is not None and self.config.GROQ_API_KEY != ""