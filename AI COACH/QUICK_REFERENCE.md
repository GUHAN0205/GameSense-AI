# Quick Reference Card

Essential commands and information for AI Game Coach.

## 🚀 Quick Start

### Frontend (Development)
```bash
npm install
npm run dev
```
Open: http://localhost:5173

### Backend (Development)
```bash
python backend_enhanced.py
```
Runs on: http://localhost:5000

## 📁 Key Files

| File | Purpose |
|------|---------|
| `src/App.tsx` | Main frontend component |
| `backend_enhanced.py` | Enhanced Flask backend |
| `coach_agent_mock.py` | Mock AI coach (replace with real AI) |
| `.env` | Environment variables |
| `README.md` | Main documentation |

## 🔧 Common Commands

### Development
```bash
npm run dev          # Start dev server
npm run build        # Build for production
npm run preview      # Preview production build
```

### Backend
```bash
python backend_enhanced.py              # Development
gunicorn -w 4 backend_enhanced:app      # Production
```

### Testing
```bash
npm run build                           # Test frontend build
python test_backend.py                  # Test backend (create file)
curl http://localhost:5000/             # Test health
```

## 📋 Environment Variables

### Frontend (.env)
```bash
VITE_API_URL=http://localhost:5000
```

### Backend (.env)
```bash
PORT=5000
DEBUG=True
FLASK_ENV=development
```

## 🎯 Supported Games

1. ♟️ Chess
2. 🎱 Pool
3. 🃏 Uno
4. 🎲 Snakes & Ladders
5. 🏏 Cricket
6. ♠️ Poker

## 🔗 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/` | Health check |
| GET | `/health` | Detailed health |
| POST | `/analyze` | Analyze stats |

## 📊 Stats Fields

```json
{
  "game": "string",
  "matches": "number",
  "wins": "number",
  "blunders": "number",
  "endgame_losses": "number",
  "safe_moves": "number",
  "risky_moves": "number"
}
```

## 🎨 Component Structure

```
App
├── Header
├── GameSelector
├── StatsForm
├── FeedbackDisplay
├── GameTips
└── Footer
```

## 📦 Tech Stack

**Frontend**: React + TypeScript + Vite + Tailwind  
**Backend**: Flask + Python  
**Deployment**: Vercel/Netlify (Frontend), Heroku/Railway (Backend)

## 🛠️ Customization Quick Links

### Add New Game
1. Edit `src/components/GameSelector.tsx`
2. Add tips in `src/components/GameTips.tsx`
3. Add coach logic in `coach_agent_mock.py`

### Change Colors
Edit Tailwind classes in components:
- Primary: `indigo-600`
- Secondary: `purple-600`
- Accent: `pink-600`

### Modify Stats
1. Update `GameStats` interface in `App.tsx`
2. Add input field in `StatsForm.tsx`
3. Handle in backend

## 🐛 Troubleshooting

### Frontend won't start
```bash
rm -rf node_modules
npm install
npm run dev
```

### Backend errors
```bash
# Check Python version
python --version  # Need 3.8+

# Reinstall dependencies
pip install Flask flask-cors
```

### CORS issues
- Check `VITE_API_URL` in `.env`
- Verify CORS config in `backend_enhanced.py`
- Check browser console for errors

### Build fails
```bash
rm -rf dist
npm run build
```

## 📚 Documentation Index

| Document | Purpose |
|----------|---------|
| [README.md](README.md) | Main overview |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | Complete enhancement details |
| [DEPLOYMENT.md](DEPLOYMENT.md) | Deployment guides |
| [BACKEND_SETUP.md](BACKEND_SETUP.md) | Backend setup |
| [TESTING.md](TESTING.md) | Testing guide |
| [USAGE_GUIDE.md](USAGE_GUIDE.md) | User & dev guide |
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | This file |

## 🔐 Security Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Use environment variables for secrets
- [ ] Configure CORS with specific origins
- [ ] Validate all inputs
- [ ] Use HTTPS
- [ ] Keep dependencies updated

## 📈 Performance Tips

- Bundle size: 237KB (70KB gzipped) ✅
- Build time: ~1 second ✅
- Use production build for deployment
- Enable gzip compression
- Use CDN for static assets

## 🚢 Deployment Quick Commands

### Vercel (Frontend)
```bash
npm install -g vercel
vercel
```

### Heroku (Backend)
```bash
heroku create
git push heroku main
```

## 💡 Pro Tips

1. **Development**: Use split terminal for frontend + backend
2. **Testing**: Test locally before deploying
3. **Debugging**: Check browser DevTools Network tab
4. **AI Integration**: Replace mock coach with real AI
5. **Database**: Add PostgreSQL for user data
6. **Analytics**: Add Google Analytics for insights

## 📞 Support

- Check browser console for errors
- Review backend logs
- Test API with curl or Postman
- Read documentation
- Open GitHub issue

## 🎯 Next Steps

1. ✅ Setup development environment
2. ✅ Run locally and test
3. ✅ Customize for your needs
4. ⬜ Integrate real AI
5. ⬜ Deploy to production
6. ⬜ Add user authentication
7. ⬜ Implement database
8. ⬜ Add analytics

---

**Need more details?** Check the full documentation files listed above.

**Ready to deploy?** See [DEPLOYMENT.md](DEPLOYMENT.md)

**Want to customize?** See [USAGE_GUIDE.md](USAGE_GUIDE.md)
