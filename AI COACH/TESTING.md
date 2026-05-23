# Testing Guide

This guide covers how to test both the frontend and backend of the AI Game Coach application.

## Frontend Testing

### Manual Testing Checklist

#### UI/UX Tests
- [ ] All games display correctly in the selector
- [ ] Game cards highlight when selected
- [ ] Stats form appears after game selection
- [ ] All input fields accept valid numbers
- [ ] Win rate calculates correctly
- [ ] Form validation prevents invalid submissions
- [ ] Loading state displays during API calls
- [ ] Success feedback displays properly
- [ ] Error messages are clear and helpful
- [ ] Reset button clears all data
- [ ] Responsive design works on mobile
- [ ] Animations are smooth
- [ ] No console errors

#### Functionality Tests
- [ ] Can select different games
- [ ] Can enter statistics
- [ ] Submit button is disabled when matches = 0
- [ ] Loading spinner shows during request
- [ ] Feedback displays after successful request
- [ ] Error displays after failed request
- [ ] Game tips show when game is selected
- [ ] Can switch between games
- [ ] Stats persist during same game selection

#### Browser Compatibility
Test in:
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

#### Responsive Design
Test at breakpoints:
- [ ] Mobile (320px - 640px)
- [ ] Tablet (641px - 1024px)
- [ ] Desktop (1025px+)
- [ ] Large screens (1920px+)

### Test Scenarios

#### Scenario 1: New User Flow
1. Load the application
2. See hero section and game selector
3. Select a game (e.g., Chess)
4. See stats form and game tips
5. Enter valid statistics
6. Click "Get AI Coaching"
7. See loading state
8. Receive feedback
9. Review coaching advice

#### Scenario 2: Multiple Games
1. Select Chess and enter stats
2. Get feedback
3. Click reset or select different game (Pool)
4. Enter Pool stats
5. Get feedback
6. Verify feedback is game-specific

#### Scenario 3: Error Handling
1. Disconnect backend or use invalid URL
2. Enter stats and submit
3. Verify error message displays
4. Verify error is user-friendly

#### Scenario 4: Edge Cases
1. Enter 0 matches (button should be disabled)
2. Enter wins > matches (backend should reject)
3. Enter very large numbers (test limits)
4. Enter negative numbers (should be prevented)

### Performance Testing

```bash
# Build the project
npm run build

# Analyze bundle size
npm run build -- --analyze

# Test with Lighthouse
# Use Chrome DevTools > Lighthouse tab
```

**Target Metrics:**
- Performance: > 90
- Accessibility: > 95
- Best Practices: > 90
- SEO: > 90

## Backend Testing

### Manual Testing with curl

#### Test Health Check
```bash
curl http://localhost:5000/
```

Expected: Status 200, JSON response with "running" status

#### Test Valid Request
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

Expected: Status 200, feedback in response

#### Test Invalid Request (Missing Data)
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{}'
```

Expected: Status 400, error message

#### Test Invalid Request (Wins > Matches)
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "game": "chess",
    "matches": 50,
    "wins": 100
  }'
```

Expected: Status 400, validation error

### Automated Testing with Python

Create `test_backend.py`:

```python
import requests
import json

BASE_URL = "http://localhost:5000"

def test_health_check():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "running"
    print("✓ Health check passed")

def test_valid_analysis():
    payload = {
        "game": "chess",
        "matches": 100,
        "wins": 60,
        "blunders": 15,
        "endgame_losses": 10,
        "safe_moves": 200,
        "risky_moves": 50
    }
    response = requests.post(f"{BASE_URL}/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "ai_coach_feedback" in data
    assert data["game"] == "chess"
    print("✓ Valid analysis passed")

def test_missing_required_fields():
    payload = {"game": "chess"}
    response = requests.post(f"{BASE_URL}/analyze", json=payload)
    assert response.status_code == 400
    print("✓ Missing fields validation passed")

def test_invalid_data():
    payload = {
        "game": "chess",
        "matches": 50,
        "wins": 100  # Invalid: wins > matches
    }
    response = requests.post(f"{BASE_URL}/analyze", json=payload)
    assert response.status_code == 400
    print("✓ Invalid data validation passed")

def test_negative_numbers():
    payload = {
        "game": "chess",
        "matches": -10,  # Invalid: negative
        "wins": 5
    }
    response = requests.post(f"{BASE_URL}/analyze", json=payload)
    assert response.status_code == 400
    print("✓ Negative number validation passed")

def test_all_games():
    games = ["chess", "pool", "uno", "snakes_ladders", "cricket", "poker"]
    for game in games:
        payload = {
            "game": game,
            "matches": 100,
            "wins": 50
        }
        response = requests.post(f"{BASE_URL}/analyze", json=payload)
        assert response.status_code == 200
        print(f"✓ {game} analysis passed")

if __name__ == "__main__":
    print("Running backend tests...\n")
    try:
        test_health_check()
        test_valid_analysis()
        test_missing_required_fields()
        test_invalid_data()
        test_negative_numbers()
        test_all_games()
        print("\n✅ All tests passed!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except requests.exceptions.ConnectionError:
        print("\n❌ Cannot connect to backend. Is it running?")
```

