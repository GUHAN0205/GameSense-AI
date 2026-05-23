import { useState } from 'react';
import { GameStats } from '../App';

interface StatsFormProps {
  game: string;
  onAnalyze: (stats: GameStats) => void;
  isLoading: boolean;
  onReset: () => void;
}

export default function StatsForm({ onAnalyze, isLoading, onReset }: StatsFormProps) {
  const [stats, setStats] = useState<GameStats>({
    matches: 0,
    wins: 0,
    blunders: 0,
    endgame_losses: 0,
    safe_moves: 0,
    risky_moves: 0,
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onAnalyze(stats);
  };

  const handleChange = (field: keyof GameStats, value: string) => {
    setStats(prev => ({
      ...prev,
      [field]: parseInt(value) || 0
    }));
  };

  const winRate = stats.matches > 0 ? ((stats.wins / stats.matches) * 100).toFixed(1) : '0';

  return (
    <div className="bg-white rounded-2xl shadow-xl p-6">
      <div className="flex items-center justify-between mb-6">
        <div>
          <h2 className="text-2xl font-bold text-gray-800">Enter Your Stats</h2>
          <p className="text-gray-600">Provide your gameplay statistics</p>
        </div>
        <button
          onClick={onReset}
          className="text-sm text-gray-500 hover:text-indigo-600 transition-colors"
        >
          Reset All
        </button>
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        {/* Win Rate Display */}
        <div className="bg-gradient-to-r from-indigo-50 to-purple-50 rounded-xl p-4 mb-6">
          <div className="text-sm text-gray-600 mb-1">Current Win Rate</div>
          <div className="text-3xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
            {winRate}%
          </div>
          <div className="text-xs text-gray-500 mt-1">
            {stats.wins} wins out of {stats.matches} matches
          </div>
        </div>

        {/* General Stats */}
        <div className="space-y-4">
          <h3 className="font-semibold text-gray-700 text-sm uppercase tracking-wide">General Stats</h3>
          
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Total Matches
              </label>
              <input
                type="number"
                min="0"
                value={stats.matches}
                onChange={(e) => handleChange('matches', e.target.value)}
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
                required
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Wins
              </label>
              <input
                type="number"
                min="0"
                max={stats.matches}
                value={stats.wins}
                onChange={(e) => handleChange('wins', e.target.value)}
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
                required
              />
            </div>
          </div>
        </div>

        {/* Performance Stats */}
        <div className="space-y-4">
          <h3 className="font-semibold text-gray-700 text-sm uppercase tracking-wide mt-6">Performance Metrics</h3>
          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Blunders / Mistakes
            </label>
            <input
              type="number"
              min="0"
              value={stats.blunders}
              onChange={(e) => handleChange('blunders', e.target.value)}
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Endgame Losses
            </label>
            <input
              type="number"
              min="0"
              value={stats.endgame_losses}
              onChange={(e) => handleChange('endgame_losses', e.target.value)}
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Safe Moves
              </label>
              <input
                type="number"
                min="0"
                value={stats.safe_moves}
                onChange={(e) => handleChange('safe_moves', e.target.value)}
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Risky Moves
              </label>
              <input
                type="number"
                min="0"
                value={stats.risky_moves}
                onChange={(e) => handleChange('risky_moves', e.target.value)}
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
              />
            </div>
          </div>
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          disabled={isLoading || stats.matches === 0}
          className="w-full mt-6 bg-gradient-to-r from-indigo-600 to-purple-600 text-white py-4 rounded-lg font-semibold text-lg hover:shadow-lg disabled:opacity-50 disabled:cursor-not-allowed transition-all transform hover:scale-[1.02] active:scale-[0.98]"
        >
          {isLoading ? (
            <span className="flex items-center justify-center">
              <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Analyzing...
            </span>
          ) : (
            '🎯 Get AI Coaching'
          )}
        </button>
      </form>
    </div>
  );
}
