# AI Game Coach - Architecture

Visual guide to understand how everything connects.

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         USER                                │
│                      (Web Browser)                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ Opens http://localhost:5173
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   FRONTEND (React)                          │
│                   Port: 5173                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Components:                                        │   │
│  │  • Header                                           │   │
│  │  • GameSelector ────────┐                           │   │
│  │  • StatsForm            │ User selects game         │   │
│  │  • FeedbackDisplay      │ and enters stats          │   │
│  │  • GameTips             │                           │   │
│  │  • Footer               │                           │   │
│  └─────────────────────────┼───────────────────────────┘   │
│                            │                               │
│                            │ Clicks "Get AI Coaching"      │
│                            ▼                               │
│                   POST /analyze                             │
│                   {game, stats}                             │
└────────────────────────────┬────────────────────────────────┘
                             │
                             │ HTTP Request (CORS enabled)
                             │ VITE_API_URL=http://localhost:5000
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                   BACKEND (Flask)                           │
│                   Port: 5000                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Endpoints:                                         │   │
│  │  • GET  /        → Health check                     │   │
│  │  • GET  /health  → Detailed health                  │   │
│  │  • POST /analyze → Main analysis                    │   │
│  └─────────────────────────┬───────────────────────────┘   │
│                            │                               │
│                            │ Validates input               │
│                            │ Calculates win rate           │
│                            ▼                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │         AI Coach Logic                              │   │
│  │  • Analyzes stats                                   │   │
│  │  • Generates feedback                               │   │
│  │  • Returns personalized advice                      │   │
│  └─────────────────────────┬───────────────────────────┘   │
│                            │                               │
└────────────────────────────┼────────────────────────────────┘
                             │
                             │ Returns JSON response
                             │ {feedback, stats_summary}
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                   FRONTEND (React)                          │
│  • Receives feedback                                        │
│  • Displays in FeedbackDisplay component                    │
│  • Shows stats summary                                      │
│  • User reads coaching advice                               │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow

```
User Action                Frontend                Backend
─────────────────────────────────────────────────────────────

1. Select Game
   ├─ Chess ───────▶ selectedGame: "chess"
   └─ Display tips


2. Enter Stats
   ├─ Matches: 100 ─▶ GameStats object
   ├─ Wins: 60       │ {
   ├─ Blunders: 15   │   matches: 100,
   └─ etc...         │   wins: 60,
                     │   ...
                     └─ }


3. Click Button ────▶ handleAnalyze()
                     │
                     └─▶ POST /analyze ───────▶ @app.route("/analyze")
                         {                      │
                           game: "chess",       ├─ Validate input
                           matches: 100,        ├─ Calculate stats
                           wins: 60,            │
                           ...                  └─▶ ai_game_coach()
                         }                          │
                                                    ├─ Analyze game
                                                    ├─ Generate feedback
                                                    └─▶ Return JSON


4. Receive Response ◀─ {                       ◀─────────────────
                         success: true,
                         game: "chess",
                         ai_coach_feedback: "...",
                         stats_summary: {...}
                       }


5. Display Feedback
   └─▶ FeedbackDisplay
       ├─ Show AI advice
       └─ Show stats
```

## File Structure & Purpose

```
ai-game-coach/
│
├── FRONTEND FILES
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.tsx          → Top navigation
│   │   │   ├── Footer.tsx          → Bottom info
│   │   │   ├── GameSelector.tsx    → 6 game cards
│   │   │   ├── StatsForm.tsx       → Input form + validation
│   │   │   ├── FeedbackDisplay.tsx → AI feedback display
│   │   │   ├── GameTips.tsx        → Quick tips
│   │   │   └── QuickStats.tsx      → Stats cards
│   │   │
│   │   ├── App.tsx                 → Main component
│   │   │                              • State management
│   │   │                              • API calls
│   │   │                              • Component composition
│   │   │
│   │   ├── main.tsx                → Entry point
│   │   ├── index.css               → Global styles
│   │   └── vite-env.d.ts           → TypeScript types
│   │
│   ├── index.html                  → HTML template
│   ├── .env                        → Config (VITE_API_URL)
│   └── package.json                → Dependencies
│
├── BACKEND FILES
│   ├── backend_simple.py           → Simple backend ⭐ USE THIS
│   │                                  • Built-in AI
│   │                                  • No dependencies
│   │                                  • Ready to use
│   │
│   ├── backend_enhanced.py         → Full-featured backend
│   │                                  • Needs coach_agent.py
│   │                                  • More validation
│   │                                  • Production ready
│   │
│   ├── coach_agent_mock.py         → Mock AI coach
│   │                                  • Game-specific feedback
│   │                                  • Copy to coach_agent.py
│   │
│   └── requirements.txt            → Python dependencies
│
├── TESTING & DEPLOYMENT
│   ├── test_backend_simple.py      → Automated tests
│   ├── start_backend.sh            → Linux/Mac startup
│   └── start_backend.bat           → Windows startup
│
└── DOCUMENTATION (You are here!)
    ├── FIXES.md                    → Quick fixes ⭐ START HERE
    ├── GETTING_STARTED.md          → Setup guide
    ├── BACKEND_TROUBLESHOOTING.md  → Backend help
    ├── QUICK_REFERENCE.md          → Commands
    └── ... more guides
```