Run tests:
```bash
python test_backend.py
```

### Load Testing

Use Apache Bench or similar tools:

```bash
# Install Apache Bench (comes with Apache)
# Test with 1000 requests, 10 concurrent
ab -n 1000 -c 10 -p test_data.json -T application/json http://localhost:5000/analyze
```

Create `test_data.json`:
```json
{
  "game": "chess",
  "matches": 100,
  "wins": 60,
  "blunders": 15,
  "endgame_losses": 10,
  "safe_moves": 200,
  "risky_moves": 50
}
```

### Security Testing

#### Test CORS
```bash
# Should fail without proper origin
curl -X POST http://localhost:5000/analyze \
  -H "Origin: http://malicious-site.com" \
  -H "Content-Type: application/json" \
  -d '{"game":"chess","matches":100,"wins":50}'
```

#### Test SQL Injection (if using database)
Try injecting SQL in game name:
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"game":"chess; DROP TABLE users;","matches":100,"wins":50}'
```

Should be handled safely by validation.

#### Test XSS (Cross-Site Scripting)
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"game":"<script>alert(1)</script>","matches":100,"wins":50}'
```

Should be sanitized or rejected.

## Integration Testing

### Full Stack Test

1. **Start Backend**
   ```bash
   python backend_enhanced.py
   ```

2. **Start Frontend**
   ```bash
   npm run dev
   ```

3. **Test End-to-End Flow**
   - Open `http://localhost:5173`
   - Select a game
   - Enter statistics
   - Submit form
   - Verify feedback appears
   - Check browser DevTools for errors
   - Verify Network tab shows successful API call

### Automated E2E Testing (Optional)

Using Playwright or Cypress:

```javascript
// Example with Playwright
import { test, expect } from '@playwright/test';

test('complete user flow', async ({ page }) => {
  await page.goto('http://localhost:5173');
  
  // Select chess
  await page.click('text=Chess');
  
  // Fill in stats
  await page.fill('input[name="matches"]', '100');
  await page.fill('input[name="wins"]', '60');
  
  // Submit
  await page.click('button:has-text("Get AI Coaching")');
  
  // Wait for and verify feedback
  await expect(page.locator('text=AI Coach Feedback')).toBeVisible();
});
```

## Test Coverage Goals

### Frontend
- [ ] All components render without errors
- [ ] All user interactions work correctly
- [ ] Form validation works
- [ ] API integration works
- [ ] Error states display properly
- [ ] Loading states work
- [ ] Responsive design works

### Backend
- [ ] All endpoints respond correctly
- [ ] Input validation works
- [ ] Error handling works
- [ ] CORS is configured properly
- [ ] AI coach integration works
- [ ] Logging works

## Continuous Testing

### Pre-commit Checks
```bash
# Add to .git/hooks/pre-commit
npm run build
# If build fails, commit is rejected
```

### CI/CD Integration
Add to `.github/workflows/test.yml`:

```yaml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
        with:
          node-version: '18'
      - run: npm install
      - run: npm run build
      - run: npm test # if you add unit tests
```

## Debugging Tips

### Frontend
1. Open Browser DevTools (F12)
2. Check Console for errors
3. Check Network tab for API calls
4. Use React DevTools extension
5. Add breakpoints in code

### Backend
1. Check terminal output for logs
2. Add print statements for debugging
3. Use Python debugger (pdb)
4. Check request/response in curl or Postman
5. Verify environment variables are set

## Common Issues

### Frontend Won't Connect to Backend
- Check VITE_API_URL in .env
- Verify backend is running
- Check CORS configuration
- Check browser console for errors

### Backend Returns Errors
- Check request payload format
- Verify all required fields are present
- Check validation rules
- Review backend logs

### Slow Performance
- Check network throttling in DevTools
- Profile with React DevTools
- Check bundle size
- Optimize images
- Check API response times

---

Regular testing ensures a stable, reliable application. Test early and often!
