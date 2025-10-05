<div align="center">

# 🚀✨ Content Summarizer Pro ✨🚀

### *Transform lengthy content into actionable insights with AI precision*

<p align="center">
  <img src="https://img.shields.io/badge/AI-Powered-FF6B6B?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-success?style=flat-square" />
  <img src="https://img.shields.io/badge/Groq-Lightning%20Fast-00D4FF?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Maintained-Yes-success?style=flat-square" />
</p>

---

### 🎯 **What does this application do?**

Transform any YouTube video or web article into a **concise, well-structured summary** using state-of-the-art AI technology. Perfect for researchers, students, content creators, and busy professionals who need to quickly extract key insights from lengthy content.

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">
</p>

</div>

## 🎨 **Visual Preview**

<div align="center">

### � **Beautiful Dark Theme Interface**

<table>
<tr>
<td width="50%">

**🎯 Main Interface**
- Clean, modern design
- Glass morphism effects
- Responsive layout
- Professional gradient themes

</td>
<td width="50%">

**📊 Analytics Dashboard**
- Real-time processing metrics
- Content type detection
- Word count analysis
- Performance indicators

</td>
</tr>
</table>

<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="400">

</div>

---

## ✨ **Key Features**

<div align="center">

| 🎥 **YouTube Processing** | 🌐 **Web Article Analysis** | ⚡ **Lightning Speed** | 🎨 **Modern UI** |
|:-------------------------:|:---------------------------:|:----------------------:|:------------------:|
| Extract insights from video transcripts | Summarize articles from any website | Powered by Groq's fast LLMs | Beautiful dark theme interface |
| Support for all video lengths | Handle various content formats | Process content in seconds | Responsive & mobile-friendly |
| Automatic caption detection | Smart content extraction | Real-time progress tracking | Glass morphism effects |

</div>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="600">
</div>

## 🛠️ **Technology Stack & Architecture**

<div align="center">

### 🏗️ **Built with Modern Technologies**

<table>
<tr>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="80"/>
<br><strong>Frontend</strong>
<br>Streamlit + CSS
</td>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257460-738ff738-247f-4445-a718-cdd0ca76e2db.gif" width="80"/>
<br><strong>AI/ML</strong>
<br>LangChain + Groq
</td>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="80"/>
<br><strong>Backend</strong>
<br>Python Services
</td>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="80"/>
<br><strong>Content</strong>
<br>APIs & Loaders
</td>
</tr>
</table>

</div>

### 🔧 **Technology Details**

- **🎨 Frontend**: Streamlit with custom CSS styling and dark theme
- **🤖 AI/ML**: LangChain framework + Groq API (Llama 3.1 model)
- **🔍 Content Processing**: YouTube Transcript API, UnstructuredURLLoader
- **🐍 Language**: Python 3.8+ with modern async/await patterns
- **🏗️ Architecture**: Clean, modular design with service-oriented architecture

## 🏗️ **Project Architecture Deep Dive**

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284136-03988914-d42b-4505-b9d4-338b4d4e2e1f.gif" width="500">
</div>

### 📁 **How This Project Was Created**

This project evolved from a single monolithic file into a **professional, scalable application** through careful refactoring and architectural planning:

#### 🔄 **Evolution Process**

<details>
<summary><strong>📊 Phase 1: Analysis & Planning</strong></summary>

- **Problem Identification**: Original `main.py` had 400+ lines with mixed concerns
- **Architecture Design**: Planned modular structure with separation of concerns
- **Technology Selection**: Chose proven technologies (Streamlit, LangChain, Groq)
- **UI/UX Design**: Designed modern dark theme with glass morphism effects

</details>

<details>
<summary><strong>🛠️ Phase 2: Modular Refactoring</strong></summary>

- **Service Layer**: Extracted content loading and AI summarization logic
- **Component Layer**: Separated UI components and styling
- **Utility Layer**: Created reusable helper functions
- **Configuration Layer**: Centralized settings and environment management