## Request/Response Example

### Request Flow

```
Browser                                    Flask
───────                                    ─────

POST /analyze
Content-Type: application/json

{
  "game": "chess",
  "matches": 100,
  "wins": 60,
  "blunders": 15,
  "endgame_losses": 10,
  "safe_moves": 200,
  "risky_moves": 50
}
                    ──────────────────▶
                                           1. Extract data
                                           2. Validate:
                                              ✓ matches > 0
                                              ✓ wins ≤ matches
                                              ✓ no negatives
                                           3. Calculate:
                                              win_rate = 60%
                                           4. Call AI coach
                                           5. Generate feedback
                    ◀──────────────────
HTTP 200 OK
Content-Type: application/json

{
  "success": true,
  "game": "chess",
  "ai_coach_feedback": "🎯 CHESS Performance...",
  "stats_summary": {
    "total_matches": 100,
    "wins": 60,
    "losses": 40,
    "win_rate": "60.0%"
  },
  "timestamp": "2024-01-01T12:00:00"
}
```

## Environment Configuration

```
┌──────────────────┐         ┌──────────────────┐
│   Frontend       │         │   Backend        │
│   (.env file)    │         │   (server)       │
├──────────────────┤         ├──────────────────┤
│                  │         │                  │
│ VITE_API_URL=    │────────▶│ Running on:      │
│ http://localhost │   Must  │ http://0.0.0.0   │
│      :5000       │  Match! │      :5000       │
│                  │         │                  │
└──────────────────┘         └──────────────────┘
```

## Backend Options Comparison

```
┌──────────────────────────────────────────────────────────┐
│                  backend_simple.py                       │
├──────────────────────────────────────────────────────────┤
│ ✅ Works immediately (no setup)                          │
│ ✅ Built-in AI coach                                     │
│ ✅ No extra files needed                                 │
│ ✅ Perfect for testing                                   │
│ ⭐ RECOMMENDED FOR BEGINNERS                             │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│                backend_enhanced.py                       │
├──────────────────────────────────────────────────────────┤
│ ⚠️  Requires coach_agent.py                              │
│ ✅ Advanced validation                                   │
│ ✅ Better error handling                                 │
│ ✅ Logging & monitoring                                  │
│ ⭐ RECOMMENDED FOR PRODUCTION                            │
└──────────────────────────────────────────────────────────┘
```

## Startup Sequence

```
┌─────────────────────────────────────────────┐
│ Step 1: Install Dependencies                │
├─────────────────────────────────────────────┤
│ Frontend: npm install                       │
│ Backend:  pip install -r requirements.txt   │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ Step 2: Configure Environment               │
├─────────────────────────────────────────────┤
│ Create .env file with:                      │
│ VITE_API_URL=http://localhost:5000          │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ Step 3: Start Backend (Terminal 1)          │
├─────────────────────────────────────────────┤
│ python backend_simple.py                    │
│ → Running on http://localhost:5000          │
│ → Keep this terminal open!                  │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ Step 4: Start Frontend (Terminal 2)         │
├─────────────────────────────────────────────┤
│ npm run dev                                 │
│ → Local: http://localhost:5173              │
│ → Keep this terminal open!                  │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ Step 5: Use the App                         │
├─────────────────────────────────────────────┤
│ 1. Open browser to http://localhost:5173    │
│ 2. Select a game                            │
│ 3. Enter stats                              │
│ 4. Click "Get AI Coaching"                  │
│ 5. Read feedback!                           │
└─────────────────────────────────────────────┘
```

## Technology Stack

```
┌─────────────────────────────────────────────┐
│              FRONTEND                       │
├─────────────────────────────────────────────┤
│ • React 18      → UI library                │
│ • TypeScript    → Type safety               │
│ • Vite          → Build tool                │
│ • Tailwind CSS  → Styling                   │
│ • Fetch API     → HTTP requests             │
└─────────────────────────────────────────────┘
                    ↕
┌─────────────────────────────────────────────┐
│              BACKEND                        │
├─────────────────────────────────────────────┤
│ • Flask         → Web framework             │
│ • Flask-CORS    → Cross-origin              │
│ • Python 3.8+   → Language                  │
│ • JSON          → Data format               │
└─────────────────────────────────────────────┘
```

## Port Usage

```
Port 5173  → Frontend (Vite dev server)
Port 5000  → Backend (Flask server)

Make sure both ports are free!
```

## Need Help?

```
Problem?              Read This:
──────────────────────────────────────
Backend not working   → FIXES.md ⭐
First time setup      → GETTING_STARTED.md
Quick commands        → QUICK_REFERENCE.md
Backend details       → BACKEND_TROUBLESHOOTING.md
```

---

**Visual learner?** This diagram shows everything!
**Prefer text?** Check the other documentation files!
