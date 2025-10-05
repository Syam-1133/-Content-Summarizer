"""
Content processing utilities.
"""
from typing import List, Dict, Any


def calculate_text_metrics(text: str) -> Dict[str, int]:
    """
    Calculate various metrics for text content.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        Dict[str, int]: Dictionary containing word count, character count, etc.
    """
    words = text.split()
    return {
        "word_count": len(words),
        "character_count": len(text),
        "character_count_no_spaces": len(text.replace(" ", "")),
        "sentence_count": len([s for s in text.split('.') if s.strip()]),
        "paragraph_count": len([p for p in text.split('\n\n') if p.strip()])
    }


def format_metrics_for_display(metrics: Dict[str, int]) -> List[Dict[str, Any]]:
    """
    Format metrics for display in the UI.
    
    Args:
        metrics (Dict[str, int]): The metrics dictionary
        
    Returns:
        List[Dict[str, Any]]: Formatted metrics for UI display
    """
    return [
        {
            "icon": "📝",
            "value": metrics["word_count"],
            "label": "Words",
            "color": "#00d4ff"
        },
        {
            "icon": "⚡",
            "value": metrics["character_count"],
            "label": "Characters",
            "color": "#00d4ff"
        },
        {
            "icon": "📄",
            "value": metrics["sentence_count"],
            "label": "Sentences",
            "color": "#00d4ff"
        },
        {
            "icon": "📋",
            "value": metrics["paragraph_count"],
            "label": "Paragraphs",
            "color": "#00d4ff"
        }
    ]


def truncate_text(text: str, max_length: int = 100) -> str:
    """
    Truncate text to specified length with ellipsis.
    
    Args:
        text (str): The text to truncate
        max_length (int): Maximum length before truncation
        
    Returns:
        str: Truncated text with ellipsis if needed
    """
    if len(text) <= max_length:
        return text
    return text[:max_length].rsplit(' ', 1)[0] + "..."