</details>

<details>
<summary><strong>📦 Phase 3: Professional Structure</strong></summary>

- **Documentation**: Created comprehensive README, development guides
- **Testing**: Set up testing framework with unit tests
- **Deployment**: Added multiple deployment options (Docker, Heroku, etc.)
- **DevOps**: Created setup scripts for different platforms

</details>

### 🏛️ **Current Architecture**

```
📁 content-summarizer/
├── 🎯 app.py                    # Main application entry point
├── � config/                  # Configuration management
│   ├── settings.py             # Centralized app settings
│   └── .env.example           # Environment template
├── 🏗️ src/                     # Source code modules
│   ├── components/             # UI components & styling
│   ├── services/               # Business logic services
│   └── utils/                  # Helper utilities
├── 📚 docs/                    # Comprehensive documentation
├── 🧪 tests/                   # Unit tests & test framework
└── 🛠️ setup files             # Cross-platform setup scripts
```

## 🚀 **Quick Start Guide**

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="400">
</div>

### 📋 **Prerequisites**

<table>
<tr>
<td align="center" width="33%">
<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<br><strong>Python 3.8+</strong>
</td>
<td align="center" width="33%">
<img src="https://img.shields.io/badge/Groq-API%20Key-FF6B6B?style=for-the-badge&logo=key&logoColor=white" />
<br><strong>Groq API Key</strong>
</td>
<td align="center" width="33%">
<img src="https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white" />
<br><strong>Git (Optional)</strong>
</td>
</tr>
</table>

### ⚡ **Installation Steps**

<details>
<summary><strong>🔽 Click to expand installation guide</strong></summary>

#### 1️⃣ **Clone Repository**
```bash
git clone <your-repo-url>
cd content-summarizer
```

#### 2️⃣ **Automated Setup** (Recommended)
```bash
# 🐧 Linux/macOS
./setup.sh

# 🪟 Windows
setup.bat
```

#### 3️⃣ **Manual Setup** (Alternative)
```bash
# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements-clean.txt
```

#### 4️⃣ **Environment Configuration**
```bash
# Copy environment template
cp config/.env.example .env

# Edit .env file and add your API key
GROQ_API_KEY=your_actual_api_key_here
```

#### 5️⃣ **Launch Application**
```bash
streamlit run app.py
```

#### 6️⃣ **Access Application**
Open your browser and navigate to: `http://localhost:8501` 🚀

</details>

## 📖 **How to Use the Application**

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">
</div>

### 🎯 **Step-by-Step Usage Guide**

<table>
<tr>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="60"/>
<br><strong>1. Enter URL</strong>
<br>Paste YouTube or article link
</td>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257460-738ff738-247f-4445-a718-cdd0ca76e2db.gif" width="60"/>
<br><strong>2. AI Processing</strong>
<br>Click "Generate Summary"
</td>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="60"/>
<br><strong>3. Get Results</strong>
<br>Receive comprehensive summary
</td>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="60"/>
<br><strong>4. Analyze</strong>
<br>Review metrics & insights
</td>
</tr>
</table>

### 📊 **Supported Content Types**

<div align="center">

| Content Type | Status | Examples | Notes |
|:------------:|:------:|:--------:|:-----:|
| 🎥 **YouTube Videos** | ✅ | Educational, Reviews, Tutorials | Requires captions/transcripts |
| 📰 **News Articles** | ✅ | CNN, BBC, Reuters | Most news websites |
| 📚 **Blog Posts** | ✅ | Medium, Personal blogs | Public content |
| 📖 **Documentation** | ✅ | Technical docs, Help pages | API docs, guides |
| 🔬 **Research Papers** | ✅ | Academic articles | Accessible PDFs/web |

</div>

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

## 🔧 **Development & Customization**

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="400">
</div>

### 🧪 **Development Workflow**

<details>
<summary><strong>🔬 Running Tests</strong></summary>

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest tests/

