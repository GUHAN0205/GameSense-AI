# Quick Fixes - Start Here! 🚨

## Backend Not Working? Try This First!

### ⚡ FASTEST FIX (Works 90% of the time)

**Step 1:** Open a terminal and run:
```bash
pip install Flask flask-cors
python backend_simple.py
```

**Step 2:** You should see:
```
🚀 AI Game Coach Backend (Simple Version)
📡 Running on http://localhost:5000
```

**Step 3:** Open a NEW terminal and test:
```bash
curl http://localhost:5000/
```

You should see: `{"status":"running"...}`

**Step 4:** If curl works, the backend is fine! Now check frontend `.env`:
```bash
# Make sure .env file contains:
VITE_API_URL=http://localhost:5000
```

**Step 5:** Restart frontend (press Ctrl+C then):
```bash
npm run dev
```

**Step 6:** Try the app at http://localhost:5173

✅ **Working? Great!** You're done!
❌ **Still not working?** Continue below...

---

## Common Errors & Instant Fixes

### Error: "ModuleNotFoundError: No module named 'flask'"

**Fix:**
```bash
pip install Flask flask-cors
```

---

### Error: "ModuleNotFoundError: No module named 'coach_agent'"

**Fix Option 1 (Easiest):**
```bash
# Use simple backend instead (no coach_agent needed)
python backend_simple.py
```

**Fix Option 2:**
```bash
# Copy the mock coach
cp coach_agent_mock.py coach_agent.py
python backend_enhanced.py
```

---

### Error: "Address already in use" or "Port 5000 is already in use"

**Fix (Windows):**
```bash
netstat -ano | findstr :5000
taskkill /PID <NUMBER_YOU_SEE> /F
python backend_simple.py
```

**Fix (Mac/Linux):**
```bash
lsof -ti:5000 | xargs kill -9
python backend_simple.py
```

**OR use a different port:**
```bash
PORT=5001 python backend_simple.py
# Then update .env: VITE_API_URL=http://localhost:5001
```

---

### Error: "python: command not found"

**Fix:**
```bash
# Try python3 instead:
python3 backend_simple.py

# OR install Python from:
# https://www.python.org/downloads/
```

---

### Frontend shows: "Cannot connect to backend" / CORS error

**Fix:**
```bash
# 1. Make sure backend is running (should see in terminal)
# 2. Check .env file has:
VITE_API_URL=http://localhost:5000

# 3. Restart frontend:
# Press Ctrl+C, then:
npm run dev

# 4. Hard refresh browser: Ctrl+Shift+R
```

---

### Backend starts but analyze doesn't work

**Test with this:**
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"game":"chess","matches":100,"wins":60}'
```

**If this works but frontend doesn't:**
1. Clear browser cache
2. Check browser console for errors (F12)
3. Make sure .env is correct
4. Restart frontend

---

## Files You Need

Make sure you have these files:

- ✅ `backend_simple.py` - Simple backend (USE THIS!)
- ✅ `requirements.txt` - Python dependencies
- ✅ `.env` - Frontend config (create if missing)
- ✅ `test_backend_simple.py` - Test script

Don't have them? You might be in the wrong folder!

---

## Complete Fresh Start

If nothing works, do this:

```bash
# 1. Make sure you're in the right folder
cd path/to/ai-game-coach

# 2. Install Python packages
pip install Flask flask-cors requests

# 3. Start simple backend
python backend_simple.py

# Leave that running, open NEW terminal:

# 4. Make sure .env exists
echo "VITE_API_URL=http://localhost:5000" > .env

# 5. Start frontend
npm run dev

# 6. Open browser to http://localhost:5173

# 7. Test it!
```

---

## Automated Test

Run this to diagnose problems:

```bash
pip install requests
python test_backend_simple.py
```

This will tell you EXACTLY what's wrong!

---

## Different Backends Explained

### backend_simple.py ⭐ RECOMMENDED
- ✅ Works immediately
- ✅ No extra files needed
- ✅ Built-in AI coach
- ✅ Perfect for testing
- ✅ Use this if you're having problems!

```bash
python backend_simple.py
```

### backend_enhanced.py
- ⚠️ Needs coach_agent.py
- ✅ More features
- ✅ Better validation
- ✅ Use for production

```bash
# Only use if you have coach_agent.py
python backend_enhanced.py
```

**When in doubt, use backend_simple.py!**

---

## Startup Scripts

### Windows:
```bash
start_backend.bat
```

### Mac/Linux:
```bash
chmod +x start_backend.sh
./start_backend.sh
```

These scripts do everything for you!

---

## Checklist: Is It Working?

- [ ] Backend terminal shows: "Running on http://localhost:5000"
- [ ] `curl http://localhost:5000/` returns JSON
- [ ] .env file exists with correct URL
- [ ] Frontend terminal shows: "Local: http://localhost:5173"
- [ ] Browser opens to app
- [ ] Can select a game
- [ ] Can enter stats
- [ ] Can click "Get AI Coaching"
- [ ] Gets feedback (not error)

✅ All checked? You're good!
❌ Any unchecked? That's your problem!

---

## Still Stuck?

### Option 1: Run the test
```bash
python test_backend_simple.py
```

### Option 2: Check the logs
Look at both terminal windows:
- Backend terminal: Shows Python errors
- Frontend terminal: Shows npm/build errors
- Browser console (F12): Shows JavaScript errors

### Option 3: Step by step verification

**Terminal 1 (Backend):**
```bash
python backend_simple.py
# Should say "Running on http://localhost:5000"
# Leave this running!
```

**Terminal 2 (Test):**
```bash
curl http://localhost:5000/
# Should show: {"status":"running"...}
```

**Terminal 3 (Frontend):**
```bash
cat .env
# Should show: VITE_API_URL=http://localhost:5000

npm run dev
# Should say "Local: http://localhost:5173"
```

**Browser:**
- Go to http://localhost:5173
- Press F12 for console
- Check for red errors
- Try using the app

---

## Contact Points

1. Check [BACKEND_TROUBLESHOOTING.md](BACKEND_TROUBLESHOOTING.md) for detailed help
2. Check [GETTING_STARTED.md](GETTING_STARTED.md) for setup guide
3. Check [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for commands

---

## Summary: What to Do Right Now

```bash
# Copy and paste this entire block:

# Install Python packages
pip install Flask flask-cors requests

# Start backend (keep running)
python backend_simple.py

# In NEW terminal, create .env
echo "VITE_API_URL=http://localhost:5000" > .env

# Start frontend
npm run dev

# Test in browser: http://localhost:5173
```

**This should work!** If it doesn't, run:
```bash
python test_backend_simple.py
```

And it will tell you exactly what's wrong! 🎯
