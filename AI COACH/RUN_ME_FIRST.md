# 🚨 GETTING "Failed to fetch" ERROR? DO THIS! 🚨

## ⚡ COPY AND PASTE THESE COMMANDS:

### Step 1: Check Your Setup
```bash
python check_setup.py
```

This will tell you exactly what's wrong!

---

### Step 2: Install Everything (If Needed)

```bash
# Install Python packages
pip install Flask flask-cors requests

# Install Node packages (if you haven't)
npm install
```

---

### Step 3: Start Backend

**Open Terminal 1** and run:

```bash
python backend_simple.py
```

You MUST see this:
```
🚀 AI Game Coach Backend (Simple Version)
📡 Running on http://localhost:5000
```

**KEEP THIS TERMINAL OPEN!** Don't close it!

---

### Step 4: Test Backend Works

**Open Terminal 2** (NEW terminal, don't close Terminal 1!) and run:

```bash
curl http://localhost:5000/
```

You should see:
```json
{"status":"running","message":"AI Game Coach Backend is Running 🚀","version":"Simple"}
```

✅ **See that?** Great! Backend is working. Continue to Step 5.
❌ **Don't see that?** Go back to Step 3 and make sure Terminal 1 is still running.

---

### Step 5: Start Frontend

**In Terminal 2**, run:

```bash
npm run dev
```

You should see:
```
Local: http://localhost:5173/
```

**KEEP THIS TERMINAL OPEN TOO!**

---

### Step 6: Use the App!

1. Open browser to: **http://localhost:5173**
2. Select a game (click on Chess)
3. Enter some stats:
   - Matches: 100
   - Wins: 60
   - Blunders: 10
4. Click "🎯 Get AI Coaching"
5. You should see feedback!

---

## 🔍 Troubleshooting Specific Errors

### Error: "python: command not found"
Try:
```bash
python3 backend_simple.py
```

### Error: "No module named 'flask'"
Run:
```bash
pip install Flask flask-cors
```
Then try Step 3 again.

### Error: "Address already in use"
Someone is using port 5000. Run:
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <number> /F

# Mac/Linux
lsof -ti:5000 | xargs kill -9
```

### Still getting "Failed to fetch"?

Check:
1. Both terminals are running (backend AND frontend)
2. Backend shows "Running on http://localhost:5000"
3. .env file exists (I created it for you!)
4. You restarted frontend after creating .env

---

## 📋 Quick Checklist

Before testing the app, make sure:

- [ ] Terminal 1 running: `python backend_simple.py`
- [ ] Terminal 1 shows: "Running on http://localhost:5000"
- [ ] Terminal 2 running: `npm run dev`
- [ ] Terminal 2 shows: "Local: http://localhost:5173"
- [ ] .env file exists (already created for you!)
- [ ] Browser at: http://localhost:5173

---

## 🆘 Emergency Fix

If NOTHING works, try this clean start:

```bash
# 1. Stop everything (Ctrl+C in both terminals)

# 2. Clean install
pip install Flask flask-cors requests
npm install

# 3. Terminal 1:
python backend_simple.py

# 4. Terminal 2 (wait for Terminal 1 to start):
npm run dev

# 5. Browser:
# Go to http://localhost:5173
```

---

## 💡 Common Mistakes

1. ❌ **Not starting the backend** → Start it!
2. ❌ **Closing the backend terminal** → Keep it open!
3. ❌ **Wrong URL in .env** → I created it correctly for you
4. ❌ **Not restarting frontend after creating .env** → Restart it!
5. ❌ **Using wrong Python command** → Try `python3` instead

---

## 🎯 Summary

You need **TWO terminals running at the same time**:

**Terminal 1:**
```bash
python backend_simple.py
# Shows: Running on http://localhost:5000
# KEEP RUNNING!
```

**Terminal 2:**
```bash
npm run dev
# Shows: Local: http://localhost:5173
# KEEP RUNNING!
```

**Then use the app in your browser!**

---

## ✅ It's Working When:

You can:
- Open http://localhost:5173
- Select a game
- Enter stats
- Click "Get AI Coaching"
- **See feedback** (not "Failed to fetch")

🎉 **That's it! You're done!**

---

**Still stuck? Run the diagnostic:**
```bash
python check_setup.py
```

**It will tell you exactly what's wrong!**
