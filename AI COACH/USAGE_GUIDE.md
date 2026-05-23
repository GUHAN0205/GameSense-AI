# AI Game Coach - Usage Guide

Complete guide for using the AI Game Coach application.

## For End Users

### Getting Started

1. **Open the Application**
   - Navigate to the deployed URL or `http://localhost:5173` for local development

2. **Select Your Game**
   - Choose from 6 available games:
     - ♟️ **Chess** - Strategic board game
     - 🎱 **Pool** - Precision cue sport
     - 🃏 **Uno** - Fast-paced card game
     - 🎲 **Snakes & Ladders** - Classic dice game
     - 🏏 **Cricket** - Bat and ball sport
     - ♠️ **Poker** - Strategic card game

3. **Enter Your Statistics**
   - **Total Matches**: Total number of games played
   - **Wins**: Number of games won
   - **Blunders/Mistakes**: Significant errors made
   - **Endgame Losses**: Games lost in the final phase
   - **Safe Moves**: Conservative plays made
   - **Risky Moves**: Aggressive plays attempted

4. **Get AI Coaching**
   - Click "Get AI Coaching" button
   - Wait for AI analysis (usually 2-5 seconds)
   - Review your personalized feedback

5. **Read Your Feedback**
   - Review strengths and weaknesses
   - Note specific recommendations
   - Check quick tips for your game
   - Apply advice in future games

### Understanding Your Stats

#### Win Rate
- **Excellent**: 70%+ - You're playing at a high level
- **Good**: 50-70% - Solid performance with room to grow
- **Developing**: Below 50% - Focus on fundamentals

#### Performance Metrics

**Blunders**
- Low (< 10% of matches): Excellent decision making
- Medium (10-20%): Room for improvement
- High (> 20%): Need to slow down and think more

**Endgame Performance**
- Strong: < 20% endgame losses
- Average: 20-40%
- Weak: > 40% - Focus on endgame practice

**Risk vs. Safety**
- Balanced: Similar safe and risky moves
- Conservative: More safe moves
- Aggressive: More risky moves

### Tips for Best Results

1. **Be Honest with Stats**
   - Accurate data = better coaching
   - Track stats over time

2. **Update Regularly**
   - Re-analyze after every 10-20 games
   - Track your progress

3. **Follow Recommendations**
   - Implement one tip at a time
   - Practice specific weaknesses

4. **Compare Over Time**
   - Keep a record of feedback
   - Note improvements

## For Developers

### Quick Start

```bash
# Frontend
npm install
npm run dev

# Backend (in separate terminal)
python backend_enhanced.py
```

### Project Structure

```
ai-game-coach/
├── src/
│   ├── components/
│   │   ├── Header.tsx          # App header
│   │   ├── Footer.tsx          # App footer
│   │   ├── GameSelector.tsx    # Game selection
│   │   ├── StatsForm.tsx       # Stats input
│   │   ├── FeedbackDisplay.tsx # AI feedback
│   │   ├── GameTips.tsx        # Quick tips
│   │   └── QuickStats.tsx      # Stats cards
│   ├── App.tsx                 # Main component
│   ├── main.tsx                # Entry point
│   └── index.css               # Global styles
├── backend_enhanced.py         # Enhanced Flask API
├── coach_agent_mock.py         # Mock AI coach
├── README.md                   # Main documentation
├── DEPLOYMENT.md               # Deployment guide
├── BACKEND_SETUP.md            # Backend setup
├── TESTING.md                  # Testing guide
└── USAGE_GUIDE.md             # This file
```

### Customization Guide

#### Adding New Games

1. **Update GameSelector.tsx**
```typescript
{
  id: 'new_game',
  name: 'New Game',
  icon: '🎮',
  description: 'Game description',
  gradient: 'from-blue-600 to-cyan-600'
}
```

2. **Add Game Tips in GameTips.tsx**
```typescript
new_game: [
  'Tip 1',
  'Tip 2',
  'Tip 3',
  'Tip 4',
]
```

3. **Update Backend Coach Logic**
```python
# In coach_agent.py
def generate_new_game_feedback(data: dict) -> str:
    # Your game-specific feedback logic
    return feedback
```

#### Customizing Styles

All styling uses Tailwind CSS. Modify colors, spacing, etc. in component files.

