# Visual Step-by-Step Guide

## 🎯 What You Need: 2 Terminals Running At Once!

```
┌─────────────────────────────────────┐
│        YOUR COMPUTER                │
├─────────────────────────────────────┤
│                                     │
│  ┌──────────────────────────────┐  │
│  │   TERMINAL 1 (Backend)       │  │
│  ├──────────────────────────────┤  │
│  │ $ python backend_simple.py   │  │
│  │                              │  │
│  │ Running on                   │  │
│  │ http://localhost:5000        │  │
│  │                              │  │
│  │ ⚠️ KEEP THIS RUNNING!        │  │
│  └──────────────────────────────┘  │
│                                     │
│  ┌──────────────────────────────┐  │
│  │   TERMINAL 2 (Frontend)      │  │
│  ├──────────────────────────────┤  │
│  │ $ npm run dev                │  │
│  │                              │  │
│  │ Local:                       │  │
│  │ http://localhost:5173        │  │
│  │                              │  │
│  │ ⚠️ KEEP THIS RUNNING!        │  │
│  └──────────────────────────────┘  │
│                                     │
│  ┌──────────────────────────────┐  │
│  │   BROWSER                    │  │
│  ├──────────────────────────────┤  │
│  │ http://localhost:5173        │  │
│  │                              │  │
│  │ ┌──────────────────────────┐ │  │
│  │ │  AI Game Coach App      │ │  │
│  │ │  Select game → Enter    │ │  │
│  │ │  stats → Get feedback!  │ │  │
│  │ └──────────────────────────┘ │  │
│  └──────────────────────────────┘  │
└─────────────────────────────────────┘
```

---

## 📝 Step-by-Step Visual

### STEP 1: Open Terminal 1

```
┌─────────────────────────────────┐
│  Terminal 1                     │
├─────────────────────────────────┤
│  $                              │ ← You are here
│                                 │
│                                 │
│                                 │
└─────────────────────────────────┘
```

Type:
```bash
python backend_simple.py
```

Press ENTER

---

### STEP 2: Backend Starts

```
┌─────────────────────────────────┐
│  Terminal 1                     │
├─────────────────────────────────┤
│  $ python backend_simple.py     │
│                                 │
│  ================================│
│  🚀 AI Game Coach Backend       │
│  📡 Running on                  │
│     http://localhost:5000       │
│  ================================│
│                                 │
│  ✅ SUCCESS!                    │
│  ⚠️ DON'T CLOSE THIS!          │
└─────────────────────────────────┘
```

**Leave this running!** Minimize it or move to the side.

---

### STEP 3: Open Terminal 2 (NEW)

```
┌─────────────────────────────────┐
│  Terminal 1 (minimized)         │  ← Still running!
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  Terminal 2 (NEW)               │
├─────────────────────────────────┤
│  $                              │ ← You are here
│                                 │
│                                 │
└─────────────────────────────────┘
```

Type:
```bash
npm run dev
```

Press ENTER

---

### STEP 4: Frontend Starts

```
┌─────────────────────────────────┐
│  Terminal 1 (minimized)         │  ← Still running!
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  Terminal 2                     │
├─────────────────────────────────┤
│  $ npm run dev                  │
│                                 │
│  VITE v7.3.2  ready in 500 ms   │
│                                 │
│  ➜  Local:                      │
│     http://localhost:5173/      │
│                                 │
│  ✅ SUCCESS!                    │
│  ⚠️ DON'T CLOSE THIS!          │
└─────────────────────────────────┘
```

**Leave this running too!**

---

### STEP 5: Open Browser

```
┌─────────────────────────────────┐
│  Browser                        │
├─────────────────────────────────┤
│  http://localhost:5173          │ ← Type this
├─────────────────────────────────┤
│                                 │
│  Loading...                     │
│                                 │
└─────────────────────────────────┘
```

---

### STEP 6: App Loads!

```
┌───────────────────────────────────────────────┐
│  AI Game Coach         http://localhost:5173  │
├───────────────────────────────────────────────┤
│                                               │
│         Level Up Your Game                    │
│                                               │
│  ┌──────┐ ┌──────┐ ┌──────┐                  │
│  │ ♟️    │ │ 🎱   │ │ 🃏   │                  │
│  │Chess │ │ Pool │ │ Uno  │  ← Click one!    │
│  └──────┘ └──────┘ └──────┘                  │
│                                               │
│  ✅ If you see this, it's working!            │
└───────────────────────────────────────────────┘
```

---

### STEP 7: Select Chess

