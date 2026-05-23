"""
Mock AI Game Coach for Testing

This is a mock implementation of the ai_game_coach function for testing.
Replace this with your actual AI implementation.
"""

def ai_game_coach(game: str, game_data: dict) -> str:
    """
    Mock AI coach that provides game-specific feedback
    
    Args:
        game: Name of the game (chess, pool, uno, etc.)
        game_data: Dictionary containing game statistics
    
    Returns:
        Personalized coaching feedback as a string
    """
    
    matches = game_data.get('matches', 0)
    wins = game_data.get('wins', 0)
    win_rate = game_data.get('win_rate', 0)
    blunders = game_data.get('blunders', 0)
    endgame_losses = game_data.get('endgame_losses', 0)
    safe_moves = game_data.get('safe_moves', 0)
    risky_moves = game_data.get('risky_moves', 0)
    
    # Game-specific coaching templates
    feedback_templates = {
        'chess': generate_chess_feedback,
        'pool': generate_pool_feedback,
        'uno': generate_uno_feedback,
        'snakes_ladders': generate_snakes_feedback,
        'cricket': generate_cricket_feedback,
        'poker': generate_poker_feedback,
    }
    
    # Get the appropriate feedback generator
    generator = feedback_templates.get(game.lower(), generate_generic_feedback)
    
    return generator(game_data)


def generate_chess_feedback(data: dict) -> str:
    """Generate chess-specific feedback"""
    win_rate = data.get('win_rate', 0)
    blunders = data.get('blunders', 0)
    endgame_losses = data.get('endgame_losses', 0)
    
    feedback = f"🎯 Chess Performance Analysis\n\n"
    feedback += f"Your current win rate is {win_rate}%. "
    
    if win_rate >= 70:
        feedback += "Excellent performance! You're playing at a strong level.\n\n"
    elif win_rate >= 50:
        feedback += "Good work! You're maintaining a positive record.\n\n"
    else:
        feedback += "There's room for improvement. Let's work on your strategy.\n\n"
    
    if blunders > data['matches'] * 0.2:
        feedback += "⚠️ Blunders Alert: You're making too many tactical mistakes. "
        feedback += "Recommendation: Take more time to analyze positions before moving. "
        feedback += "Practice tactical puzzles daily to improve pattern recognition.\n\n"
    
    if endgame_losses > data['wins'] * 0.3:
        feedback += "📚 Endgame Focus: You're losing advantage in endgames. "
        feedback += "Recommendation: Study fundamental endgame positions like king and pawn endings. "
        feedback += "Practice converting winning positions.\n\n"
    
    feedback += "💡 Key Takeaway: "
    if blunders < 5:
        feedback += "Your tactical play is solid. Focus on strategic planning and opening preparation."
    else:
        feedback += "Reduce blunders by double-checking moves, especially in critical positions."
    
    return feedback


def generate_pool_feedback(data: dict) -> str:
    """Generate pool-specific feedback"""
    win_rate = data.get('win_rate', 0)
    break_success = data.get('break_success', 0)
    fouls = data.get('fouls', 0)
    
    feedback = f"🎱 Pool Performance Analysis\n\n"
    feedback += f"Win Rate: {win_rate}%\n\n"
    
    if break_success < data['matches'] * 0.4:
        feedback += "🎯 Break Shot: Your break needs improvement. "
        feedback += "Focus on consistent cue ball positioning and power control.\n\n"
    
    if fouls > data['matches'] * 0.15:
        feedback += "⚠️ Foul Management: Reduce unforced errors. "
        feedback += "Take your time to line up shots and ensure clean contact.\n\n"
    
    feedback += "💡 Recommendation: Practice position play and safety shots to gain tactical advantages."
    
    return feedback


