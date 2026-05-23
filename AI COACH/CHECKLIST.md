# ✅ Backend Startup Checklist

Use this to verify everything is set up correctly.

## Before You Start

- [ ] I have Python installed (`python --version` works)
- [ ] I have Node.js installed (`node --version` works)
- [ ] I'm in the ai-game-coach project folder

## Option 1: Automatic Start (Easiest!)

**Windows:**
- [ ] I double-clicked `fix_backend.bat`
- [ ] A window opened showing "Running on http://localhost:5000"
- [ ] I kept that window open

**Mac/Linux:**
- [ ] I ran `chmod +x fix_backend.sh`
- [ ] I ran `./fix_backend.sh`
- [ ] Terminal shows "Running on http://localhost:5000"
- [ ] I kept that terminal open

## Option 2: Manual Start

### Terminal 1 (Backend)
- [ ] Opened a NEW terminal
- [ ] Navigated to project folder (`cd /path/to/ai-game-coach`)
- [ ] Ran `pip install Flask flask-cors`
- [ ] Ran `python backend_simple.py`
- [ ] See: "Running on http://localhost:5000"
- [ ] Kept terminal open!

### Terminal 2 (Frontend - should already be running)
- [ ] Terminal shows `npm run dev`
- [ ] See: "Local: http://localhost:5173"
- [ ] Kept terminal open!

## Verify Backend is Running

Open a **third** terminal and test:

```bash
curl http://localhost:5000/
```

- [ ] Got JSON response with "status":"running"

**OR** open browser to http://localhost:5000/ :

- [ ] See JSON with "AI Game Coach Backend is Running"

## Verify Frontend Can Connect

- [ ] `.env` file exists in project root
- [ ] `.env` contains: `VITE_API_URL=http://localhost:5000`
- [ ] Restarted frontend after creating .env (if you just created it)

## Test the Full App

1. Browser Actions:
   - [ ] Opened http://localhost:5173
   - [ ] Page loads successfully
   - [ ] See "AI Game Coach" header
   - [ ] See game selection cards

2. Select Game:
   - [ ] Clicked on Chess (or any game)
   - [ ] Stats form appeared
   - [ ] Can enter numbers in fields

3. Enter Stats:
   - [ ] Entered Matches: 100
   - [ ] Entered Wins: 60
   - [ ] Entered Blunders: 10
   - [ ] Win rate shows 60%

4. Get Feedback:
   - [ ] Clicked "🎯 Get AI Coaching"
   - [ ] Loading spinner appeared
   - [ ] **Feedback appeared** (NOT "Failed to fetch")
   - [ ] Can read AI coaching advice

## ✅ SUCCESS!

If all boxes are checked, especially the last one (feedback appeared), you're all set! 🎉

## ❌ If Feedback Didn't Appear

Check which step failed:

### "Failed to fetch" error?
→ Backend not running or wrong URL
→ Go back to "Terminal 1 (Backend)" section
→ Make sure it's actually running

### "CORS error" in console?
→ Backend might be using wrong CORS config
→ Make sure you're using `backend_simple.py`

### Different error?
→ Open browser console (F12)
→ Check the Console tab for error details
→ Check backend terminal for Python errors

## Quick Debug Commands

```bash
# Check if backend is running
curl http://localhost:5000/

# Check if frontend is running
curl http://localhost:5173/

# Check .env file
cat .env        # Mac/Linux
type .env       # Windows

# List running processes
lsof -i :5000   # Mac/Linux - backend port
lsof -i :5173   # Mac/Linux - frontend port
```

## What Working Looks Like

### Terminal 1 (Backend):
```
🚀 AI Game Coach Backend (Simple Version)
📡 Running on http://localhost:5000
==================================================

 * Serving Flask app 'backend_simple'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

### Terminal 2 (Frontend):
```
VITE v7.3.2  ready in 500 ms

➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
```

### Browser at http://localhost:5000/ :
```json
{
  "status": "running",
  "message": "AI Game Coach Backend is Running 🚀",
  "version": "Simple"
}
```

### Browser at http://localhost:5173 (The App):
- Beautiful gradient design
- Game cards visible
- Can click and interact
- Gets AI feedback successfully

## Still Having Issues?

1. **Run the diagnostic:**
   ```bash
   python check_setup.py
   ```

2. **Read these in order:**
   - [INSTANT_FIX.md](INSTANT_FIX.md)
   - [RUN_ME_FIRST.md](RUN_ME_FIRST.md)
   - [VISUAL_GUIDE.md](VISUAL_GUIDE.md)

3. **Check both terminals are running:**
   - Terminal 1: Backend
   - Terminal 2: Frontend
   - Both must be open!

## Common Mistakes

1. ❌ Starting backend then closing the terminal
   → ✅ Keep it open!

2. ❌ Not creating .env file
   → ✅ Create it with: `VITE_API_URL=http://localhost:5000`

3. ❌ Not restarting frontend after creating .env
   → ✅ Press Ctrl+C, then `npm run dev`

4. ❌ Using the wrong port in .env
   → ✅ Use exactly: `http://localhost:5000`

5. ❌ Trying to use the app with only frontend running
   → ✅ Need BOTH backend AND frontend running!

---

**Print this checklist and use it every time you start the app!** 📋
