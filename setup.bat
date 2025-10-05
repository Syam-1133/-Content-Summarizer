@echo off
REM Content Summarizer Setup Script for Windows
REM This script sets up the development environment

echo 🚀 Setting up Content Summarizer...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo ✅ Python found

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo ⬆️ Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo 📥 Installing dependencies...
if exist requirements-clean.txt (
    pip install -r requirements-clean.txt
) else (
    echo ⚠️ requirements-clean.txt not found, using requirements.txt
    pip install -r requirements.txt
)

REM Create .env file if it doesn't exist
if not exist .env (
    echo 🔧 Creating .env file...
    copy config\.env.example .env
    echo ⚠️ Please edit .env file and add your Groq API key
) else (
    echo ✅ .env file already exists
)

REM Create necessary directories
echo 📁 Creating directories...
if not exist logs mkdir logs
if not exist temp mkdir temp

echo.
echo 🎉 Setup complete!
echo.
echo Next steps:
echo 1. Activate the virtual environment: venv\Scripts\activate.bat
echo 2. Edit .env file and add your Groq API key
echo 3. Run the application: streamlit run app.py
echo.
echo Happy summarizing! 🚀
pause