def generate_uno_feedback(data: dict) -> str:
    """Generate Uno-specific feedback"""
    win_rate = data.get('win_rate', 0)
    wild_card_usage = data.get('wild_card_usage', 0)
    risky_moves = data.get('risky_moves', 0)
    
    feedback = f"🃏 Uno Performance Analysis\n\n"
    feedback += f"Win Rate: {win_rate}%\n\n"
    
    if wild_card_usage < data['matches'] * 0.3:
        feedback += "🎴 Wild Card Strategy: You may be holding wild cards too long. "
        feedback += "Use them strategically to change momentum.\n\n"
    
    if risky_moves > data['matches'] * 0.5:
        feedback += "⚠️ Risk Management: Balance aggressive plays with defensive strategies.\n\n"
    
    feedback += "💡 Key Tip: Track opponents' card counts and colors to make better decisions."
    
    return feedback


def generate_snakes_feedback(data: dict) -> str:
    """Generate Snakes & Ladders feedback"""
    win_rate = data.get('win_rate', 0)
    
    feedback = f"🎲 Snakes & Ladders Analysis\n\n"
    feedback += f"Win Rate: {win_rate}%\n\n"
    
    feedback += "This is primarily a game of chance, but positioning awareness helps. "
    feedback += "Stay positive and enjoy the game!\n\n"
    feedback += "💡 Remember: Luck evens out over many games. Keep playing and have fun!"
    
    return feedback


def generate_cricket_feedback(data: dict) -> str:
    """Generate cricket-specific feedback"""
    win_rate = data.get('win_rate', 0)
    risky_moves = data.get('risky_moves', 0)
    safe_moves = data.get('safe_moves', 0)
    
    feedback = f"🏏 Cricket Performance Analysis\n\n"
    feedback += f"Win Rate: {win_rate}%\n\n"
    
    if risky_moves > safe_moves:
        feedback += "⚠️ Shot Selection: You're taking too many risks. "
        feedback += "Balance aggressive shots with defensive technique.\n\n"
    
    feedback += "💡 Focus Areas: Work on timing, footwork, and reading the bowler's delivery."
    
    return feedback


def generate_poker_feedback(data: dict) -> str:
    """Generate poker-specific feedback"""
    win_rate = data.get('win_rate', 0)
    blunders = data.get('blunders', 0)
    risky_moves = data.get('risky_moves', 0)
    
    feedback = f"♠️ Poker Performance Analysis\n\n"
    feedback += f"Win Rate: {win_rate}%\n\n"
    
    if blunders > data['matches'] * 0.15:
        feedback += "🎯 Decision Making: Reduce costly mistakes by following optimal strategy. "
        feedback += "Study hand ranges and pot odds.\n\n"
    
    if risky_moves > data['matches'] * 0.6:
        feedback += "⚠️ Aggression: Balance your aggressive plays with position and stack sizes.\n\n"
    
    feedback += "💡 Key Skills: Master position play, hand reading, and bankroll management."
    
    return feedback


def generate_generic_feedback(data: dict) -> str:
    """Generate generic feedback for unknown games"""
    win_rate = data.get('win_rate', 0)
    
    feedback = f"🎮 Game Performance Analysis\n\n"
    feedback += f"Win Rate: {win_rate}%\n\n"
    
    if win_rate >= 60:
        feedback += "Great performance! You're playing well. "
        feedback += "Keep practicing to maintain your edge.\n\n"
    elif win_rate >= 40:
        feedback += "Solid performance. "
        feedback += "Focus on consistency and learning from losses.\n\n"
    else:
        feedback += "There's significant room for improvement. "
        feedback += "Analyze your gameplay and identify weak areas.\n\n"
    
    feedback += "💡 General Tips: Practice regularly, study strategies, and learn from experienced players."
    
    return feedback


# Example usage
if __name__ == "__main__":
    # Test the coach with sample data
    test_data = {
        "matches": 100,
        "wins": 65,
        "win_rate": 65,
        "blunders": 12,
        "endgame_losses": 8,
        "safe_moves": 150,
        "risky_moves": 45
    }
    
    print("Testing Chess Feedback:")
    print("-" * 50)
    print(ai_game_coach("chess", test_data))
