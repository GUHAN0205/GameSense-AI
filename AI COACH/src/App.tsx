import { useState } from 'react';
import GameSelector from './components/GameSelector';
import StatsForm from './components/StatsForm';
import FeedbackDisplay from './components/FeedbackDisplay';
import Header from './components/Header';
import Footer from './components/Footer';
import GameTips from './components/GameTips';

export interface GameStats {
  matches: number;
  wins: number;
  blunders: number;
  endgame_losses: number;
  safe_moves: number;
  risky_moves: number;
}

function App() {
  const [selectedGame, setSelectedGame] = useState<string>('');
  const [feedback, setFeedback] = useState<string>('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string>('');

  const handleAnalyze = async (stats: GameStats) => {
    setIsLoading(true);
    setError('');
    setFeedback('');

    try {
      // Try to use Python backend if available, otherwise use built-in mock
      const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';
      const USE_MOCK = import.meta.env.VITE_USE_MOCK_BACKEND !== 'false'; // Default to true
      
      let data;
      
      if (USE_MOCK) {
        // Use built-in mock backend (no Python server needed!)
        const { mockBackendService } = await import('./services/mockBackend');
        data = await mockBackendService.analyzeGame(selectedGame, stats);
      } else {
        // Try Python backend
        const response = await fetch(`${API_URL}/analyze`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            game: selectedGame,
            ...stats,
          }),
        });

        if (!response.ok) {
          throw new Error('Backend server not responding');
        }

        data = await response.json();
      }

      setFeedback(data.ai_coach_feedback);
    } catch (err) {
      // If Python backend fails, automatically fallback to mock
      console.log('Using built-in AI coach...');
      try {
        const { mockBackendService } = await import('./services/mockBackend');
        const data = await mockBackendService.analyzeGame(selectedGame, stats);
        setFeedback(data.ai_coach_feedback);
      } catch (mockErr) {
        setError(mockErr instanceof Error ? mockErr.message : 'An error occurred');
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleReset = () => {
    setSelectedGame('');
    setFeedback('');
    setError('');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50">
      <Header />
      
      <main className="container mx-auto px-4 py-8 max-w-6xl">
        {/* Hero Section */}
        <div className="text-center mb-12">
          <div className="inline-block mb-4">
            <div className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-6 py-2 rounded-full text-sm font-semibold">
              🎮 AI-Powered Gaming Insights
            </div>
          </div>
          <h1 className="text-5xl md:text-6xl font-bold bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 bg-clip-text text-transparent mb-4">
            Level Up Your Game
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Get personalized AI coaching for 12+ games including Chess, Basketball, Valorant, FIFA, and more!
          </p>
        </div>

        {/* Main Content */}
        <div className="grid lg:grid-cols-2 gap-8 mb-12">
          {/* Left Column - Game Selection & Stats */}
          <div className="space-y-6">
            <GameSelector 
              selectedGame={selectedGame} 
              onGameSelect={setSelectedGame}
            />
            
            {selectedGame && (
              <StatsForm
                game={selectedGame}
                onAnalyze={handleAnalyze}
                isLoading={isLoading}
                onReset={handleReset}
              />
            )}
          </div>

          {/* Right Column - Feedback */}
          <div className="lg:sticky lg:top-8 h-fit space-y-6">
            <FeedbackDisplay
              feedback={feedback}
              error={error}
              isLoading={isLoading}
              selectedGame={selectedGame}
            />
            
            {selectedGame && !feedback && !isLoading && (
              <GameTips game={selectedGame} />
            )}
          </div>
        </div>

        {/* Features Section */}
        <div className="mt-16 grid md:grid-cols-3 gap-8">
          <div className="bg-white rounded-2xl p-6 shadow-lg hover:shadow-xl transition-shadow">
            <div className="w-12 h-12 bg-indigo-100 rounded-xl flex items-center justify-center mb-4">
              <span className="text-2xl">🎯</span>
            </div>
            <h3 className="text-xl font-bold text-gray-800 mb-2">Accurate Analysis</h3>
            <p className="text-gray-600">
              AI-powered insights based on your actual gameplay statistics and patterns
            </p>
          </div>

          <div className="bg-white rounded-2xl p-6 shadow-lg hover:shadow-xl transition-shadow">
            <div className="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center mb-4">
              <span className="text-2xl">📊</span>
            </div>
            <h3 className="text-xl font-bold text-gray-800 mb-2">12+ Games Supported</h3>
            <p className="text-gray-600">
              Traditional games, sports, and esports - Chess, Basketball, Valorant, FIFA, LoL, and more!
            </p>
          </div>

          <div className="bg-white rounded-2xl p-6 shadow-lg hover:shadow-xl transition-shadow">
            <div className="w-12 h-12 bg-pink-100 rounded-xl flex items-center justify-center mb-4">
              <span className="text-2xl">💡</span>
            </div>
            <h3 className="text-xl font-bold text-gray-800 mb-2">Actionable Tips</h3>
            <p className="text-gray-600">
              Receive specific, actionable advice to improve your performance
            </p>
          </div>
        </div>
      </main>

      <Footer />
    </div>
  );
}

export default App;
