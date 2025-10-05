#!/bin/bash

# Content Summarizer Setup Script
# This script sets up the development environment

set -e

echo "🚀 Setting up Content Summarizer..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python $required_version or higher is required. Found: $python_version"
    exit 1
fi

echo "✅ Python $python_version found"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing dependencies..."
if [ -f "requirements-clean.txt" ]; then
    pip install -r requirements-clean.txt
else
    echo "⚠️ requirements-clean.txt not found, using requirements.txt"
    pip install -r requirements.txt
fi

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "🔧 Creating .env file..."
    cp config/.env.example .env
    echo "⚠️ Please edit .env file and add your Groq API key"
else
    echo "✅ .env file already exists"
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p logs
mkdir -p temp

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Edit .env file and add your Groq API key"
echo "3. Run the application: streamlit run app.py"
echo ""
echo "Happy summarizing! 🚀"