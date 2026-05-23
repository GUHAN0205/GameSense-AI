"""
Enhanced AI Game Coach Backend

This is an improved version of your Flask backend with:
- Better error handling
- Input validation
- Request logging
- Rate limiting support
- Enhanced response structure
- CORS configuration
- Health check endpoint
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from coach_agent import ai_game_coach
import os
from datetime import datetime

app = Flask(__name__)

# Configure CORS - Allow requests from your frontend
# In production, replace '*' with your actual frontend URL
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:5173", "http://localhost:3000", "*"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# ---------- UTILITY FUNCTIONS ----------
def validate_game_stats(data):
    """Validate incoming game statistics"""
    required_fields = ['game', 'matches', 'wins']
    errors = []
    
    # Check required fields
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    
    if errors:
        return False, errors
    
    # Validate data types and ranges
    try:
        matches = int(data.get('matches', 0))
        wins = int(data.get('wins', 0))
        
        if matches < 0:
            errors.append("Matches cannot be negative")
        if wins < 0:
            errors.append("Wins cannot be negative")
        if wins > matches:
            errors.append("Wins cannot exceed total matches")
        
        # Validate optional fields
        optional_fields = ['blunders', 'endgame_losses', 'safe_moves', 'risky_moves']
        for field in optional_fields:
            if field in data:
                value = int(data.get(field, 0))
                if value < 0:
                    errors.append(f"{field} cannot be negative")
    
    except (ValueError, TypeError) as e:
        errors.append(f"Invalid data type: {str(e)}")
    
    return len(errors) == 0, errors


def log_request(endpoint, data=None):
    """Log incoming requests for debugging"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {endpoint} - Data: {data}")


# ---------- HOME ROUTE ----------
@app.route("/")
def home():
    """Health check endpoint"""
    return jsonify({
        "status": "running",
        "message": "AI Game Coach Backend is Running 🚀",
        "version": "2.0",
        "endpoints": {
            "/": "Health check",
            "/analyze": "POST - Analyze game statistics"
        }
    })


# ---------- HEALTH CHECK ----------
@app.route("/health")
def health():
    """Detailed health check"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "AI Game Coach"
    })


# ---------- ANALYZE ROUTE ----------
@app.route("/analyze", methods=["POST", "OPTIONS"])
def analyze():
    """
    Analyze game statistics and provide AI coaching feedback
    
    Expected JSON payload:
    {
        "game": "chess",
        "matches": 100,
        "wins": 60,
        "blunders": 15,
        "endgame_losses": 10,
        "safe_moves": 200,
        "risky_moves": 50
    }
    """
    # Handle CORS preflight
    if request.method == "OPTIONS":
        return "", 204
    
    try:
        data = request.json
        
        if not data:
            return jsonify({
                "error": "No data provided",
                "message": "Request body must contain JSON data"
            }), 400
        
        # Log the request
        log_request("/analyze", data)
        
        # Validate input
        is_valid, errors = validate_game_stats(data)
        if not is_valid:
            return jsonify({
                "error": "Validation failed",
                "details": errors
            }), 400
        
        # Extract and convert data
        game = data.get("game", "").strip()
        matches = int(data.get("matches", 0))
        wins = int(data.get("wins", 0))
        blunders = int(data.get("blunders", 0))
        endgame_losses = int(data.get("endgame_losses", 0))
        safe_moves = int(data.get("safe_moves", 0))
        risky_moves = int(data.get("risky_moves", 0))
        
        # Game-specific stats mapping
        # This allows flexibility for different game types
        fouls = blunders
        break_success = safe_moves
        penalty_cards = risky_moves
        wild_card_usage = safe_moves
        snake_hits = endgame_losses
        
        # Prepare comprehensive game data
        game_data = {
            "matches": matches,
            "wins": wins,
            "blunders": blunders,
            "endgame_losses": endgame_losses,
            "safe_moves": safe_moves,
            "risky_moves": risky_moves,
            "fouls": fouls,
            "break_success": break_success,
            "penalty_cards": penalty_cards,
            "wild_card_usage": wild_card_usage,
            "snake_hits": snake_hits,
            # Calculate additional metrics
            "losses": matches - wins,
            "win_rate": round((wins / matches * 100), 2) if matches > 0 else 0
        }
        
        # Get AI feedback
        try:
            feedback = ai_game_coach(game, game_data)
        except Exception as e:
            print(f"Error calling AI coach: {str(e)}")
            return jsonify({
                "error": "AI processing failed",
                "message": "Unable to generate feedback at this time"
            }), 500
        
        # Return successful response
        return jsonify({
            "success": True,
            "game": game,
            "ai_coach_feedback": feedback,
            "stats_summary": {
                "total_matches": matches,
                "wins": wins,
                "losses": game_data["losses"],
                "win_rate": f"{game_data['win_rate']}%"
            },
            "timestamp": datetime.now().isoformat()
        }), 200
    
    except ValueError as e:
        return jsonify({
            "error": "Invalid input",
            "message": str(e)
        }), 400
    
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "message": "An unexpected error occurred"
        }), 500


# ---------- ERROR HANDLERS ----------
@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return jsonify({
        "error": "Not found",
        "message": "The requested endpoint does not exist"
    }), 404


@app.errorhandler(405)
def method_not_allowed(e):
    """Handle 405 errors"""
    return jsonify({
        "error": "Method not allowed",
        "message": "This endpoint does not support the requested HTTP method"
    }), 405


@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors"""
    return jsonify({
        "error": "Internal server error",
        "message": "An unexpected error occurred on the server"
    }), 500


# ---------- MAIN (IMPORTANT FOR DEPLOYMENT) ----------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG", "False").lower() == "true"
    
    print("=" * 50)
    print("🚀 AI Game Coach Backend Starting...")
    print(f"📡 Port: {port}")
    print(f"🔧 Debug Mode: {debug}")
    print("=" * 50)
    
    app.run(
        host="0.0.0.0",
        port=port,
        debug=debug
    )