# Run with coverage report
pytest --cov=src tests/

# Run specific test file
pytest tests/test_basic.py -v
```

</details>

<details>
<summary><strong>🏗️ Code Architecture</strong></summary>

The application follows **clean architecture principles**:

- **🎯 Services**: Handle business logic (content loading, AI processing)
- **🎨 Components**: Manage UI rendering and styling
- **🔧 Utils**: Provide utility functions for common tasks
- **⚙️ Config**: Centralized configuration management

**Key Design Patterns Used:**
- Dependency Injection
- Factory Pattern
- Strategy Pattern
- Observer Pattern

</details>

<details>
<summary><strong>✨ Adding New Features</strong></summary>

1. **New Content Sources**: Add loaders in `src/services/content_loader.py`
2. **UI Components**: Create components in `src/components/ui_components.py`
3. **Utility Functions**: Add helpers in `src/utils/`
4. **Configuration**: Update settings in `config/settings.py`
5. **Tests**: Add tests in `tests/` directory

</details>

### ⚙️ **Configuration Options**

<div align="center">

| Setting | Location | Purpose | Example |
|:-------:|:--------:|:-------:|:-------:|
| **API Keys** | `.env` | Authentication | `GROQ_API_KEY=xxx` |
| **Models** | `config/settings.py` | AI Configuration | `llama-3.1-8b-instant` |
| **UI Theme** | `src/components/styling.py` | Visual Appearance | Dark/Light themes |
| **Processing** | `config/settings.py` | Performance Tuning | Timeouts, retries |

</div>

## � **Deployment Options**

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284136-03988914-d42b-4505-b9d4-338b4d4e2e1f.gif" width="400">
</div>

### 🌐 **Multiple Deployment Platforms**

<table>
<tr>
<td align="center" width="25%">
<img src="https://img.shields.io/badge/Streamlit-Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
<br><strong>Streamlit Cloud</strong>
<br>✅ Free & Easy
<br>🔄 Auto-deploy from Git
</td>
<td align="center" width="25%">
<img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" />
<br><strong>Heroku</strong>
<br>⚡ Fast deployment
<br>📊 Built-in monitoring
</td>
<td align="center" width="25%">
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
<br><strong>Docker</strong>
<br>🐳 Containerized
<br>�🔧 Flexible hosting
</td>
<td align="center" width="25%">
<img src="https://img.shields.io/badge/Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white" />
<br><strong>Railway</strong>
<br>🚂 Modern platform
<br>⚡ Lightning fast
</td>
</tr>
</table>

<details>
<summary><strong>📋 Quick Deployment Commands</strong></summary>

**Streamlit Cloud (Recommended)**
```bash
git push origin main
# Visit share.streamlit.io and connect your repo
```

**Docker**
```bash
docker build -t content-summarizer .
docker run -p 8501:8501 -e GROQ_API_KEY=your_key content-summarizer
```

**Heroku**
```bash
heroku create your-app-name
heroku config:set GROQ_API_KEY=your_key
git push heroku main
```

</details>

## 🔧 **Troubleshooting & Support**

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="300">
</div>

### 🚨 **Common Issues & Solutions**

<details>
<summary><strong>🔐 API Key Issues</strong></summary>

**Problem**: "API Key not found" error
- ✅ Ensure `.env` file exists in project root
- ✅ Verify `GROQ_API_KEY` is set correctly  
- ✅ Restart application after changes
- ✅ Check for extra spaces or quotes in API key

</details>

<details>
<summary><strong>🔗 Content Loading Fails</strong></summary>

**Problem**: Unable to load content from URL
- ✅ Check internet connectivity
- ✅ Verify URL is publicly accessible
- ✅ Some websites block automated requests
- ✅ YouTube videos need captions/transcripts
- ✅ Try different URLs to isolate the issue

</details>

<details>
<summary><strong>🐌 Performance Issues</strong></summary>

**Problem**: Slow processing or timeouts
- ✅ Check internet connection speed
- ✅ Groq API may have rate limits
- ✅ Try with shorter content first
- ✅ Monitor system resources (CPU/Memory)

</details>

### 📞 **Getting Help**

<div align="center">

| Issue Type | Solution | Action |
|:----------:|:--------:|:------:|
| **🐛 Bugs** | Check troubleshooting in app | Report via Issues |
| **💡 Features** | Review roadmap | Suggest via Issues |
| **❓ Usage** | Read documentation | Ask in Discussions |
| **🔧 Technical** | Check logs & configs | Debug locally first |

</div>

## 🤝 **Contributing & Community**

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">
</div>

### 🌟 **How to Contribute**

We welcome contributions from the community! Here's how you can help:

<details>
<summary><strong>🔀 Contributing Code</strong></summary>

1. **Fork the repository**
   ```bash
   git fork https://github.com/your-username/content-summarizer
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-new-feature
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

