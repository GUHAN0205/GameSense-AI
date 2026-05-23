=====================================================
  AI GAME COACH - SIMPLE INSTRUCTIONS
=====================================================

YOU'RE GETTING "Failed to fetch" ERROR?
The backend is not running. Here's how to fix it:

=====================================================
  EASIEST METHOD - DOUBLE CLICK TO START
=====================================================

Windows Users:
  1. Find the file: START_BACKEND.bat
  2. Double-click it
  3. A window will open showing the backend running
  4. KEEP THAT WINDOW OPEN!
  5. Go back to your browser and try again

Mac/Linux Users:
  1. Open Terminal
  2. Navigate to this folder:
     cd /path/to/ai-game-coach
  3. Run:
     chmod +x START_BACKEND.sh
     ./START_BACKEND.sh
  4. KEEP TERMINAL OPEN!
  5. Go back to your browser and try again

=====================================================
  MANUAL METHOD
=====================================================

1. Open a NEW terminal/command prompt
   (Don't close your existing one!)

2. Navigate to this folder:
   cd /path/to/ai-game-coach

3. Install dependencies:
   pip install Flask flask-cors

4. Start backend:
   python backend_simple.py

5. You should see:
   "Running on http://localhost:5000"

6. KEEP THIS TERMINAL OPEN!

7. Go to browser: http://localhost:5173

8. Try the app again - it should work!

=====================================================
  WHAT YOU NEED RUNNING
=====================================================

You need TWO things running at the same time:

1. Frontend (you already have this running)
   - Shows: "Local: http://localhost:5173"

2. Backend (this is what you need to start!)
   - Shows: "Running on http://localhost:5000"

Both must be running for the app to work!

=====================================================
  TESTING IF IT WORKS
=====================================================

Open a browser and go to: http://localhost:5000/

You should see:
{"status":"running","message":"AI Game Coach Backend is Running"}

If you see that, the backend is working!

=====================================================
  STILL NOT WORKING?
=====================================================

Read these files in order:
1. INSTANT_FIX.md
2. RUN_ME_FIRST.md
3. VISUAL_GUIDE.md

Or run the diagnostic:
python check_setup.py

=====================================================
  QUICK SUMMARY
=====================================================

Problem: "Failed to fetch" error
Cause: Backend not running
Solution: Start the backend!

Windows: Double-click START_BACKEND.bat
Mac/Linux: Run ./START_BACKEND.sh

Keep both terminals open, then try the app!

=====================================================
