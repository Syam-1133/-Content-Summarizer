# 🚀 Content Summarizer

A modern, AI-powered web application built with Streamlit that transforms lengthy YouTube videos and web articles into concise, actionable summaries using cutting-edge language models.

![Content Summarizer](https://img.shields.io/badge/AI-Powered-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- 🎥 **YouTube Video Summarization** - Extract key insights from video transcripts
- 🌐 **Web Article Processing** - Summarize articles from any accessible website
- ⚡ **Lightning Fast** - Powered by Groq's high-performance LLMs
- 🎨 **Beautiful Dark UI** - Modern, responsive interface with glass morphism effects
- 📊 **Analytics Dashboard** - Track content metrics and processing statistics
- 🔧 **Error Handling** - Robust error handling with helpful troubleshooting tips
- 🔒 **Secure** - Environment-based API key management

## 🛠️ Technology Stack

- **Frontend**: Streamlit with custom CSS styling
- **AI/ML**: LangChain + Groq API (Llama 3.1)
- **Content Loading**: YouTube Transcript API, UnstructuredURLLoader
- **Language**: Python 3.8+
- **Architecture**: Modular, service-oriented design

## 📁 Project Structure

```
content-summarizer/
├── 📁 src/
│   ├── 📁 components/          # UI components and styling
│   │   ├── __init__.py
│   │   ├── styling.py          # CSS themes and styling
│   │   └── ui_components.py    # Reusable UI components
│   ├── 📁 services/            # Business logic services
│   │   ├── __init__.py
│   │   ├── content_loader.py   # Content loading from URLs
│   │   └── summarization.py    # AI summarization service
│   └── 📁 utils/               # Utility functions
│       ├── __init__.py
│       ├── text_utils.py       # Text processing utilities
│       └── url_utils.py        # URL validation and processing
├── 📁 config/                  # Configuration files
│   ├── .env.example           # Environment variables template
│   └── settings.py            # Application settings
├── 📁 docs/                   # Documentation
├── 📁 tests/                  # Unit tests
├── 📁 assets/                 # Static assets
├── app.py                     # Main application entry point
├── main.py                    # Legacy main file (can be removed)
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API Key ([Get one here](https://groq.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd content-summarizer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example env file
   cp config/.env.example .env
   
   # Edit .env and add your Groq API key
   # GROQ_API_KEY=your_actual_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   - Navigate to `http://localhost:8501`
   - Start summarizing content! 🎉

## 📖 Usage

1. **Enter URL**: Paste a YouTube video URL or web article link
2. **Click Process**: Hit the "🚀 Generate AI Summary" button
3. **Get Results**: Receive a comprehensive summary with analytics
4. **Review Metrics**: Check processing statistics and content insights

### Supported Content Types

- ✅ YouTube videos with transcripts/captions
- ✅ News articles and blog posts
- ✅ Documentation and help pages
- ✅ Research papers and academic content
- ✅ Most publicly accessible web content

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.1-8b-instant
```

### Application Settings

Modify `config/settings.py` to customize:

- Summary word count target
- Timeout settings
- UI configuration
- Default headers for web scraping

## 🧪 Development

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/

# Run with coverage
pytest --cov=src tests/
```

### Code Structure

The application follows a clean, modular architecture:

- **Services**: Handle business logic (content loading, summarization)
- **Components**: Manage UI rendering and styling
- **Utils**: Provide utility functions for common tasks
- **Config**: Centralized configuration management

### Adding New Features

1. Create new service modules in `src/services/`
2. Add UI components in `src/components/`
3. Implement utility functions in `src/utils/`
4. Update configuration in `config/settings.py`
5. Add tests in `tests/`

## 🔧 Troubleshooting

### Common Issues

**API Key Not Found**
- Ensure `.env` file exists in project root
- Verify `GROQ_API_KEY` is set correctly
- Restart the application after changes

**Content Loading Fails**
- Check internet connectivity
- Verify URL is accessible
- Some websites may block automated requests
- YouTube videos need captions/transcripts

**Slow Performance**
- Check your internet connection
- Groq API may have rate limits
- Try with shorter content

### Getting Help

- Check the troubleshooting section in the app
- Review error messages for specific guidance
- Ensure all dependencies are properly installed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for providing lightning-fast AI inference
- [LangChain](https://langchain.com/) for the excellent AI framework
- [Streamlit](https://streamlit.io/) for the amazing web app framework
- The open-source community for various tools and libraries

## 📞 Support

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs via issues
- 💡 Suggesting new features
- 🤝 Contributing to the codebase

---

**Made with ❤️ and AI** | Transform content, amplify insights
