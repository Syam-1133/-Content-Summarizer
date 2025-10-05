"""
Streamlit styling and theme configuration.
"""
import streamlit as st


def apply_dark_theme():
    """Apply dark theme CSS styling to the Streamlit app."""
    
    dark_theme_css = """
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
        
        /* Button styling */
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
    """
    
    st.markdown(dark_theme_css, unsafe_allow_html=True)