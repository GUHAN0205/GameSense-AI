interface QuickStatsProps {
  stats: {
    matches: number;
    wins: number;
    blunders: number;
    endgame_losses: number;
  };
}

export default function QuickStats({ stats }: QuickStatsProps) {
  const winRate = stats.matches > 0 ? ((stats.wins / stats.matches) * 100).toFixed(1) : '0';
  const losses = stats.matches - stats.wins;

  const statCards = [
    {
      label: 'Win Rate',
      value: `${winRate}%`,
      icon: '🎯',
      color: 'from-green-500 to-emerald-600',
    },
    {
      label: 'Total Games',
      value: stats.matches,
      icon: '🎮',
      color: 'from-blue-500 to-cyan-600',
    },
    {
      label: 'Victories',
      value: stats.wins,
      icon: '🏆',
      color: 'from-yellow-500 to-orange-600',
    },
    {
      label: 'Defeats',
      value: losses,
      icon: '📉',
      color: 'from-red-500 to-pink-600',
    },
  ];

  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
      {statCards.map((card, index) => (
        <div
          key={index}
          className="bg-white rounded-xl shadow-md p-4 hover:shadow-lg transition-shadow"
        >
          <div className={`inline-flex items-center justify-center w-10 h-10 rounded-lg bg-gradient-to-br ${card.color} mb-2`}>
            <span className="text-xl">{card.icon}</span>
          </div>
          <div className="text-2xl font-bold text-gray-800">{card.value}</div>
          <div className="text-sm text-gray-600">{card.label}</div>
        </div>
      ))}
    </div>
  );
}
