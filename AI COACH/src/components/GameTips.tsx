interface GameTipsProps {
  game: string;
}

const gameTips: Record<string, string[]> = {
  chess: [
    'Control the center of the board early',
    'Develop your pieces before attacking',
    'Castle early to protect your king',
    'Think 3-5 moves ahead',
  ],
  pool: [
    'Plan your shot sequence before breaking',
    'Focus on cue ball positioning',
    'Practice your break shot consistently',
    'Use safety shots when needed',
  ],
  uno: [
    'Save wild cards for crucial moments',
    'Track colors opponents are collecting',
    'Use action cards strategically',
    'Watch for players close to winning',
  ],
  snakes_ladders: [
    'Stay positive - it\'s a game of chance!',
    'Enjoy the journey with friends',
    'Remember: everyone has equal odds',
    'Have fun and don\'t take it too seriously',
  ],
  cricket: [
    'Watch the ball until it hits the bat',
    'Keep your head still during shots',
    'Play according to field placement',
    'Rotate strike to keep pressure',
  ],
  poker: [
    'Position is power - play more hands in late position',
    'Study pot odds and expected value',
    'Observe opponents\' betting patterns',
    'Manage your bankroll wisely',
  ],
  basketball: [
    'Practice your shooting form daily',
    'Keep your head up while dribbling',
    'Communicate with teammates on defense',
    'Box out on every rebound',
  ],
  tennis: [
    'Develop a reliable first serve',
    'Keep your feet moving between shots',
    'Hit with topspin for consistency',
    'Stay mentally tough point by point',
  ],
  valorant: [
    'Crosshair placement at head level',
    'Use utility before entering sites',
    'Communicate enemy positions',
    'Practice in deathmatch daily',
  ],
  lol: [
    'Check minimap every 3-5 seconds',
    'Focus on CS and gold income',
    'Ward key jungle paths',
    'Play 2-3 champions consistently',
  ],
  fifa: [
    'Practice timed finishing',
    'Use driven passes for speed',
    'Jockey instead of rushing tackles',
    'Control possession to create space',
  ],
  cod: [
    'Pre-aim common angles',
    'Learn the spawns on each map',
    'Use cover effectively',
    'Find your optimal sensitivity',
  ],
};

export default function GameTips({ game }: GameTipsProps) {
  const tips = gameTips[game] || [
    'Practice regularly to improve',
    'Learn from your mistakes',
    'Study strategies from experts',
    'Stay focused and patient',
  ];

  return (
    <div className="bg-gradient-to-br from-indigo-50 to-purple-50 rounded-2xl p-6 shadow-lg">
      <div className="flex items-center mb-4">
        <span className="text-2xl mr-3">💡</span>
        <h3 className="text-lg font-bold text-gray-800">Quick Tips</h3>
      </div>
      <ul className="space-y-2">
        {tips.map((tip, index) => (
          <li key={index} className="flex items-start">
            <span className="text-indigo-600 mr-2 mt-1">•</span>
            <span className="text-gray-700 text-sm">{tip}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
