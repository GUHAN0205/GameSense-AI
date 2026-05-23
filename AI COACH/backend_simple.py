"""
Simple AI Game Coach Backend - Minimal Version
Use this if the enhanced version isn't working

This version works WITHOUT needing coach_agent.py
"""

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simple AI coach function built-in (no external file needed)
def simple_ai_coach(game, game_data):
    """Simple built-in AI coach"""
    win_rate = game_data.get('win_rate', 0)
    matches = game_data.get('matches', 0)
    wins = game_data.get('wins', 0)
    blunders = game_data.get('blunders', 0)
    
    feedback = f"🎯 {game.upper()} Performance Analysis\n\n"
    feedback += f"You've played {matches} matches with {wins} wins ({win_rate}% win rate).\n\n"
    
    if win_rate >= 70:
        feedback += "🌟 Excellent performance! You're playing at a high level.\n\n"
    elif win_rate >= 50:
        feedback += "👍 Good work! You're maintaining a positive record.\n\n"
    else:
        feedback += "📚 There's room for improvement. Let's work on your skills.\n\n"
    
    if blunders > matches * 0.2:
        feedback += "⚠️ You're making too many mistakes. Try to slow down and think through each move.\n\n"
    
    feedback += "💡 Keep practicing regularly to improve your skills!"
    
    return feedback

@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "message": "AI Game Coach Backend is Running 🚀",
        "version": "Simple"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "AI Game Coach"
    })

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Get data
        game = data.get("game", "")
        matches = int(data.get("matches", 0))
        wins = int(data.get("wins", 0))
        blunders = int(data.get("blunders", 0))
        endgame_losses = int(data.get("endgame_losses", 0))
        safe_moves = int(data.get("safe_moves", 0))
        risky_moves = int(data.get("risky_moves", 0))
        
        # Validate
        if matches <= 0:
            return jsonify({"error": "Matches must be greater than 0"}), 400
        
        if wins > matches:
            return jsonify({"error": "Wins cannot exceed matches"}), 400
        
        # Calculate stats
        win_rate = round((wins / matches * 100), 2) if matches > 0 else 0
        
        game_data = {
            "matches": matches,
            "wins": wins,
            "blunders": blunders,
            "endgame_losses": endgame_losses,
            "safe_moves": safe_moves,
            "risky_moves": risky_moves,
            "win_rate": win_rate
        }
        
        # Get feedback
        feedback = simple_ai_coach(game, game_data)
        
        return jsonify({
            "success": True,
            "game": game,
            "ai_coach_feedback": feedback,
            "stats_summary": {
                "total_matches": matches,
                "wins": wins,
                "losses": matches - wins,
                "win_rate": f"{win_rate}%"
            }
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    
    print("\n" + "=" * 50)
    print("🚀 AI Game Coach Backend (Simple Version)")
    print(f"📡 Running on http://localhost:{port}")
    print("=" * 50 + "\n")
    
    app.run(host="0.0.0.0", port=port, debug=True)
