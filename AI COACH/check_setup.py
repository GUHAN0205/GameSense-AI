#!/usr/bin/env python3
"""
Setup Checker - Run this to diagnose your setup!
This will check everything and tell you exactly what's wrong.
"""

import os
import sys
import subprocess

def print_header(text):
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def check_mark(passed):
    return "✅" if passed else "❌"

def run_checks():
    print_header("AI Game Coach - Setup Checker")
    print("\nThis will check your entire setup...\n")
    
    issues = []
    
    # Check 1: Python version
    print("1️⃣  Checking Python version...")
    py_version = sys.version_info
    if py_version.major >= 3 and py_version.minor >= 8:
        print(f"   {check_mark(True)} Python {py_version.major}.{py_version.minor}.{py_version.micro}")
    else:
        print(f"   {check_mark(False)} Python version too old: {py_version.major}.{py_version.minor}")
        issues.append("Upgrade Python to 3.8 or higher")
    
    # Check 2: Flask installed
    print("\n2️⃣  Checking Flask...")
    try:
        import flask
        print(f"   {check_mark(True)} Flask {flask.__version__} installed")
    except ImportError:
        print(f"   {check_mark(False)} Flask not installed")
        issues.append("Run: pip install Flask flask-cors")
    
    # Check 3: Flask-CORS installed
    print("\n3️⃣  Checking Flask-CORS...")
    try:
        import flask_cors
        print(f"   {check_mark(True)} Flask-CORS installed")
    except ImportError:
        print(f"   {check_mark(False)} Flask-CORS not installed")
        issues.append("Run: pip install flask-cors")
    
    # Check 4: Backend files exist
    print("\n4️⃣  Checking backend files...")
    backend_simple = os.path.exists("backend_simple.py")
    backend_enhanced = os.path.exists("backend_enhanced.py")
    
    print(f"   {check_mark(backend_simple)} backend_simple.py")
    print(f"   {check_mark(backend_enhanced)} backend_enhanced.py")
    
    if not backend_simple and not backend_enhanced:
        issues.append("No backend files found! Are you in the right directory?")
    
    # Check 5: .env file
    print("\n5️⃣  Checking .env file...")
    if os.path.exists(".env"):
        print(f"   {check_mark(True)} .env file exists")
        with open(".env", "r") as f:
            content = f.read()
            if "VITE_API_URL" in content:
                print(f"   {check_mark(True)} VITE_API_URL is set")
                # Extract the URL
                for line in content.split('\n'):
                    if 'VITE_API_URL' in line:
                        print(f"   📋 Value: {line.strip()}")
            else:
                print(f"   {check_mark(False)} VITE_API_URL not found in .env")
                issues.append("Add to .env: VITE_API_URL=http://localhost:5000")
    else:
        print(f"   {check_mark(False)} .env file not found")
        issues.append("Create .env file with: VITE_API_URL=http://localhost:5000")
    
    # Check 6: Backend running
    print("\n6️⃣  Checking if backend is running...")
    try:
        import requests
        response = requests.get("http://localhost:5000/", timeout=2)
        if response.status_code == 200:
            print(f"   {check_mark(True)} Backend is running on port 5000")
            data = response.json()
            print(f"   📋 Status: {data.get('message', 'Running')}")
        else:
            print(f"   {check_mark(False)} Backend returned status {response.status_code}")
            issues.append("Backend is running but returned an error")
    except ImportError:
        print(f"   ⚠️  'requests' module not installed (needed for testing)")
        print(f"   ℹ️  Install with: pip install requests")
    except Exception as e:
        print(f"   {check_mark(False)} Cannot connect to backend")
        print(f"   📋 Error: {str(e)}")
        issues.append("Start backend: python backend_simple.py")
    
    # Check 7: Node modules
    print("\n7️⃣  Checking frontend setup...")
    if os.path.exists("node_modules"):
        print(f"   {check_mark(True)} node_modules installed")
    else:
        print(f"   {check_mark(False)} node_modules not found")
        issues.append("Run: npm install")
    
    if os.path.exists("package.json"):
        print(f"   {check_mark(True)} package.json exists")
    else:
        print(f"   {check_mark(False)} package.json not found")
        issues.append("Are you in the right directory?")
    
    # Summary
    print_header("Summary")
    
    if not issues:
        print("\n🎉 Everything looks good!\n")
        print("To use the app:")
        print("  1. Terminal 1: python backend_simple.py")
        print("  2. Terminal 2: npm run dev")
        print("  3. Browser: http://localhost:5173")
    else:
        print("\n⚠️  Found some issues:\n")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
        
        print("\n" + "="*60)
        print("QUICK FIX:")
        print("="*60)
        print("\n# Install Python dependencies:")
        print("pip install Flask flask-cors requests")
        print("\n# Create .env file:")
        print('echo "VITE_API_URL=http://localhost:5000" > .env')
        print("\n# Install Node dependencies:")
        print("npm install")
        print("\n# Start backend:")
        print("python backend_simple.py")
        print("\n# In another terminal, start frontend:")
        print("npm run dev")
        print("\n" + "="*60)
    
    print("\nFor more help, see: FIX_NOW.md or FIXES.md\n")

if __name__ == "__main__":
    try:
        run_checks()
    except KeyboardInterrupt:
        print("\n\nCheck cancelled.")
    except Exception as e:
        print(f"\n\nError running checks: {e}")
        print("But don't worry! Try the manual steps in FIX_NOW.md")
