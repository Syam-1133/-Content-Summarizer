"""
UI components for the Streamlit interface.
"""
import streamlit as st
from typing import List, Dict, Any


def render_header():
    """Render the main header section with animated logo."""
    st.markdown("""
    <div class="logo-section">
        <div class="logo-container">
            <div class="logo">🚀</div>
            <div class="logo">✨</div>
            <div class="logo">📝</div>
            <div class="logo">⚡</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-header">Content Summarizer</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Transform lengthy content into concise, actionable summaries with AI-powered precision</p>', unsafe_allow_html=True)


def render_sidebar_info():
    """Render the sidebar with app information."""
    st.markdown("### 🎯 How It Works")
    st.markdown("""
    <div style="line-height: 1.8;">
    <div style="display: flex; align-items: center; margin: 15px 0; padding: 10px; background: rgba(40, 40, 50, 0.5); border-radius: 10px;">
        <span style="font-size: 1.8rem; margin-right: 15px; color: #00d4ff;">🔗</span>
        <div>
            <div style="font-weight: 600; color: #ffffff;">Paste URL</div>
            <div style="font-size: 0.9rem; color: #b0b0b0;">YouTube or Article Link</div>
        </div>
    </div>
    <div style="display: flex; align-items: center; margin: 15px 0; padding: 10px; background: rgba(40, 40, 50, 0.5); border-radius: 10px;">
        <span style="font-size: 1.8rem; margin-right: 15px; color: #00d4ff;">⚡</span>
        <div>
            <div style="font-weight: 600; color: #ffffff;">AI Processing</div>
            <div style="font-size: 0.9rem; color: #b0b0b0;">Extract & Analyze Content</div>
        </div>
    </div>
    <div style="display: flex; align-items: center; margin: 15px 0; padding: 10px; background: rgba(40, 40, 50, 0.5); border-radius: 10px;">
        <span style="font-size: 1.8rem; margin-right: 15px; color: #00d4ff;">📊</span>
        <div>
            <div style="font-weight: 600; color: #ffffff;">Get Summary</div>
            <div style="font-size: 0.9rem; color: #b0b0b0;">Key Insights & Main Points</div>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📋 Supported Content")
    st.markdown("""
    <div style="background: rgba(40, 40, 50, 0.5); padding: 1rem; border-radius: 10px; line-height: 2;">
    <div>🎥 YouTube Videos</div>
    <div>🌐 News Articles</div>
    <div>📄 Blog Posts</div>
    <div>🔗 Web Pages</div>
    <div>📚 Documentation</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ⚡ Powered By")
    col_logo1, col_logo2 = st.columns(2)
    with col_logo1:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: rgba(40, 40, 50, 0.5); border-radius: 10px;">
            <div style="font-size: 2.5rem; color: #00d4ff;">🚀</div>
            <div style="font-weight: 600; color: #ffffff;">Groq AI</div>
            <div style="font-size: 0.8rem; color: #b0b0b0;">Lightning Fast</div>
        </div>
        """, unsafe_allow_html=True)
    with col_logo2:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: rgba(40, 40, 50, 0.5); border-radius: 10px;">
            <div style="font-size: 2.5rem; color: #00d4ff;">🔗</div>
            <div style="font-weight: 600; color: #ffffff;">LangChain</div>
            <div style="font-size: 0.8rem; color: #b0b0b0;">AI Framework</div>
        </div>
        """, unsafe_allow_html=True)


def render_url_input() -> str:
    """
    Render URL input field and return the entered URL.
    
    Returns:
        str: The entered URL
    """
    st.markdown("### 🔗 Enter Content URL")
    
    url = st.text_input(
        "Paste YouTube or website URL here:",
        placeholder="https://www.youtube.com/watch?v=... or https://example.com/article",
        label_visibility="collapsed",
        key="url_input"
    )
    
    return url


def render_process_button() -> bool:
    """
    Render the process button and return whether it was clicked.
    
    Returns:
        bool: True if button was clicked
    """
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        return st.button("🚀 Generate AI Summary", use_container_width=True)


def render_status_message(message_type: str, message: str):
    """
    Render a status message with appropriate styling.
    
    Args:
        message_type (str): Type of message ('success', 'error', 'info')
        message (str): The message to display
    """
    st.markdown(f'<div class="status-{message_type}">{message}</div>', unsafe_allow_html=True)


def render_summary(summary_text: str):
    """
    Render the summary text in a styled container.
    
    Args:
        summary_text (str): The summary text to display
    """
    st.markdown("### 📋 AI Summary")
    st.markdown(f'<div class="summary-card">{summary_text}</div>', unsafe_allow_html=True)


def render_metrics(metrics: List[Dict[str, Any]], content_type: str = ""):
    """
    Render metrics in a grid layout.
    
    Args:
        metrics (List[Dict[str, Any]]): List of metric dictionaries
        content_type (str): Type of content being displayed
    """
    st.markdown("### 📊 Summary Analytics")
    
    # Ensure we have exactly 4 columns
    cols = st.columns(4)
    
    # Add document count as first metric
    with cols[0]:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 2.5rem; color: #00d4ff;">📄</div>
            <div style="font-size: 1.8rem; font-weight: bold; color: #ffffff;">1</div>
            <div style="color: #b0b0b0;">Documents</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Add content type as second metric
    with cols[1]:
        content_type_icon = "🎥" if "youtube" in content_type.lower() else "🌐"
        content_type_text = "YouTube" if "youtube" in content_type.lower() else "Website"
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 2.5rem; color: #00d4ff;">{content_type_icon}</div>
            <div style="font-size: 1.2rem; font-weight: bold; color: #ffffff; margin: 0.5rem 0;">{content_type_text}</div>
            <div style="color: #b0b0b0;">Content Type</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Add remaining metrics
    for i, metric in enumerate(metrics[:2]):  # Only take first 2 metrics to fill remaining columns
        with cols[i + 2]:
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 2.5rem; color: #00d4ff;">{metric['icon']}</div>
                <div style="font-size: 1.8rem; font-weight: bold; color: #ffffff;">{metric['value']}</div>
                <div style="color: #b0b0b0;">{metric['label']}</div>
            </div>
            """, unsafe_allow_html=True)


def render_troubleshooting():
    """Render troubleshooting tips in an expander."""
    with st.expander("🔧 Troubleshooting Tips"):
        st.markdown("""
        **Common Solutions:**
        - 🔄 Refresh and try again
        - 🌐 Check your internet connection
        - 🔗 Verify the URL is correct and accessible
        - 📹 For YouTube: Ensure video has captions
        - 🏠 For websites: Some may block automated access
        
        **Still having issues?**
        - Try a different URL
        - Contact support if problem persists
        """)


def render_footer():
    """Render the application footer."""
    st.markdown("""
    <div class="footer">
        <div style="text-align: center;">
            <div style="display: flex; justify-content: center; gap: 30px; margin-bottom: 1rem; flex-wrap: wrap;">
                <div style="font-size: 1.1rem; font-weight: 600; color: #00d4ff;">📝 Content Summarizer Pro</div>
                <div style="font-size: 1.1rem; font-weight: 600; color: #00d4ff;">⚡ Powered by Groq AI</div>
                <div style="font-size: 1.1rem; font-weight: 600; color: #00d4ff;">🔗 Built with LangChain</div>
            </div>
            <div style="color: #b0b0b0; font-size: 0.9rem;">
                Transform lengthy content into actionable insights in seconds • Dark Theme Optimized
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)