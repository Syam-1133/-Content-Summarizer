"""
Content Summarizer Application
A modern Streamlit application for summarizing YouTube videos and web articles using AI.
"""
import streamlit as st
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config.settings import Config
from src.components import (
    apply_dark_theme,
    render_header,
    render_sidebar_info, 
    render_url_input,
    render_process_button,
    render_status_message,
    render_summary,
    render_metrics,
    render_troubleshooting,
    render_footer
)
from src.services import ContentLoader, ContentLoaderError, SummarizationService, SummarizationError
from src.utils import validate_url, get_content_type_display, calculate_text_metrics, format_metrics_for_display


def initialize_app():
    """Initialize the Streamlit application with configuration."""
    config = Config()
    
    # Configure Streamlit page
    st.set_page_config(**config.get_app_config())
    
    # Apply dark theme styling
    apply_dark_theme()
    
    return config


def check_configuration(config: Config) -> bool:
    """
    Check if the application is properly configured.
    
    Args:
        config (Config): Application configuration
        
    Returns:
        bool: True if configuration is valid
    """
    if not config.validate_config():
        render_status_message(
            "error", 
            "❌ Groq API Key not found in environment variables. Please set GROQ_API_KEY in your .env file."
        )
        st.stop()
        return False
    return True


def initialize_services() -> tuple:
    """
    Initialize application services.
    
    Returns:
        tuple: (content_loader, summarization_service)
    """
    try:
        content_loader = ContentLoader()
        summarization_service = SummarizationService()
        return content_loader, summarization_service
    except (ContentLoaderError, SummarizationError) as e:
        render_status_message("error", f"❌ Failed to initialize services: {str(e)}")
        st.stop()


def process_content(url: str, content_loader: ContentLoader, summarization_service: SummarizationService):
    """
    Process content from URL and generate summary.
    
    Args:
        url (str): URL to process
        content_loader (ContentLoader): Content loading service
        summarization_service (SummarizationService): Summarization service
    """
    # Validate URL
    is_valid, content_type, error_message = validate_url(url)
    
    if not is_valid:
        render_status_message("error", f"❌ {error_message}")
        return
    
    content_type_display = get_content_type_display(content_type)
    
    with st.spinner("🔄 Processing your content... This may take a moment."):
        try:
            # Load content
            render_status_message("info", f"📥 Loading {content_type_display} Content...")
            
            docs = content_loader.load_content(url)
            
            if not content_loader.validate_documents(docs):
                render_status_message(
                    "error", 
                    "❌ No content was extracted from the URL. Please check if the URL contains accessible text content."
                )
                render_troubleshooting()
                return
            
            # Generate summary
            render_status_message("info", "🧠 AI is analyzing and generating your summary...")
            
            summary_result = summarization_service.summarize_content(docs)
            
            render_status_message("success", "✅ Summary Generated Successfully!")
            
            # Display results
            render_summary(summary_result["summary"])
            
            # Calculate and display metrics
            text_metrics = calculate_text_metrics(summary_result["summary"])
            formatted_metrics = format_metrics_for_display(text_metrics)
            
            render_metrics(formatted_metrics, content_type_display)
            
        except (ContentLoaderError, SummarizationError) as e:
            render_status_message("error", f"❌ An error occurred while processing your request: {str(e)}")
            render_troubleshooting()
        except Exception as e:
            render_status_message("error", "❌ An unexpected error occurred while processing your request")
            render_troubleshooting()


def main():
    """Main application function."""
    # Initialize application
    config = initialize_app()
    
    # Check configuration
    if not check_configuration(config):
        return
    
    # Initialize services
    content_loader, summarization_service = initialize_services()
    
    # Render UI
    render_header()
    
    # Main content layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        render_sidebar_info()
    
    with col2:
        # URL input and processing
        url = render_url_input()
        process_clicked = render_process_button()
        
        # Process content if button clicked and URL provided
        if url and process_clicked:
            process_content(url, content_loader, summarization_service)
    
    # Render footer
    render_footer()


if __name__ == "__main__":
    main()