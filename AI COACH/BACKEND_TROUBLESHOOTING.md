# Backend Troubleshooting Guide

Quick guide to fix backend issues.

## 🚨 Common Problems & Solutions

### Problem 1: "Cannot connect to backend" / CORS Error

**Symptoms:**
- Frontend shows error message
- Browser console shows "Failed to fetch" or CORS error
- Can't get AI feedback

**Solutions:**

1. **Check if backend is running:**
   ```bash
   # Open a new terminal and run:
   curl http://localhost:5000/
   
   # Should see: {"status":"running",...}
   ```

2. **If backend is NOT running:**
   ```bash
   # Start the simple backend (easiest):
   python backend_simple.py
   
   # OR start the enhanced backend:
   python backend_enhanced.py
   ```

3. **If you get "Module not found":**
   ```bash
   pip install Flask flask-cors
   # Then try running backend again
   ```

---

### Problem 2: "ModuleNotFoundError: No module named 'coach_agent'"

**Symptoms:**
- Backend crashes on startup
- Error mentions `coach_agent`

**Solution Option A (Easiest):**
```bash
# Use the simple backend instead (no coach_agent needed):
python backend_simple.py
```

**Solution Option B:**
```bash
# Copy the mock coach:
cp coach_agent_mock.py coach_agent.py
# Then run:
python backend_enhanced.py
```

---

### Problem 3: "Port 5000 already in use"

**Symptoms:**
- Error: "Address already in use"
- Can't start backend

**Solution:**

**Windows:**
```bash
# Find what's using port 5000:
netstat -ano | findstr :5000

# Kill it (replace PID with the number you see):
taskkill /PID <PID> /F

# Or use different port:
set PORT=5001
python backend_simple.py
```

**Mac/Linux:**
```bash
# Find and kill process:
lsof -ti:5000 | xargs kill -9

# Or use different port:
PORT=5001 python backend_simple.py
```

If using different port, update frontend `.env`:
```
VITE_API_URL=http://localhost:5001
```

---

### Problem 4: Backend starts but analyze doesn't work

**Test the backend directly:**

```bash
# Test health check:
curl http://localhost:5000/

# Test analyze:
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"game":"chess","matches":100,"wins":60}'

# Should get feedback back
```

If curl works but frontend doesn't:
1. Check `.env` has `VITE_API_URL=http://localhost:5000`
2. Restart frontend: Ctrl+C then `npm run dev`
3. Clear browser cache (Ctrl+Shift+R)

---

### Problem 5: Python not found

**Symptoms:**
- `python: command not found`

**Solutions:**

Try `python3` instead:
```bash
python3 backend_simple.py
```

Or install Python:
- Windows: https://www.python.org/downloads/
- Mac: `brew install python3`
- Linux: `sudo apt-get install python3`

---

## ✅ Quick Fix Checklist

Try these in order:

1. **[ ] Use the simple backend:**
   ```bash
   python backend_simple.py
   ```

2. **[ ] Install dependencies:**
   ```bash
   pip install Flask flask-cors
   ```

3. **[ ] Test with curl:**
   ```bash
   curl http://localhost:5000/
   ```

4. **[ ] Check frontend .env:**
   ```bash
   # Make sure .env contains:
   VITE_API_URL=http://localhost:5000
   ```

5. **[ ] Restart frontend:**
   ```bash
   # Press Ctrl+C to stop
   npm run dev
   ```

6. **[ ] Run test script:**
   ```bash
   pip install requests
   python test_backend_simple.py
   ```

---

## 🧪 Testing the Backend

### Step 1: Test if it's running
```bash
curl http://localhost:5000/
```

**Expected:**
```json
{"status":"running","message":"AI Game Coach Backend is Running 🚀"}
```

### Step 2: Test the analyze endpoint
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

**Expected:**
```json
{
  "success": true,
  "game": "chess",
  "ai_coach_feedback": "...feedback text...",
  "stats_summary": {...}
}
```

