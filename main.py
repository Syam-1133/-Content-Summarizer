import validators, streamlit as st
import os
import traceback
import re
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

def is_youtube_url(url):
    """Check if URL is a valid YouTube URL and return normalized format"""
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

# Streamlit APP Configuration
st.set_page_config(
    page_title="Content Summarizer", 
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dark Theme Professional CSS Styling
st.markdown("""
<style>
    /* Main dark theme styling */
    .main {
        background-color: #0f0f23;
        color: #ffffff;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
    }
    
    /* Header styling */
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #00d4ff, #00f2fe, #4facfe, #00f2fe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        font-weight: 800;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-shadow: 0 0 30px rgba(0, 242, 254, 0.3);
    }
    
    .sub-header {
        font-size: 1.3rem;
        color: #b0b0b0;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    /* Card styling - Glass morphism effect */
    .card {
        background: rgba(25, 25, 35, 0.8);
        border-radius: 20px;
        padding: 2.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 2rem;
    }
    
    .summary-card {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1) 0%, rgba(79, 172, 254, 0.1) 100%);
        color: #e0e0e0;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(0, 212, 255, 0.2);
        line-height: 1.6;
    }
    
    /* Input styling */
    .stTextInput>div>div>input {
        border-radius: 15px;
        border: 2px solid #333344;
        padding: 15px 20px;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        background: rgba(40, 40, 50, 0.8);
        color: #ffffff;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #00d4ff;
        box-shadow: 0 0 0 2px rgba(0, 212, 255, 0.3);
        background: rgba(50, 50, 60, 0.9);
    }
    
    .stTextInput>div>div>input::placeholder {
        color: #888899;
    }
    
    /* Button styling - UPDATED WITH BOLD TEXT */
    .stButton>button {
        border-radius: 15px;
        background: linear-gradient(45deg, #00d4ff, #4facfe);
        color: #0f0f23;
        border: none;
        padding: 18px 30px;
        font-size: 1.6rem;
        font-weight: 800;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        transition: all 0.3s ease;
        width: 100%;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 30px rgba(0, 212, 255, 0.5);
        background: linear-gradient(45deg, #4facfe, #00d4ff);
    }
    
    /* Make button text bold and prominent */
    .stButton>button div p {
        font-size: 1.6rem !important;
        font-weight: 800 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        margin: 0 !important;
        text-align: center !important;
        background: linear-gradient(45deg, #0f0f23, #1a1a2e) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: #0f0f23 !important;
        color: #0f0f23 !important;
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {
        background: linear-gradient(45deg, #00d4ff, #4facfe);
    }
    
    /* Metric cards */
    .metric-card {
        background: rgba(30, 30, 40, 0.9);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
        border-left: 4px solid #00d4ff;
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        border-left: 4px solid #4facfe;
    }
    
    /* Logo section */
    .logo-section {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .logo-container {
        display: inline-flex;
        align-items: center;
        gap: 25px;
        margin-bottom: 1rem;
    }
    
    .logo {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #00d4ff, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 10px rgba(0, 212, 255, 0.5));
    }
    
    /* Feature icons */
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        color: #00d4ff;
    }
    
    /* Status indicators */
    .status-success {
        background: linear-gradient(135deg, rgba(86, 171, 47, 0.2) 0%, rgba(168, 230, 207, 0.2) 100%);
        color: #56ab2f;
        padding: 1.2rem;
        border-radius: 12px;
        margin: 1rem 0;
        border: 1px solid rgba(86, 171, 47, 0.3);
        border-left: 5px solid #56ab2f;
    }
    
    .status-error {
        background: linear-gradient(135deg, rgba(255, 65, 108, 0.2) 0%, rgba(255, 75, 43, 0.2) 100%);
        color: #ff416c;
        padding: 1.2rem;
        border-radius: 12px;
        margin: 1rem 0;
        border: 1px solid rgba(255, 65, 108, 0.3);
        border-left: 5px solid #ff416c;
    }
    
    .status-info {
        background: linear-gradient(135deg, rgba(74, 0, 224, 0.2) 0%, rgba(142, 45, 226, 0.2) 100%);
        color: #8E2DE2;
        padding: 1.2rem;
        border-radius: 12px;
        margin: 1rem 0;
        border: 1px solid rgba(142, 45, 226, 0.3);
        border-left: 5px solid #8E2DE2;
    }
    
    /* Text styling */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    
    p, li, div {
        color: #cccccc !important;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: rgba(40, 40, 50, 0.8) !important;
        color: #ffffff !important;
        border-radius: 10px !important;
    }
    
    .streamlit-expanderContent {
        background: rgba(30, 30, 40, 0.8) !important;
        color: #cccccc !important;
        border-radius: 0 0 10px 10px !important;
    }
    
    /* Divider styling */
    hr {
        border-color: #333344 !important;
        margin: 2rem 0 !important;
    }
    
    /* Footer styling */
    .footer {
        background: rgba(20, 20, 30, 0.9);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Get Groq API Key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.markdown('<div class="status-error">❌ Groq API Key not found in environment variables. Please set GROQ_API_KEY in your .env file.</div>', unsafe_allow_html=True)
    st.stop()

# Initialize LLM
try:
    llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=groq_api_key)
except Exception as e:
    st.markdown(f'<div class="status-error">❌ Failed to initialize Groq API: {str(e)}</div>', unsafe_allow_html=True)
    st.stop()

# Header Section with Animated Logo
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

# Main content area
col1, col2 = st.columns([1, 2])

with col1:
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
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    
    st.markdown("### 🔗 Enter Content URL")
    
    # URL input with enhanced styling
    generic_url = st.text_input(
        "Paste YouTube or website URL here:",
        placeholder="https://www.youtube.com/watch?v=... or https://example.com/article",
        label_visibility="collapsed",
        key="url_input"
    )
    
    # Process button - This will now have bold text
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        process_clicked = st.button("🚀 Generate AI Summary", use_container_width=True)
    
    # Auto-detect URL type and provide feedback
    if generic_url and process_clicked:
        if validators.url(generic_url):
            with st.spinner("🔄 Processing your content... This may take a moment."):
                try:
                    # Determine content type
                    content_type = "🎥 YouTube Video" if is_youtube_url(generic_url) else "🌐 Website Article"
                    
                    # Loading content based on URL type
                    if is_youtube_url(generic_url):
                        st.markdown(f'<div class="status-info">📥 Loading {content_type} Content...</div>', unsafe_allow_html=True)
                        
                        try:
                            loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=True)
                            docs = loader.load()
                        except Exception as yt_error:
                            loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=False)
                            docs = loader.load()
                            
                    else:
                        st.markdown(f'<div class="status-info">📥 Loading {content_type} Content...</div>', unsafe_allow_html=True)
                        
                        loader = UnstructuredURLLoader(
                            urls=[generic_url],
                            ssl_verify=False,
                            headers={
                                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                "Accept-Language": "en-US,en;q=0.5",
                                "Accept-Encoding": "gzip, deflate",
                                "Connection": "keep-alive",
                                "Upgrade-Insecure-Requests": "1"
                            }
                        )
                        docs = loader.load()

                    if not docs or len(docs) == 0:
                        st.markdown('<div class="status-error">❌ No content was extracted from the URL. Please check if the URL contains accessible text content.</div>', unsafe_allow_html=True)
                    else:
                        # Generate summary
                        st.markdown('<div class="status-info">🧠 AI is analyzing and generating your summary...</div>', unsafe_allow_html=True)
                        
                        prompt_template = """
                        Provide a comprehensive and well-structured summary of the following content in approximately 300 words. 
                        Focus on the main points, key insights, and important details:

                        Content: {text}

                        Summary:
                        """
                        prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
                        
                        chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                        output_summary = chain.invoke({"input_documents": docs})
                        
                        st.markdown('<div class="status-success">✅ Summary Generated Successfully!</div>', unsafe_allow_html=True)
                        
                        # Display the summary in a nice box
                        st.markdown("### 📋 AI Summary")
                        st.markdown(f'<div class="summary-card">{output_summary["output_text"]}</div>', unsafe_allow_html=True)
                        
                        # Metrics section
                        st.markdown("### 📊 Summary Analytics")
                        col1, col2, col3, col4 = st.columns(4)
                        
                        with col1:
                            st.markdown(f"""
                            <div class="metric-card">
                                <div style="font-size: 2.5rem; color: #00d4ff;">📄</div>
                                <div style="font-size: 1.8rem; font-weight: bold; color: #ffffff;">{len(docs)}</div>
                                <div style="color: #b0b0b0;">Documents</div>
                            </div>
                            """, unsafe_allow_html=True)
                            
                        with col2:
                            content_type_icon = "🎥" if is_youtube_url(generic_url) else "🌐"
                            st.markdown(f"""
                            <div class="metric-card">
                                <div style="font-size: 2.5rem; color: #00d4ff;">{content_type_icon}</div>
                                <div style="font-size: 1.2rem; font-weight: bold; color: #ffffff; margin: 0.5rem 0;">{"YouTube" if is_youtube_url(generic_url) else "Website"}</div>
                                <div style="color: #b0b0b0;">Content Type</div>
                            </div>
                            """, unsafe_allow_html=True)
                            
                        with col3:
                            word_count = len(output_summary['output_text'].split())
                            st.markdown(f"""
                            <div class="metric-card">
                                <div style="font-size: 2.5rem; color: #00d4ff;">📝</div>
                                <div style="font-size: 1.8rem; font-weight: bold; color: #ffffff;">{word_count}</div>
                                <div style="color: #b0b0b0;">Words</div>
                            </div>
                            """, unsafe_allow_html=True)
                            
                        with col4:
                            char_count = len(output_summary['output_text'])
                            st.markdown(f"""
                            <div class="metric-card">
                                <div style="font-size: 2.5rem; color: #00d4ff;">⚡</div>
                                <div style="font-size: 1.8rem; font-weight: bold; color: #ffffff;">{char_count}</div>
                                <div style="color: #b0b0b0;">Characters</div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                except Exception as e:
                    st.markdown('<div class="status-error">❌ An error occurred while processing your request</div>', unsafe_allow_html=True)
                    
                    # Troubleshooting tips
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
        else:
            st.markdown('<div class="status-error">❌ Please enter a valid URL format (e.g., https://www.youtube.com/watch?v=...)</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Enhanced Footer
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