**Color Scheme:**
- Primary: Indigo (indigo-600)
- Secondary: Purple (purple-600)
- Accent: Pink (pink-600)
- Success: Green (green-600)
- Warning: Orange (orange-600)
- Error: Red (red-600)

#### Modifying Stats Fields

To add new stat fields:

1. **Update GameStats interface** in `App.tsx`:
```typescript
export interface GameStats {
  matches: number;
  wins: number;
  // ... existing fields
  new_field: number; // Add new field
}
```

2. **Update StatsForm.tsx** with new input field

3. **Update backend** to handle new field

### API Integration

#### Endpoint
```
POST /analyze
```

#### Request Format
```json
{
  "game": "string",
  "matches": "number",
  "wins": "number",
  "blunders": "number",
  "endgame_losses": "number",
  "safe_moves": "number",
  "risky_moves": "number"
}
```

#### Response Format
```json
{
  "success": true,
  "game": "string",
  "ai_coach_feedback": "string",
  "stats_summary": {
    "total_matches": "number",
    "wins": "number",
    "losses": "number",
    "win_rate": "string"
  },
  "timestamp": "string"
}
```

#### Error Handling
```javascript
try {
  const response = await fetch(`${API_URL}/analyze`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  
  if (!response.ok) {
    throw new Error('API request failed');
  }
  
  const result = await response.json();
  // Handle success
} catch (error) {
  // Handle error
}
```

### Environment Configuration

#### Frontend (.env)
```bash
VITE_API_URL=http://localhost:5000
```

#### Backend (.env)
```bash
FLASK_APP=backend_enhanced.py
FLASK_ENV=development
DEBUG=True
PORT=5000
```

### Building for Production

```bash
# Frontend
npm run build
# Output: dist/

# Backend
pip install -r requirements.txt
gunicorn -w 4 backend_enhanced:app
```

## Advanced Features

### Real AI Integration

Replace mock coach with real AI (OpenAI example):

```python
import openai

def ai_game_coach(game: str, game_data: dict) -> str:
    prompt = f"""
    Analyze these {game} statistics and provide coaching:
    {json.dumps(game_data, indent=2)}
    
    Provide specific, actionable advice.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Expert game coach"},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content
```

### Analytics Tracking

Add Google Analytics or similar:

```typescript
// In App.tsx
useEffect(() => {
  // Track page view
  gtag('event', 'page_view', {
    page_path: window.location.pathname
  });
}, []);

// Track analyze event
const handleAnalyze = async (stats: GameStats) => {
  gtag('event', 'analyze_game', {
    game: selectedGame,
    matches: stats.matches
  });
  // ... rest of code
};
```

### Database Integration

Store user sessions:

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.String(50))
    matches = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    feedback = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

### User Authentication

Add user accounts:

```python
from flask_login import LoginManager, login_required

@app.route("/analyze", methods=["POST"])
@login_required
def analyze():
    # Only authenticated users can analyze
    pass
```

## Troubleshooting

### Common Issues

**Issue**: Frontend can't connect to backend
- **Solution**: Check VITE_API_URL in .env
- Verify backend is running on correct port
- Check CORS configuration

**Issue**: No feedback after submission
- **Solution**: Check browser console for errors
- Verify backend logs for errors
- Test API directly with curl

**Issue**: Build fails
- **Solution**: Delete node_modules and reinstall
- Clear dist folder
- Check Node.js version (need 16+)

## Best Practices

1. **Data Entry**
   - Be consistent with stat tracking
   - Update stats after each session
   - Keep notes on improvements

2. **Performance**
   - Track multiple games separately
   - Compare stats over time
   - Focus on one improvement area at a time

3. **Development**
   - Use TypeScript for type safety
   - Follow component structure
   - Write clean, documented code
   - Test before deploying

## Support & Resources

- **Documentation**: See README.md
- **Deployment**: See DEPLOYMENT.md
- **Backend Setup**: See BACKEND_SETUP.md
- **Testing**: See TESTING.md

## Feedback & Contributions

We welcome feedback and contributions! Please:
1. Open issues for bugs
2. Submit PRs for features
3. Share your use cases
4. Suggest improvements

---

Happy Gaming and Coaching! 🎮🚀