```
┌───────────────────────────────────────────────┐
│  AI Game Coach                                │
├───────────────────────────────────────────────┤
│                                               │
│  ┌──────┐ ┌──────┐ ┌──────┐                  │
│  │ ♟️    │ │ 🎱   │ │ 🃏   │                  │
│  │Chess │ │ Pool │ │ Uno  │                  │
│  └──────┘ └──────┘ └──────┘                  │
│    ↑ Selected!                                │
│                                               │
│  Enter Your Stats                             │
│  ┌─────────────────────┐                     │
│  │ Total Matches: 100  │ ← Fill these in     │
│  │ Wins: 60            │                     │
│  │ Blunders: 10        │                     │
│  └─────────────────────┘                     │
│                                               │
│  [🎯 Get AI Coaching]  ← Click this!         │
└───────────────────────────────────────────────┘
```

---

### STEP 8: Get Feedback!

```
┌───────────────────────────────────────────────┐
│  AI Game Coach                                │
├───────────────────────────────────────────────┤
│                                               │
│  🤖 AI Coach Feedback                         │
│  ┌─────────────────────────────────────────┐ │
│  │ 🎯 CHESS Performance Analysis          │ │
│  │                                         │ │
│  │ You've played 100 matches with 60      │ │
│  │ wins (60% win rate).                   │ │
│  │                                         │ │
│  │ 🌟 Good work! You're maintaining a     │ │
│  │ positive record.                       │ │
│  │                                         │ │
│  │ 💡 Keep practicing regularly to        │ │
│  │ improve your skills!                   │ │
│  └─────────────────────────────────────────┘ │
│                                               │
│  ✅ IT WORKS!                                 │
└───────────────────────────────────────────────┘
```

---

## ❌ What It Looks Like When It's BROKEN

### Broken: Backend Not Running

```
┌─────────────────────────────────┐
│  Terminal 1                     │
├─────────────────────────────────┤
│  $                              │ ← Empty! Nothing running!
│                                 │
│  ❌ PROBLEM: Backend not started│
└─────────────────────────────────┘

┌───────────────────────────────────────────────┐
│  Browser                                      │
├───────────────────────────────────────────────┤
│  ⚠️ Error Getting Feedback                    │
│  Failed to fetch                              │
│                                               │
│  ← THIS IS YOUR ERROR!                        │
└───────────────────────────────────────────────┘
```

**FIX:** Start backend in Terminal 1!

---

### Broken: Frontend Not Restarted After .env

```
┌─────────────────────────────────┐
│  Terminal 2                     │
├─────────────────────────────────┤
│  $ npm run dev                  │
│  Running...                     │
│                                 │
│  ⚠️ You created .env AFTER      │
│     starting this!              │
│                                 │
│  NEED TO RESTART!               │
└─────────────────────────────────┘
```

**FIX:** Press Ctrl+C, then `npm run dev` again

---

## ✅ Checklist - All Must Be True!

```
Before using app, verify:

Terminal 1:
  ✓ Running: python backend_simple.py
  ✓ Shows: "Running on http://localhost:5000"
  ✓ Still open (not closed)

Terminal 2:
  ✓ Running: npm run dev
  ✓ Shows: "Local: http://localhost:5173"
  ✓ Still open (not closed)
  ✓ Started AFTER .env was created

Files:
  ✓ .env exists
  ✓ .env contains: VITE_API_URL=http://localhost:5000

Browser:
  ✓ At: http://localhost:5173
  ✓ Can see game selection
  ✓ Can enter stats
  ✓ Can get feedback (no "Failed to fetch")
```

---

## 🆘 Quick Test

### Test 1: Is backend running?

```
Open Terminal 3 (another new one) and run:
$ curl http://localhost:5000/

✅ GOOD: {"status":"running"...}
❌ BAD:  Connection refused

If BAD: Backend not running! Start it in Terminal 1
```

### Test 2: Can frontend see backend?

```
In browser, press F12
Click "Console" tab
Look for errors

✅ GOOD: No errors, or just warnings
❌ BAD:  "Failed to fetch" or "CORS error"

If BAD: 
  1. Check .env exists
  2. Restart frontend (Terminal 2)
  3. Make sure backend is running (Terminal 1)
```

---

## 🎯 Success Looks Like This

```
┌─────────────────────────────────┐
│  Terminal 1 ✅                  │
│  Running backend on :5000       │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  Terminal 2 ✅                  │
│  Running frontend on :5173      │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  Browser ✅                     │
│  App loaded, can get feedback   │
└─────────────────────────────────┘

        🎉 ALL WORKING!
```

---

## Need More Help?

Run this to check everything:
```bash
python check_setup.py
```

Or read:
- [RUN_ME_FIRST.md](RUN_ME_FIRST.md) - Detailed fix guide
- [FIX_NOW.md](FIX_NOW.md) - Emergency fixes
- [FIXES.md](FIXES.md) - All solutions

**You can do this! 💪**
