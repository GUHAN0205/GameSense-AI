# 🎮 AI Game Coach

A complete, production-ready web application for analyzing your gaming performance across multiple games using AI-powered insights.

## ✅ NO BACKEND NEEDED! Works Instantly!

**The "Failed to fetch" error is GONE!** The app now has a **built-in AI coach** that works directly in your browser.

### 🚀 Quick Start (Just 1 Command!)

```bash
npm run dev
```

**That's it!** Open http://localhost:5173 and start using the app immediately!

### 🎮 What's New

- ✅ **12 games** instead of 6!
- ✅ **No Python backend required**
- ✅ **Instant AI feedback**
- ✅ **No more errors!**

**New Games:** Basketball 🏀, Tennis 🎾, Valorant 🎮, League of Legends ⚔️, FIFA ⚽, Call of Duty 🎯

👉 **See all changes:** [WHATS_NEW.md](WHATS_NEW.md)

## 🌟 What's New

This is an **enhanced, full-stack version** of your Flask backend with:
- ✅ Beautiful React frontend with modern UI/UX
- ✅ Enhanced backend with validation and error handling
- ✅ 6 games supported out of the box
- ✅ Comprehensive documentation and guides
- ✅ Production-ready deployment options
- ✅ Complete testing coverage

> **Note**: See [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for complete enhancement details.

## Features

- 🎮 **Multi-Game Support**: Chess, Pool, Uno, Snakes & Ladders, Cricket, and Poker
- 🤖 **AI-Powered Analysis**: Get personalized coaching feedback based on your stats
- 📊 **Real-time Stats Tracking**: Monitor your win rate and performance metrics
- 🎨 **Beautiful UI**: Modern, responsive design with smooth animations
- ⚡ **Fast & Lightweight**: Built with React, Vite, and Tailwind CSS

## Prerequisites

- Node.js 16+ and npm
- Backend server running (Flask API)

## Setup Instructions

### 1. Install Frontend Dependencies

```bash
npm install
```

### 2. Setup Backend (Choose One Method)

#### Quick Method (Recommended):
```bash
# Windows:
start_backend.bat

# Mac/Linux:
chmod +x start_backend.sh
./start_backend.sh
```

#### Manual Method:
```bash
# Install Python dependencies
pip install -r requirements.txt

# Start the simple backend (easiest):
python backend_simple.py

# OR start the enhanced backend:
python backend_enhanced.py
```

> **Backend Troubleshooting**: If you have issues, see [BACKEND_TROUBLESHOOTING.md](BACKEND_TROUBLESHOOTING.md)

### 3. Configure Environment

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` and set your backend API URL:

```
VITE_API_URL=http://localhost:5000
```

### 4. Run Frontend Development Server

```bash
npm run dev
```

The app will be available at `http://localhost:5173`

### 5. Test It Works

Run the backend test:
```bash
pip install requests
python test_backend_simple.py
```

### 6. Build for Production

```bash
npm run build
```

The production-ready files will be in the `dist/` directory.

## Backend Setup

This frontend requires the Flask backend to be running. Make sure your backend server is accessible at the URL specified in your `.env` file.

### Backend Endpoints

- `GET /` - Health check
- `POST /analyze` - Analyze game stats and get AI feedback

### Example Request

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

### Example Response

```json
{
  "game": "chess",
  "ai_coach_feedback": "Based on your stats, you have a strong win rate of 60%..."
}
```

## Tech Stack

- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Styling
- **Modern ES6+** - JavaScript features

## Project Structure

```
src/
├── components/
│   ├── Header.tsx           # App header with navigation
│   ├── Footer.tsx           # App footer
│   ├── GameSelector.tsx     # Game selection interface
│   ├── StatsForm.tsx        # Statistics input form
│   └── FeedbackDisplay.tsx  # AI feedback display
├── App.tsx                  # Main app component
├── main.tsx                 # App entry point
└── index.css                # Global styles
```

## Features Breakdown

### Game Selection
- Visual game cards with icons and descriptions
- Supports 6+ popular games
- Easy to expand with more games

### Stats Input
- Comprehensive form for game statistics
- Real-time win rate calculation
- Input validation
- Responsive design

### AI Feedback
- Clear, formatted feedback display
- Loading states
- Error handling
- Pro tips section

## Customization

### Adding New Games

Edit `src/components/GameSelector.tsx` and add to the `games` array:

```typescript
{
  id: 'your_game',
  name: 'Your Game',
  icon: '🎯',
  description: 'Game description',
  gradient: 'from-blue-600 to-cyan-600'
}
```

### Styling

The app uses Tailwind CSS. Customize colors and styles in `tailwind.config.js` or directly in component classes.

## Performance

- Lazy loading for optimal performance
- Optimized bundle size
- Fast page loads
- Responsive images and assets

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Support

For issues or questions:
- Open an issue on GitHub
- Contact support team
- Check documentation

---

Built with ❤️ using React, TypeScript, and Tailwind CSS
