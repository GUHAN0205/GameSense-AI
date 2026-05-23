interface FeedbackDisplayProps {
  feedback: string;
  error: string;
  isLoading: boolean;
  selectedGame: string;
}

export default function FeedbackDisplay({ feedback, error, isLoading, selectedGame }: FeedbackDisplayProps) {
  if (!selectedGame) {
    return (
      <div className="bg-white rounded-2xl shadow-xl p-8 h-full flex items-center justify-center">
        <div className="text-center">
          <div className="text-6xl mb-4">🎮</div>
          <h3 className="text-xl font-semibold text-gray-700 mb-2">
            Ready to Level Up?
          </h3>
          <p className="text-gray-500">
            Select a game and enter your stats to get personalized AI coaching
          </p>
        </div>
      </div>
    );
  }

  if (isLoading) {
    return (
      <div className="bg-white rounded-2xl shadow-xl p-8 h-full">
        <div className="flex flex-col items-center justify-center h-full">
          <div className="relative w-24 h-24 mb-6">
            <div className="absolute inset-0 border-4 border-indigo-200 rounded-full"></div>
            <div className="absolute inset-0 border-4 border-indigo-600 rounded-full border-t-transparent animate-spin"></div>
          </div>
          <h3 className="text-xl font-semibold text-gray-700 mb-2">
            Analyzing Your Performance
          </h3>
          <p className="text-gray-500 text-center">
            Our AI coach is reviewing your stats...
          </p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-white rounded-2xl shadow-xl p-8">
        <div className="bg-red-50 border-2 border-red-200 rounded-xl p-6">
          <div className="flex items-start">
            <span className="text-3xl mr-4">⚠️</span>
            <div>
              <h3 className="text-lg font-semibold text-red-800 mb-2">
                Error Getting Feedback
              </h3>
              <p className="text-red-600 mb-4">{error}</p>
              <p className="text-sm text-red-500">
                Please make sure the backend server is running and try again.
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (feedback) {
    return (
      <div className="bg-white rounded-2xl shadow-xl p-8">
        <div className="flex items-center mb-6">
          <div className="w-12 h-12 bg-gradient-to-br from-indigo-600 to-purple-600 rounded-xl flex items-center justify-center mr-4">
            <span className="text-white text-2xl">🤖</span>
          </div>
          <div>
            <h2 className="text-2xl font-bold text-gray-800">AI Coach Feedback</h2>
            <p className="text-gray-600">Personalized insights for you</p>
          </div>
        </div>

        <div className="bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50 rounded-xl p-6 mb-6">
          <div className="prose prose-lg max-w-none">
            {feedback.split('\n').map((line, index) => {
              const trimmedLine = line.trim();
              if (!trimmedLine) return null;
              
              // Format bold text (markdown-style **text**)
              const formattedLine = trimmedLine.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
              
              // Check if it's a heading (starts with emoji or special characters)
              const isHeading = /^[♟️🎱🃏🎲🏏♠️🏀🎾🎮⚔️⚽🎯📊🌟👍📚⚠️✅🎯⚖️🏆🛡️⚡🎪💡🎴👁️🏁🗺️🎭💰📍🧠]/.test(trimmedLine);
              
              if (isHeading) {
                return (
                  <h3 
                    key={index} 
                    className="text-lg font-bold text-gray-800 mt-4 mb-2 first:mt-0"
                    dangerouslySetInnerHTML={{ __html: formattedLine }}
                  />
                );
              }
              
              // Check if it's a bullet point
              if (trimmedLine.startsWith('•') || trimmedLine.startsWith('-')) {
                return (
                  <li 
                    key={index} 
                    className="text-gray-700 ml-4 mb-1"
                    dangerouslySetInnerHTML={{ __html: formattedLine.substring(1) }}
                  />
                );
              }
              
              // Regular paragraph
              return (
                <p 
                  key={index} 
                  className="text-gray-700 leading-relaxed mb-3"
                  dangerouslySetInnerHTML={{ __html: formattedLine }}
                />
              );
            })}
          </div>
        </div>

        <div className="flex items-start p-4 bg-blue-50 rounded-lg border border-blue-200">
          <span className="text-2xl mr-3">💡</span>
          <div>
            <h4 className="font-semibold text-blue-900 mb-1">Pro Tip</h4>
            <p className="text-sm text-blue-700">
              Track your progress over time by keeping a record of your stats and comparing AI feedback from different sessions.
            </p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-2xl shadow-xl p-8 h-full flex items-center justify-center">
      <div className="text-center">
        <div className="text-6xl mb-4">📊</div>
        <h3 className="text-xl font-semibold text-gray-700 mb-2">
          Enter Your Stats
        </h3>
        <p className="text-gray-500">
          Fill in your game statistics and click "Get AI Coaching" to receive personalized feedback
        </p>
      </div>
    </div>
  );
}
