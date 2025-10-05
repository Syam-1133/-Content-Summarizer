"""
UI components for the Content Summarizer application.
"""

from .styling import apply_dark_theme
from .ui_components import (
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

__all__ = [
    'apply_dark_theme',
    'render_header',
    'render_sidebar_info',
    'render_url_input',
    'render_process_button',
    'render_status_message',
    'render_summary',
    'render_metrics',
    'render_troubleshooting',
    'render_footer'
]