4. **Commit your changes**
   ```bash
   git commit -m "✨ Add amazing new feature"
   ```

5. **Push and create PR**
   ```bash
   git push origin feature/amazing-new-feature
   ```

</details>

<details>
<summary><strong>🐛 Reporting Issues</strong></summary>

When reporting bugs, please include:
- 🖥️ **Operating System** (Windows, macOS, Linux)
- 🐍 **Python Version** (`python --version`)
- 📝 **Error Messages** (full stack trace)
- 🔗 **URL/Content** that caused the issue (if applicable)
- 📋 **Steps to Reproduce** the problem

</details>

### 🎯 **Contribution Areas**

<div align="center">

| Area | Skill Level | Examples |
|:----:|:-----------:|:--------:|
| **🐛 Bug Fixes** | Beginner | Fix typos, small bugs |
| **✨ Features** | Intermediate | New content sources, UI improvements |
| **🏗️ Architecture** | Advanced | Performance optimization, new services |
| **📚 Documentation** | All Levels | README improvements, tutorials |
| **🧪 Testing** | Intermediate | Unit tests, integration tests |

</div>

## 📄 **License & Acknowledgments**

<div align="center">

### 📜 **MIT License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

<img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge" />

</div>

### 🙏 **Special Thanks**

<table>
<tr>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="60"/>
<br><strong>Groq</strong>
<br>Lightning-fast AI inference
</td>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257460-738ff738-247f-4445-a718-cdd0ca76e2db.gif" width="60"/>
<br><strong>LangChain</strong>
<br>Excellent AI framework
</td>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="60"/>
<br><strong>Streamlit</strong>
<br>Amazing web app framework
</td>
<td align="center" width="25%">
<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="60"/>
<br><strong>Open Source</strong>
<br>Community & libraries
</td>
</tr>
</table>

## 📞 **Support the Project**

<div align="center">

If you find this project helpful, please consider:

<p>
<a href="#"><img src="https://img.shields.io/badge/⭐-Star%20this%20repo-yellow?style=for-the-badge" /></a>
<a href="#"><img src="https://img.shields.io/badge/🐛-Report%20bugs-red?style=for-the-badge" /></a>
<a href="#"><img src="https://img.shields.io/badge/💡-Suggest%20features-blue?style=for-the-badge" /></a>
<a href="#"><img src="https://img.shields.io/badge/🤝-Contribute-green?style=for-the-badge" /></a>
</p>

### � **Project Stats**

<img src="https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=flat-square" />
<img src="https://img.shields.io/badge/Maintained-Yes-success?style=flat-square" />
<img src="https://img.shields.io/badge/Python-3.8+-blue?style=flat-square" />
<img src="https://img.shields.io/badge/AI-Powered-orange?style=flat-square" />

</div>

---

<div align="center">

### 🚀 **Made with ❤️ and AI**

**Transform content • Amplify insights • Empower productivity**

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="600">

*Ready to revolutionize how you consume content? [Get started now!](#-quick-start-guide)*

</div>
