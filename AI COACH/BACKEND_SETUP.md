# Backend Setup Guide

This guide will help you set up and run the enhanced Flask backend for the AI Game Coach application.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation Steps

### 1. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install Flask==2.3.0
pip install flask-cors==4.0.0
pip install gunicorn==21.2.0  # For production deployment
```

Or create a `requirements.txt` file:

```txt
Flask==2.3.0
flask-cors==4.0.0
gunicorn==21.2.0
openai==1.3.0  # If using OpenAI for AI coaching
python-dotenv==1.0.0  # For environment variables
```

Then install:
```bash
pip install -r requirements.txt
```

### 3. Choose Your Coach Implementation

#### Option A: Use the Mock Coach (for testing)

Rename `coach_agent_mock.py` to `coach_agent.py`:
```bash
mv coach_agent_mock.py coach_agent.py
```

#### Option B: Implement Your Own AI Coach

Create `coach_agent.py` with your AI implementation:

```python
def ai_game_coach(game: str, game_data: dict) -> str:
    """
    Your AI implementation here
    
    Args:
        game: Name of the game
        game_data: Dictionary with game statistics
        
    Returns:
        Coaching feedback as string
    """
    # Your AI logic here
    # Could use OpenAI, Claude, or your custom model
    pass
```

Example using OpenAI:

```python
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def ai_game_coach(game: str, game_data: dict) -> str:
    prompt = f"""
    You are an expert {game} coach. Analyze these statistics and provide 
    personalized coaching advice:
    
    {game_data}
    
    Provide specific, actionable feedback to help improve performance.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert game coach."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content
```

### 4. Configure Environment Variables

Create a `.env` file in the backend directory:

```bash
# Flask Configuration
FLASK_APP=backend_enhanced.py
FLASK_ENV=development
DEBUG=True
PORT=5000

# AI Configuration (if using OpenAI)
OPENAI_API_KEY=your_api_key_here

# CORS (optional - defaults to allow all in development)
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

### 5. Run the Backend

#### Development Mode

```bash
python backend_enhanced.py
```

Or using Flask CLI:
```bash
flask run
```

The server will start on `http://localhost:5000`

#### Production Mode

```bash
gunicorn -w 4 -b 0.0.0.0:5000 backend_enhanced:app
```

Options:
- `-w 4`: Number of worker processes
- `-b 0.0.0.0:5000`: Bind to all interfaces on port 5000

## API Documentation

### Endpoints

#### GET /
Health check endpoint

**Response:**
```json
{
  "status": "running",
  "message": "AI Game Coach Backend is Running 🚀",
  "version": "2.0"
}
```

#### GET /health
Detailed health check

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00",
  "service": "AI Game Coach"
}
```

#### POST /analyze
Analyze game statistics

**Request:**
```json
{
  "game": "chess",
  "matches": 100,
  "wins": 60,
  "blunders": 15,
  "endgame_losses": 10,
  "safe_moves": 200,
  "risky_moves": 50
}
```

**Response:**
```json
{
  "success": true,
  "game": "chess",
  "ai_coach_feedback": "Your personalized feedback here...",
  "stats_summary": {
    "total_matches": 100,
    "wins": 60,
    "losses": 40,
    "win_rate": "60.0%"
  },
  "timestamp": "2024-01-01T12:00:00"
}
```

**Error Response:**
```json
{
  "error": "Validation failed",
  "details": ["Wins cannot exceed total matches"]
}
```

## Testing

### Using curl

```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "game": "chess",
    "matches": 100,
    "wins": 60,
    "blunders": 15,
    "endgame_losses": 10,
    "safe_moves": 200,
    "risky_moves": 50
  }'
```

### Using Python

```python
import requests

data = {
    "game": "chess",
    "matches": 100,
    "wins": 60,
    "blunders": 15,
    "endgame_losses": 10,
    "safe_moves": 200,
    "risky_moves": 50
}

response = requests.post('http://localhost:5000/analyze', json=data)
print(response.json())
```

### Using Postman

1. Create a new POST request
2. URL: `http://localhost:5000/analyze`
3. Headers: `Content-Type: application/json`
4. Body: Raw JSON (see request example above)
5. Send

## Troubleshooting

### Port Already in Use
```bash
# Find process using port 5000
lsof -i :5000  # macOS/Linux
netstat -ano | findstr :5000  # Windows

# Kill the process or use a different port
PORT=5001 python backend_enhanced.py
```

### CORS Issues
- Check that CORS is properly configured in `backend_enhanced.py`
- Verify frontend URL is in allowed origins
- Check browser console for specific CORS errors

### Module Not Found
```bash
# Ensure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

### AI Coach Errors
- Check that `coach_agent.py` exists and has the correct function signature
- If using OpenAI, verify API key is set
- Check logs for specific error messages

## Performance Optimization

### 1. Caching
Add Redis caching for repeated requests:

```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'redis'})

@app.route("/analyze", methods=["POST"])
@cache.cached(timeout=300, key_prefix=make_cache_key)
def analyze():
    # ... existing code
```

### 2. Rate Limiting
Protect against abuse:

```python
from flask_limiter import Limiter

limiter = Limiter(
    app,
    key_func=lambda: request.remote_addr,
    default_limits=["100 per hour"]
)

@app.route("/analyze", methods=["POST"])
@limiter.limit("10 per minute")
def analyze():
    # ... existing code
```

### 3. Async Processing
For slow AI responses:

```python
from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379')

@celery.task
def process_ai_feedback(game, game_data):
    return ai_game_coach(game, game_data)
```

## Monitoring

### Logging
The enhanced backend includes request logging. Check console output for:
- Request timestamps
- Endpoint access
- Request data
- Errors and exceptions

### Production Monitoring
Consider adding:
- Application Performance Monitoring (APM)
- Error tracking (Sentry)
- Health check endpoints
- Metrics collection (Prometheus)

## Security Checklist

- [ ] Set DEBUG=False in production
- [ ] Use environment variables for secrets
- [ ] Implement rate limiting
- [ ] Validate all inputs
- [ ] Use HTTPS in production
- [ ] Set proper CORS origins
- [ ] Keep dependencies updated
- [ ] Use secure headers (helmet)

## Next Steps

1. Implement your AI coach logic in `coach_agent.py`
2. Test all endpoints thoroughly
3. Set up environment variables
4. Configure CORS for your frontend
5. Deploy to production (see DEPLOYMENT.md)

For deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

---

Need help? Check the main README.md or create an issue.
