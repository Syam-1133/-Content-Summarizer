# Development Documentation

## Architecture Overview

The Content Summarizer application follows a clean, modular architecture with clear separation of concerns:

### Core Components

1. **Configuration Layer** (`config/`)
   - Centralized settings management
   - Environment variable handling
   - Application configuration validation

2. **Service Layer** (`src/services/`)
   - Content loading from various sources
   - AI-powered summarization
   - Error handling and retry logic

3. **UI Layer** (`src/components/`)
   - Reusable UI components
   - Styling and theming
   - User interaction handling

4. **Utility Layer** (`src/utils/`)
   - URL validation and processing
   - Text analysis and metrics
   - Common helper functions

### Design Patterns

- **Dependency Injection**: Services are injected into components
- **Factory Pattern**: Content loaders are created based on URL type
- **Strategy Pattern**: Different summarization strategies can be implemented
- **Observer Pattern**: Status updates throughout the processing pipeline

## API Documentation

### ContentLoader Service

```python
class ContentLoader:
    def load_content(self, url: str) -> List[Any]:
        """Load content from URL (auto-detects type)"""
    
    def load_youtube_content(self, url: str) -> List[Any]:
        """Load content from YouTube URL"""
    
    def load_website_content(self, url: str) -> List[Any]:
        """Load content from website URL"""
```

### SummarizationService

```python
class SummarizationService:
    def summarize_content(self, documents: List[Any], word_count: int = None) -> Dict[str, Any]:
        """Summarize content from documents"""
    
    def create_prompt_template(self, word_count: int = None) -> PromptTemplate:
        """Create a prompt template for summarization"""
```

## Testing Guidelines

### Unit Tests

- Test individual functions and methods
- Mock external dependencies (APIs, file systems)
- Use pytest fixtures for common test data

### Integration Tests

- Test complete workflows
- Use real API calls with test data
- Validate error handling scenarios

### UI Tests

- Test component rendering
- Validate user interactions
- Check responsive design

## Deployment

### Local Development

```bash
streamlit run app.py
```

### Production Deployment

1. **Streamlit Cloud**
   - Connect your GitHub repository
   - Set environment variables in settings
   - Deploy with one click

2. **Docker Deployment**
   ```dockerfile
   FROM python:3.9-slim
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 8501
   CMD ["streamlit", "run", "app.py"]
   ```

3. **Heroku Deployment**
   - Add `Procfile`: `web: streamlit run app.py --server.port=$PORT`
   - Set environment variables in Heroku dashboard

## Performance Optimization

### Content Loading

- Implement caching for frequently accessed content
- Use async/await for concurrent processing
- Add request timeouts and retry mechanisms

### UI Rendering

- Lazy load heavy components
- Use Streamlit's caching decorators
- Optimize CSS for better performance

### AI Processing

- Batch multiple requests when possible
- Implement request queuing for rate limiting
- Cache summarization results

## Security Considerations

### API Key Management

- Store API keys in environment variables
- Never commit keys to version control
- Use separate keys for development and production

### Input Validation

- Validate and sanitize all user inputs
- Check URL accessibility before processing
- Implement rate limiting for user requests

### Error Handling

- Don't expose internal error details to users
- Log errors securely for debugging
- Provide helpful error messages without revealing system internals