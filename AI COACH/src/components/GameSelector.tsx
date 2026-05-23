interface GameSelectorProps {
  selectedGame: string;
  onGameSelect: (game: string) => void;
}

const games = [
  {
    id: 'chess',
    name: 'Chess',
    icon: '♟️',
    description: 'Strategic board game',
    gradient: 'from-gray-700 to-gray-900'
  },
  {
    id: 'pool',
    name: 'Pool',
    icon: '🎱',
    description: 'Precision cue sport',
    gradient: 'from-green-600 to-emerald-700'
  },
  {
    id: 'uno',
    name: 'Uno',
    icon: '🃏',
    description: 'Fast-paced card game',
    gradient: 'from-red-600 to-orange-600'
  },
  {
    id: 'snakes_ladders',
    name: 'Snakes & Ladders',
    icon: '🎲',
    description: 'Classic dice game',
    gradient: 'from-blue-600 to-cyan-600'
  },
  {
    id: 'cricket',
    name: 'Cricket',
    icon: '🏏',
    description: 'Bat and ball sport',
    gradient: 'from-indigo-600 to-purple-600'
  },
  {
    id: 'poker',
    name: 'Poker',
    icon: '♠️',
    description: 'Strategic card game',
    gradient: 'from-purple-600 to-pink-600'
  },
  {
    id: 'basketball',
    name: 'Basketball',
    icon: '🏀',
    description: 'Fast-paced team sport',
    gradient: 'from-orange-500 to-red-600'
  },
  {
    id: 'tennis',
    name: 'Tennis',
    icon: '🎾',
    description: 'Racquet sport',
    gradient: 'from-yellow-500 to-green-600'
  },
  {
    id: 'valorant',
    name: 'Valorant',
    icon: '🎮',
    description: 'Tactical FPS',
    gradient: 'from-red-500 to-black'
  },
  {
    id: 'lol',
    name: 'League of Legends',
    icon: '⚔️',
    description: 'MOBA strategy game',
    gradient: 'from-blue-500 to-purple-700'
  },
  {
    id: 'fifa',
    name: 'FIFA',
    icon: '⚽',
    description: 'Soccer simulation',
    gradient: 'from-green-500 to-blue-600'
  },
  {
    id: 'cod',
    name: 'Call of Duty',
    icon: '🎯',
    description: 'FPS shooter',
    gradient: 'from-slate-700 to-red-700'
  }
];

export default function GameSelector({ selectedGame, onGameSelect }: GameSelectorProps) {
  return (
    <div className="bg-white rounded-2xl shadow-xl p-6">
      <h2 className="text-2xl font-bold text-gray-800 mb-2">Select Your Game</h2>
      <p className="text-gray-600 mb-6">Choose the game you want to analyze</p>
      
      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
        {games.map((game) => (
          <button
            key={game.id}
            onClick={() => onGameSelect(game.id)}
            className={`
              relative overflow-hidden rounded-xl p-4 transition-all duration-300
              ${selectedGame === game.id 
                ? 'ring-4 ring-indigo-400 scale-105 shadow-lg' 
                : 'hover:scale-105 hover:shadow-md'
              }
            `}
          >
            <div className={`absolute inset-0 bg-gradient-to-br ${game.gradient} opacity-${selectedGame === game.id ? '100' : '80'}`} />
            <div className="relative z-10">
              <div className="text-4xl mb-2">{game.icon}</div>
              <div className="text-white font-bold text-sm mb-1">{game.name}</div>
              <div className="text-white text-xs opacity-90">{game.description}</div>
            </div>
          </button>
        ))}
      </div>
    </div>
  );
}
