# 🚨 INSTANT FIX - DO THIS NOW!

## The Problem
Your frontend is running, but the backend is NOT running.
That's why you get "Failed to fetch"

## The Solution (3 Steps)

### STEP 1: Open a NEW Terminal Window

**Don't close your existing terminal!** Open a completely NEW one.

- **Windows:** Click Start → Type "cmd" → Press Enter
- **Mac:** Press Cmd+Space → Type "terminal" → Press Enter
- **VS Code:** Click Terminal menu → New Terminal

### STEP 2: Navigate to Your Project Folder

Type this (replace with YOUR project path):

```bash
cd path/to/your/ai-game-coach
```

For example:
```bash
cd C:\Users\YourName\Desktop\ai-game-coach
# or
cd ~/Desktop/ai-game-coach
```

### STEP 3: Run These Two Commands

Copy and paste these ONE AT A TIME:

```bash
pip install Flask flask-cors
```

Press ENTER, wait for it to finish, then:

```bash
python backend_simple.py
```

Press ENTER.

---

## What You Should See

If it works, you'll see this:

```
==================================================
🚀 AI Game Coach Backend (Simple Version)
📡 Running on http://localhost:5000
==================================================
```

**✅ SEE THAT? GREAT! Leave this terminal open!**

Now go back to your browser and try the app again!

---

## ❌ If You See Errors

### Error: "python: command not found"
Try this instead:
```bash
python3 backend_simple.py
```

### Error: "No module named 'flask'"
Run this first:
```bash
pip install Flask flask-cors
```
Then try `python backend_simple.py` again

### Error: "cannot find backend_simple.py"
You're in the wrong folder! 

Type:
```bash
ls          # Mac/Linux
dir         # Windows
```

You should see `backend_simple.py` in the list.
If not, use `cd` to navigate to the correct folder.

---

## 🧪 Test If Backend is Running

Open ANOTHER new terminal and type:

```bash
curl http://localhost:5000/
```

**Windows users:** If curl doesn't work, open your browser and go to:
```
http://localhost:5000/
```

You should see:
```json
{"status":"running","message":"AI Game Coach Backend is Running 🚀","version":"Simple"}
```

✅ **See that?** Backend is working! Try your app again!

---

## ✅ Final Check

Before using the app:

1. **Terminal 1** (the one you had before):
   - Running `npm run dev`
   - Shows "Local: http://localhost:5173"

2. **Terminal 2** (the new one you just opened):
   - Running `python backend_simple.py`
   - Shows "Running on http://localhost:5000"

3. **Browser**:
   - Go to http://localhost:5173
   - Try to get AI feedback
   - Should work now!

---

## 🎯 Summary

You need **BOTH** terminals running:

```
Terminal 1: npm run dev          ← You already have this
Terminal 2: python backend_simple.py  ← You need to start this!
```

**That's it!** 🚀
