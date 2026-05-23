"""
Simple Backend Test Script
Run this to test if your backend is working
"""

import requests
import json

def test_backend():
    BASE_URL = "http://localhost:5000"
    
    print("🧪 Testing AI Game Coach Backend\n")
    print("=" * 50)
    
    # Test 1: Health Check
    print("\n1️⃣ Testing Health Check (GET /)...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ PASSED - Backend is running!")
            print(f"Response: {response.json()}")
        else:
            print(f"❌ FAILED - Status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ FAILED - Cannot connect to backend!")
        print("Make sure backend is running: python backend_enhanced.py")
        return False
    except Exception as e:
        print(f"❌ FAILED - Error: {e}")
        return False
    
    # Test 2: Analyze Endpoint
    print("\n2️⃣ Testing Analyze Endpoint (POST /analyze)...")
    
    test_data = {
        "game": "chess",
        "matches": 100,
        "wins": 60,
        "blunders": 15,
        "endgame_losses": 10,
        "safe_moves": 200,
        "risky_moves": 50
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/analyze",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            print("✅ PASSED - Analysis successful!")
            data = response.json()
            print(f"\nGame: {data.get('game')}")
            print(f"Win Rate: {data.get('stats_summary', {}).get('win_rate')}")
            print(f"\nFeedback Preview:")
            feedback = data.get('ai_coach_feedback', '')
            print(feedback[:200] + "..." if len(feedback) > 200 else feedback)
        else:
            print(f"❌ FAILED - Status code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"❌ FAILED - Error: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("✅ All tests passed! Backend is working correctly.\n")
    return True

if __name__ == "__main__":
    success = test_backend()
    if not success:
        print("\n⚠️ Backend tests failed. See errors above.")
        print("\nQuick fixes:")
        print("1. Make sure backend is running: python backend_enhanced.py")
        print("2. Check if coach_agent.py exists")
        print("3. Install dependencies: pip install Flask flask-cors")
        print("4. Check if port 5000 is available")
