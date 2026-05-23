# Getting Started with AI Game Coach

Welcome! This guide will help you get the AI Game Coach application running in just a few minutes.

## What You're Building

A beautiful web app that provides AI-powered coaching for games like Chess, Pool, Uno, and more!

**What it looks like:**
- Modern, gradient-based design
- Game selector with 6 games
- Stats input form
- Real-time win rate calculation
- AI feedback display
- Game-specific tips

## Prerequisites

Before you start, make sure you have:

- ✅ **Node.js 16+** ([Download](https://nodejs.org/))
- ✅ **Python 3.8+** ([Download](https://www.python.org/))
- ✅ **Code Editor** (VS Code recommended)
- ✅ **Terminal/Command Line** access
- ✅ **Basic command line knowledge**

### Check Your Installation

```bash
# Check Node.js
node --version    # Should be 16.x or higher

# Check npm
npm --version     # Should be 7.x or higher

# Check Python
python --version  # Should be 3.8 or higher (or python3)

# Check pip
pip --version     # Should be installed with Python
```

## Step 1: Get the Code

### Option A: If you have the files
```bash
cd path/to/ai-game-coach
```

### Option B: Clone from repository
```bash
git clone <your-repo-url>
cd ai-game-coach
```

## Step 2: Setup Frontend

### Install Dependencies
```bash
npm install
```

This will install:
- React 18
- TypeScript
- Vite
- Tailwind CSS
- All necessary dependencies

**Expected output:**
```
added 234 packages in 15s
```

### Configure Environment

Create a `.env` file in the root directory:

```bash
# Copy the example file
cp .env.example .env

# Or create manually with:
echo "VITE_API_URL=http://localhost:5000" > .env
```

### Test the Frontend

```bash
npm run dev
```

**Expected output:**
```
  VITE v7.3.2  ready in 500 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

Open http://localhost:5173 in your browser. You should see the app, but the backend won't work yet!

**Keep this terminal running** and open a new terminal for the next step.

## Step 3: Setup Backend

### Option A: Using the Mock Coach (Recommended for Testing)

1. **Rename the mock file:**
```bash
# Windows
copy coach_agent_mock.py coach_agent.py

# macOS/Linux
cp coach_agent_mock.py coach_agent.py
```

2. **Install Python dependencies:**
```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install packages
pip install Flask==2.3.0 flask-cors==4.0.0
```

3. **Run the backend:**
```bash
python backend_enhanced.py
```

**Expected output:**
```
==================================================
🚀 AI Game Coach Backend Starting...
📡 Port: 5000
🔧 Debug Mode: True
==================================================
 * Running on http://0.0.0.0:5000
```

### Option B: Using Your Own AI Coach

If you already have `coach_agent.py` with your AI implementation:

```bash
# Just install dependencies and run
pip install Flask==2.3.0 flask-cors==4.0.0
python backend_enhanced.py
```

## Step 4: Test the Full Application

Now with both frontend and backend running:

1. **Open Frontend**: http://localhost:5173
2. **Select a Game**: Click on Chess (♟️)
3. **Enter Stats**:
   - Total Matches: 100
   - Wins: 60
   - Blunders: 15
   - Endgame Losses: 10
   - Safe Moves: 200
   - Risky Moves: 50
4. **Click**: "🎯 Get AI Coaching"
5. **See Feedback**: AI analysis appears!

### What You Should See

✅ **Game Selection**: Colorful game cards  
✅ **Stats Form**: Input fields with validation  
✅ **Win Rate**: Calculated automatically (60% in example)  
✅ **Loading**: Spinner while processing  
✅ **Feedback**: AI coaching advice  
✅ **Tips**: Game-specific quick tips  

## Step 5: Explore the Features

### Try Different Games
- Click on different game cards
- Notice the tips change for each game
- Enter stats and get game-specific feedback

### Test Error Handling
- Try submitting without entering matches (button disabled)
- Stop the backend and submit (error message appears)
- Enter invalid data like wins > matches (backend rejects it)

### Check Responsive Design
- Resize browser window
- Test on mobile device
- Everything should adapt beautifully

## Common First-Time Issues

### Issue: "Port 5173 already in use"
**Solution:**
```bash
# Kill the process or use different port
npm run dev -- --port 3000
```

### Issue: "Port 5000 already in use"
**Solution:**
```bash
# On Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# On macOS/Linux
lsof -i :5000
kill -9 <PID>

# Or use different port
PORT=5001 python backend_enhanced.py
```

### Issue: "Cannot find module 'Flask'"
**Solution:**
```bash
# Make sure virtual environment is activated
pip install Flask flask-cors
```

### Issue: "CORS error" in browser
**Solution:**
- Make sure backend is running
- Check `.env` has correct `VITE_API_URL`
- Restart frontend: Ctrl+C and `npm run dev`

### Issue: Frontend shows but backend doesn't respond
**Solution:**
- Check backend terminal for errors
- Test backend directly: `curl http://localhost:5000/`
- Verify CORS is enabled in `backend_enhanced.py`

### Issue: "Module not found" errors in frontend
**Solution:**
```bash
# Delete and reinstall
rm -rf node_modules
npm install
```

## Understanding the Project Structure

```
ai-game-coach/
│
├── 🎨 Frontend Files
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── App.tsx         # Main app
│   │   └── main.tsx        # Entry point
│   ├── index.html          # HTML template
│   └── .env                # Environment config
│
├── 🐍 Backend Files
│   ├── backend_enhanced.py      # Flask server
│   └── coach_agent_mock.py      # AI coach
│
└── 📚 Documentation
    ├── README.md
    ├── GETTING_STARTED.md  # This file
    ├── DEPLOYMENT.md
    └── ... more guides
```

## Next Steps

### Immediate (Learn the Basics)
1. ✅ Read [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for command cheat sheet
2. ✅ Try all 6 games
3. ✅ Experiment with different stats
4. ✅ Customize a game tip or color

### Short Term (Customize)
1. ⬜ Add a new game
2. ⬜ Change the color scheme
3. ⬜ Modify the AI feedback
4. ⬜ Add your own stats fields

### Long Term (Production)
1. ⬜ Integrate real AI (OpenAI, Claude)
2. ⬜ Deploy to production (see [DEPLOYMENT.md](DEPLOYMENT.md))
3. ⬜ Add user authentication
4. ⬜ Implement database for history
5. ⬜ Add analytics

## Learning Resources

### Understanding the Code

**Frontend (React + TypeScript):**
- `src/App.tsx` - Main component with state management
- `src/components/GameSelector.tsx` - Game selection UI
- `src/components/StatsForm.tsx` - Form with validation
- `src/components/FeedbackDisplay.tsx` - AI feedback display

**Backend (Flask + Python):**
- `backend_enhanced.py` - API endpoints and validation
- `coach_agent_mock.py` - Game-specific feedback logic

### Documentation Order

1. **First**: This file (GETTING_STARTED.md)
2. **Second**: [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
3. **Third**: [README.md](README.md)
4. **Fourth**: [USAGE_GUIDE.md](USAGE_GUIDE.md)
5. **When ready to deploy**: [DEPLOYMENT.md](DEPLOYMENT.md)

## Development Workflow

### Daily Development

**Terminal 1 (Frontend):**
```bash
npm run dev
# Keep running, auto-reloads on changes
```

**Terminal 2 (Backend):**
```bash
python backend_enhanced.py
# Restart when you change backend code
```

**Terminal 3 (Commands):**
```bash
# Use for git, testing, etc.
```

### Making Changes

1. **Edit code** in your editor
2. **Frontend changes** auto-reload (hot module replacement)
3. **Backend changes** require restart (Ctrl+C, then run again)
4. **Test** in browser
5. **Commit** when satisfied

### Before Deploying

```bash
# Test production build
npm run build
# Should succeed without errors

# Check for TypeScript errors
npm run build
# Should have no type errors
```

## Getting Help

### In Order of Preference:

1. **Check this guide** - Common issues above
2. **Check documentation** - [README.md](README.md), other guides
3. **Check browser console** - F12 → Console tab
4. **Check backend logs** - Terminal running backend
5. **Test API directly** - Use curl or Postman
6. **Read error messages** - They usually tell you what's wrong!

### Useful Commands for Debugging

```bash
# Check if backend is running
curl http://localhost:5000/

# Check if frontend can reach backend
curl http://localhost:5000/health

# Test analyze endpoint
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"game":"chess","matches":100,"wins":60}'

# Check Node/npm versions
node --version && npm --version

# Check Python/pip versions
python --version && pip --version
```

## Success Checklist

After following this guide, you should have:

- ✅ Frontend running on http://localhost:5173
- ✅ Backend running on http://localhost:5000
- ✅ Can select games
- ✅ Can enter stats
- ✅ Can get AI feedback
- ✅ See game tips
- ✅ No console errors
- ✅ Responsive design works
- ✅ Can build without errors (`npm run build`)

## Congratulations! 🎉

You now have a fully functional AI Game Coach application running locally!

### What you learned:
- How to setup a React + TypeScript frontend
- How to run a Flask backend
- How to connect frontend and backend
- How to test the full application
- How to debug common issues

### What's next:
- Customize the app to your needs
- Add your own AI implementation
- Deploy to production
- Share with users!

---

**Need more help?** Check:
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Commands cheat sheet
- [USAGE_GUIDE.md](USAGE_GUIDE.md) - Detailed usage
- [DEPLOYMENT.md](DEPLOYMENT.md) - Deployment guides
- [TESTING.md](TESTING.md) - Testing strategies

**Happy Coaching! 🎮🚀**
