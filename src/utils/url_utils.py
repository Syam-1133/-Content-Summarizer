"""
URL validation and processing utilities.
"""
import re
import validators
from typing import Tuple, Optional


def is_youtube_url(url: str) -> bool:
    """
    Check if URL is a valid YouTube URL and return normalized format.
    
    Args:
        url (str): The URL to validate
        
    Returns:
        bool: True if the URL is a valid YouTube URL, False otherwise
    """
    youtube_patterns = [
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/',
        r'(https?://)?(www\.)?youtu\.be/',
        r'(https?://)?(www\.)?youtube\.com/watch\?v=',
        r'(https?://)?(www\.)?youtube\.com/embed/',
        r'(https?://)?(www\.)?youtube\.com/v/'
    ]
    
    for pattern in youtube_patterns:
        if re.search(pattern, url):
            return True
    return False


def validate_url(url: str) -> Tuple[bool, Optional[str], Optional[str]]:
    """
    Validate URL and determine its type.
    
    Args:
        url (str): The URL to validate
        
    Returns:
        Tuple[bool, Optional[str], Optional[str]]: 
            (is_valid, content_type, error_message)
    """
    if not url:
        return False, None, "URL cannot be empty"
    
    if not validators.url(url):
        return False, None, "Invalid URL format"
    
    if is_youtube_url(url):
        return True, "youtube", None
    else:
        return True, "website", None


def get_content_type_display(content_type: str) -> str:
    """
    Get display name for content type.
    
    Args:
        content_type (str): The content type ('youtube' or 'website')
        
    Returns:
        str: Display name for the content type
    """
    content_types = {
        "youtube": "🎥 YouTube Video",
        "website": "🌐 Website Article"
    }
    return content_types.get(content_type, "🔗 Unknown Content")


def extract_domain(url: str) -> str:
    """
    Extract domain from URL for display purposes.
    
    Args:
        url (str): The URL to extract domain from
        
    Returns:
        str: The domain name
    """
    try:
        from urllib.parse import urlparse
        parsed = urlparse(url)
        return parsed.netloc
    except Exception:
        return "Unknown"