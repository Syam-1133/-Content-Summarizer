# Deployment Guide

This guide covers various deployment options for the Content Summarizer application.

## Prerequisites

- Python 3.8+
- Groq API Key
- Git repository (for cloud deployments)

## Deployment Options

### 1. Streamlit Cloud (Recommended)

Streamlit Cloud is the easiest way to deploy Streamlit applications.

#### Steps:

1. **Push code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Visit Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub

3. **Deploy App**
   - Click "New app"
   - Select your repository
   - Set main file path: `app.py`
   - Add secrets in "Advanced settings":
     ```toml
     GROQ_API_KEY = "your_api_key_here"
     ```

4. **Deploy**
   - Click "Deploy!"
   - Your app will be available at `https://your-app-name.streamlit.app`

### 2. Heroku Deployment

#### Setup Files:

1. **Create `Procfile`**:
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Create `runtime.txt`**:
   ```
   python-3.9.20
   ```

#### Deploy Steps:

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   
   # Windows
   # Download from heroku.com
   ```

2. **Login and Create App**
   ```bash
   heroku login
   heroku create your-app-name
   ```

3. **Set Environment Variables**
   ```bash
   heroku config:set GROQ_API_KEY=your_api_key_here
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

### 3. Docker Deployment

#### Create `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy application code
COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  content-summarizer:
    build: .
    ports:
      - "8501:8501"
    environment:
      - GROQ_API_KEY=${GROQ_API_KEY}
    volumes:
      - .:/app
    restart: unless-stopped
```

#### Deploy:

```bash
# Build and run
docker-compose up --build

# Or build and run separately
docker build -t content-summarizer .
docker run -p 8501:8501 -e GROQ_API_KEY=your_key content-summarizer
```

### 4. Railway Deployment

1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login and Deploy**
   ```bash
   railway login
   railway init
   railway add --service
   railway deploy
   ```

3. **Set Environment Variables**
   ```bash
   railway variables set GROQ_API_KEY=your_api_key_here
   ```

### 5. DigitalOcean App Platform

1. **Create `app.yaml`**:
   ```yaml
   name: content-summarizer
   services:
   - name: web
     source_dir: /
     github:
       repo: your-username/content-summarizer
       branch: main
     run_command: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
     environment_slug: python
     instance_count: 1
     instance_size_slug: basic-xxs
     envs:
     - key: GROQ_API_KEY
       value: your_api_key_here
       type: SECRET
   ```

2. **Deploy via DigitalOcean Console**
   - Go to App Platform in DigitalOcean
   - Create new app from GitHub
   - Select your repository
   - Configure environment variables

## Environment Variables

Set these environment variables in your deployment:

```bash
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.1-8b-instant  # Optional, defaults to this
```

## Post-Deployment Checklist

- [ ] Verify the app loads correctly
- [ ] Test URL input and processing
- [ ] Check error handling with invalid URLs
- [ ] Verify API key is working
- [ ] Test with different content types (YouTube, websites)
- [ ] Check mobile responsiveness
- [ ] Monitor performance and logs

## Monitoring and Maintenance

### Health Checks

Add health check endpoints for monitoring:

```python
@st.cache_data
def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}
```

### Logging

Configure structured logging:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### Performance Monitoring

- Monitor response times
- Track API usage and costs
- Set up alerts for errors
- Monitor resource usage (CPU, memory)

## Troubleshooting

### Common Issues:

1. **Port Configuration**
   - Ensure the app binds to the correct port
   - Use `--server.port=$PORT` for cloud deployments

2. **Dependencies**
   - Verify all dependencies are in `requirements.txt`
   - Check Python version compatibility

3. **Environment Variables**
   - Ensure API keys are set correctly
   - Check variable names match exactly

4. **Memory Limits**
   - Optimize memory usage for free tiers
   - Consider upgrading plans for production

### Debug Steps:

1. Check application logs
2. Verify environment variables
3. Test locally with same configuration
4. Check network connectivity
5. Validate API endpoints

## Security Best Practices

- Never commit API keys to version control
- Use environment variables for all secrets
- Implement rate limiting
- Validate all user inputs
- Keep dependencies updated
- Use HTTPS in production
- Monitor for security vulnerabilities