### Step 3: Run automated test
```bash
# Install requests if needed:
pip install requests

# Run test:
python test_backend_simple.py
```

---

## 🔍 Which Backend to Use?

### Use `backend_simple.py` if:
- ✅ You just want it to work quickly
- ✅ You're getting coach_agent errors
- ✅ You're new to Python/Flask
- ✅ You want minimal setup

### Use `backend_enhanced.py` if:
- ✅ You have coach_agent.py working
- ✅ You want full validation
- ✅ You need advanced features
- ✅ You're deploying to production

---

## 📝 Step-by-Step: Fresh Start

If nothing works, start fresh:

### 1. Clean Install
```bash
# Create new directory
mkdir backend-test
cd backend-test

# Copy simple backend
# (copy backend_simple.py to this folder)

# Install dependencies
pip install Flask flask-cors

# Run it
python backend_simple.py
```

### 2. Test It
```bash
# In another terminal:
curl http://localhost:5000/
```

### 3. Connect Frontend
```bash
# In your frontend folder, create .env:
echo "VITE_API_URL=http://localhost:5000" > .env

# Restart frontend:
npm run dev
```

### 4. Test in Browser
- Go to http://localhost:5173
- Select a game
- Enter stats
- Click "Get AI Coaching"
- Should work! ✅

---

## 🐛 Still Not Working?

### Check Browser Console
1. Open browser (Chrome recommended)
2. Press F12
3. Click "Console" tab
4. Look for red errors
5. Common errors:

   **"Failed to fetch"**
   - Backend not running → Start it
   
   **"CORS error"**
   - Backend not configured → Use backend_simple.py
   
   **"Network error"**
   - Wrong URL in .env → Check VITE_API_URL

### Check Backend Terminal
Look for:
- Import errors → Install dependencies
- Port errors → Use different port
- Syntax errors → Check Python version (need 3.8+)

### Check Python Version
```bash
python --version
# Need 3.8 or higher

# If too old:
python3 --version
# Try using python3 instead
```

---

## 💡 Pro Tips

1. **Always check both terminals:**
   - Frontend terminal (npm run dev)
   - Backend terminal (python backend_simple.py)

2. **Test backend independently first:**
   - Use curl or test_backend_simple.py
   - Make sure it works before connecting frontend

3. **Check the basics:**
   - Is backend running? (see terminal)
   - Is it on port 5000? (check terminal output)
   - Does .env match? (check VITE_API_URL)

4. **When in doubt:**
   - Stop everything (Ctrl+C)
   - Start backend first
   - Then start frontend
   - Test in browser

---

## 📞 Getting Help

Include this info when asking for help:

1. **What command did you run?**
   ```
   Example: python backend_simple.py
   ```

2. **What error do you see?**
   ```
   Copy the exact error message
   ```

3. **What does curl show?**
   ```bash
   curl http://localhost:5000/
   ```

4. **Python version:**
   ```bash
   python --version
   ```

5. **Is Flask installed?**
   ```bash
   pip list | grep Flask
   ```

---

## ✅ Success Checklist

Backend is working when:

- [ ] Terminal shows: "Running on http://0.0.0.0:5000"
- [ ] `curl http://localhost:5000/` returns JSON
- [ ] Test script passes all tests
- [ ] Frontend can get AI feedback
- [ ] No CORS errors in browser console

---

## 🎯 Most Common Fix

**90% of the time, this solves it:**

```bash
# 1. Use simple backend
python backend_simple.py

# 2. In another terminal, test it
curl http://localhost:5000/

# 3. If that works, make sure frontend .env has:
VITE_API_URL=http://localhost:5000

# 4. Restart frontend
npm run dev

# 5. Try again in browser
```

**Still stuck?** Run the test script:
```bash
pip install requests
python test_backend_simple.py
```

This will tell you exactly what's wrong! 🎯
