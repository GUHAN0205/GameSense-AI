# ⚠️ "Failed to fetch" Error - Fix It Now!

This error means your frontend can't reach the backend. Let's fix it!

## Step 1: Is the Backend Running?

Open a **NEW terminal** (don't close the frontend one) and type:

```bash
curl http://localhost:5000/
```

### Result A: You see JSON like `{"status":"running"...}`
✅ **Backend is working!** Skip to Step 3.

### Result B: "Connection refused" or "Could not resolve host"
❌ **Backend is NOT running.** Do Step 2.

---

## Step 2: Start the Backend

In your **NEW terminal**, run:

```bash
# Install dependencies first
pip install Flask flask-cors

# Start the simple backend
python backend_simple.py
```

You should see:
```
🚀 AI Game Coach Backend (Simple Version)
📡 Running on http://localhost:5000
```

**Keep this terminal open!**

Now test again:
```bash
# In ANOTHER terminal
curl http://localhost:5000/
```

Should show: `{"status":"running"...}`

✅ **Working?** Continue to Step 3.

---

## Step 3: Check .env File

In your project folder, check if `.env` file exists:

```bash
# See if .env exists
ls -la .env     # Mac/Linux
dir .env        # Windows
```

### If .env does NOT exist:
Create it now:

```bash
# Mac/Linux
echo "VITE_API_URL=http://localhost:5000" > .env

# Windows
echo VITE_API_URL=http://localhost:5000 > .env
```

### If .env DOES exist:
Open it and make sure it says **exactly**:
```
VITE_API_URL=http://localhost:5000
```

No extra spaces, no quotes, no trailing slashes!

---

## Step 4: Restart Frontend

**Important!** After creating/changing .env, you MUST restart:

1. Go to terminal running `npm run dev`
2. Press `Ctrl+C` to stop it
3. Run again:
```bash
npm run dev
```

---

## Step 5: Test in Browser

1. Open http://localhost:5173
2. Press `F12` to open Developer Tools
3. Click **Console** tab
4. Try to get AI feedback
5. Look at the console

### What do you see?

**"Failed to fetch"** → .env is wrong or backend stopped
**CORS error** → Backend not configured (use backend_simple.py)
**No error** → It's working!

---

## Quick Fix Summary

```bash
# Terminal 1 - Backend
pip install Flask flask-cors
python backend_simple.py
# Keep this running!

# Terminal 2 - Create .env
echo "VITE_API_URL=http://localhost:5000" > .env

# Terminal 2 - Restart Frontend
# Press Ctrl+C if npm run dev is running
npm run dev

# Browser
# Go to http://localhost:5173
# Try again!
```

---

## Still Not Working?

Run this diagnostic:

```bash
pip install requests
python test_backend_simple.py
```

This will tell you EXACTLY what's wrong!
