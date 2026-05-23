/**
 * Mock Backend Service - Works without Python backend!
 * This provides AI coaching directly in the browser
 */

import { GameStats } from '../App';

interface GameAnalysisResponse {
  success: boolean;
  game: string;
  ai_coach_feedback: string;
  stats_summary: {
    total_matches: number;
    wins: number;
    losses: number;
    win_rate: string;
  };
}

export const mockBackendService = {
  analyzeGame: async (game: string, stats: GameStats): Promise<GameAnalysisResponse> => {
    // Simulate network delay for realism
    await new Promise(resolve => setTimeout(resolve, 800));

    const winRate = stats.matches > 0 ? ((stats.wins / stats.matches) * 100).toFixed(1) : '0';
    const losses = stats.matches - stats.wins;

    const feedback = generateFeedback(game, {
      ...stats,
      win_rate: parseFloat(winRate),
      losses
    });

    return {
      success: true,
      game,
      ai_coach_feedback: feedback,
      stats_summary: {
        total_matches: stats.matches,
        wins: stats.wins,
        losses,
        win_rate: `${winRate}%`
      }
    };
  }
};

function generateFeedback(game: string, data: GameStats & { win_rate: number; losses: number }): string {
  const feedbackGenerators: Record<string, (data: GameStats & { win_rate: number; losses: number }) => string> = {
    chess: generateChessFeedback,
    pool: generatePoolFeedback,
    uno: generateUnoFeedback,
    snakes_ladders: generateSnakesFeedback,
    cricket: generateCricketFeedback,
    poker: generatePokerFeedback,
    basketball: generateBasketballFeedback,
    tennis: generateTennisFeedback,
    valorant: generateValorantFeedback,
    lol: generateLoLFeedback,
    fifa: generateFifaFeedback,
    cod: generateCodFeedback,
  };

  const generator = feedbackGenerators[game] || generateGenericFeedback;
  return generator(data);
}

// Game-specific feedback generators

function generateChessFeedback(data: GameStats & { win_rate: number; losses: number }): string {
  let feedback = `♟️ **CHESS PERFORMANCE ANALYSIS**\n\n`;
  feedback += `📊 **Your Statistics:**\n`;
  feedback += `• Total Games: ${data.matches}\n`;
  feedback += `• Wins: ${data.wins} | Losses: ${data.losses}\n`;
  feedback += `• Win Rate: ${data.win_rate}%\n`;
  feedback += `• Blunders: ${data.blunders}\n\n`;

  if (data.win_rate >= 70) {
    feedback += `🌟 **Outstanding Performance!** You're playing at an advanced level.\n\n`;
  } else if (data.win_rate >= 55) {
    feedback += `👍 **Solid Performance!** You're maintaining a strong positive record.\n\n`;
  } else if (data.win_rate >= 45) {
    feedback += `⚖️ **Balanced Record.** You're holding your own but there's room for growth.\n\n`;
  } else {
    feedback += `📚 **Development Phase.** Focus on fundamentals to improve your game.\n\n`;
  }

  // Blunders analysis
  const blunderRate = data.matches > 0 ? (data.blunders / data.matches) : 0;
  if (blunderRate > 0.3) {
    feedback += `⚠️ **Critical: High Blunder Rate**\n`;
    feedback += `You're averaging ${blunderRate.toFixed(1)} blunders per game. This is significantly impacting your results.\n\n`;
    feedback += `**Action Plan:**\n`;
    feedback += `• Take 10+ seconds before making critical moves\n`;
    feedback += `• Practice tactical puzzles daily (Chess.com, Lichess)\n`;
    feedback += `• Analyze your games to identify recurring mistakes\n`;
    feedback += `• Focus on one tactical pattern at a time\n\n`;
  } else if (blunderRate > 0.15) {
    feedback += `⚠️ **Tactical Awareness Needed**\n`;
    feedback += `Your blunder rate is moderate. Sharpening your tactics will boost your performance.\n\n`;
    feedback += `**Recommendations:**\n`;
    feedback += `• Solve 10-15 tactical puzzles daily\n`;
    feedback += `• Always check for hanging pieces before moving\n`;
    feedback += `• Learn common tactical motifs (pins, forks, skewers)\n\n`;
  } else {
    feedback += `✅ **Excellent Tactical Play**\n`;
    feedback += `Your blunder rate is low. Your tactical awareness is strong!\n\n`;
  }

  // Endgame analysis
  const endgameRate = data.matches > 0 ? (data.endgame_losses / data.matches) : 0;
  if (endgameRate > 0.3) {
    feedback += `🏁 **Endgame Weaknesses Detected**\n`;
    feedback += `You're losing ${(endgameRate * 100).toFixed(0)}% of your games in the endgame.\n\n`;
    feedback += `**Endgame Study Plan:**\n`;
    feedback += `• Master basic checkmates (King+Queen, King+Rook)\n`;
    feedback += `• Study pawn endgames (opposition, square of the pawn)\n`;
    feedback += `• Practice converting advantages (up a piece/pawn)\n`;
    feedback += `• Learn key theoretical positions\n\n`;
  }

  // Playing style analysis
  const safetyRatio = data.safe_moves + data.risky_moves > 0 
    ? data.safe_moves / (data.safe_moves + data.risky_moves) 
    : 0.5;

  if (safetyRatio > 0.7) {
    feedback += `🛡️ **Playing Style: Defensive/Positional**\n`;
    feedback += `You favor safe, solid moves. This is good for consistency!\n\n`;
    feedback += `**Growth Tip:** Occasionally seize tactical opportunities to keep opponents under pressure.\n\n`;
  } else if (safetyRatio < 0.3) {
    feedback += `⚔️ **Playing Style: Aggressive/Tactical**\n`;
    feedback += `You take calculated risks. This can lead to brilliant victories!\n\n`;
    feedback += `**Growth Tip:** Balance aggression with solid positional play to avoid overextending.\n\n`;
  } else {
    feedback += `⚖️ **Playing Style: Balanced**\n`;
    feedback += `Great mix of solid play and tactical sharpness!\n\n`;
  }

  feedback += `💡 **Key Takeaway:**\n`;
  if (data.win_rate < 50) {
    feedback += `Focus on reducing blunders and strengthening your endgame. These two areas alone can boost your win rate by 15-20%!`;
  } else if (data.win_rate < 60) {
    feedback += `You're doing well! To reach the next level, deepen your opening preparation and study master games in your favorite openings.`;
  } else {
    feedback += `Excellent play! Continue refining your strategy and consider studying grandmaster games to add new ideas to your repertoire.`;
  }

  return feedback;
}

function generatePoolFeedback(data: GameStats & { win_rate: number }): string {
  let feedback = `🎱 **POOL PERFORMANCE ANALYSIS**\n\n`;
  feedback += `📊 **Your Statistics:**\n`;
  feedback += `• Total Games: ${data.matches}\n`;
  feedback += `• Win Rate: ${data.win_rate}%\n\n`;

  if (data.win_rate >= 60) {
    feedback += `🏆 **Strong Performance!** You're demonstrating excellent cue control.\n\n`;
  } else if (data.win_rate >= 45) {
    feedback += `👍 **Competitive Play!** You're holding your own at the table.\n\n`;
  } else {
    feedback += `📚 **Building Your Skills.** Focus on fundamentals and practice will pay off.\n\n`;
  }

  const breakSuccess = data.safe_moves;
  const fouls = data.blunders;

  if (breakSuccess < data.matches * 0.4) {
    feedback += `🎯 **Break Shot Needs Work**\n`;
    feedback += `Your break success rate is low. A strong break gives you table control.\n\n`;
    feedback += `**Break Practice Drills:**\n`;
    feedback += `• Practice consistent cue ball positioning\n`;
    feedback += `• Work on power control (not always maximum power)\n`;
    feedback += `• Find the sweet spot on the rack\n`;
    feedback += `• Film yourself to check technique\n\n`;
  }

  if (fouls > data.matches * 0.15) {
    feedback += `⚠️ **Foul Management**\n`;
    feedback += `Reduce unforced errors to maintain momentum.\n\n`;
    feedback += `**Clean Play Tips:**\n`;
    feedback += `• Take your time lining up shots\n`;
    feedback += `• Visualize the shot path before shooting\n`;
    feedback += `• Practice bridge stability\n`;
    feedback += `• Be mindful of the cue ball path\n\n`;
  }

  feedback += `💡 **Pro Tips:**\n`;
  feedback += `• Focus on position play, not just pocketing balls\n`;
  feedback += `• Master safety shots for tactical advantages\n`;
  feedback += `• Practice different types of english/spin\n`;
  feedback += `• Study patterns and leave yourself easy next shots`;

  return feedback;
}

function generateUnoFeedback(data: GameStats & { win_rate: number }): string {
  let feedback = `🃏 **UNO PERFORMANCE ANALYSIS**\n\n`;
  feedback += `📊 Win Rate: ${data.win_rate}%\n\n`;

  if (data.win_rate >= 60) {
    feedback += `🎉 Excellent! You're mastering the art of Uno!\n\n`;
  } else if (data.win_rate >= 45) {
    feedback += `👍 Good play! You understand the game dynamics.\n\n`;
  } else {
    feedback += `📚 Keep practicing! Strategy makes a big difference in Uno.\n\n`;
  }

  feedback += `**Winning Strategies:**\n\n`;
  feedback += `🎴 **Wild Card Timing:**\n`;
  feedback += `• Save wild cards for crucial moments\n`;
  feedback += `• Use them to change momentum or block opponents\n`;
  feedback += `• Don't waste them early in the game\n\n`;

  feedback += `👁️ **Card Tracking:**\n`;
  feedback += `• Watch what colors opponents pick up\n`;
  feedback += `• Notice who's close to winning (1-2 cards left)\n`;
  feedback += `• Target the leader with action cards\n\n`;

  feedback += `⚡ **Action Card Strategy:**\n`;
  feedback += `• Skip/Reverse to maintain turn control\n`;
  feedback += `• Draw Two on players with few cards\n`;
  feedback += `• Stack action cards for maximum impact\n\n`;

  feedback += `💡 **Pro Tip:** When you have one card left, make sure it's playable on multiple colors!`;

  return feedback;
}

function generateSnakesFeedback(data: GameStats & { win_rate: number }): string {
  return `🎲 **SNAKES & LADDERS ANALYSIS**\n\n📊 Win Rate: ${data.win_rate}%\n\n🎲 This is primarily a game of chance! Your win rate reflects the luck of the dice.\n\n✨ **Remember:** The fun is in the journey, not just winning!\n\n💡 **Enjoy the game:** Stay positive, have fun with friends, and may the dice be ever in your favor!`;
}

function generateCricketFeedback(data: GameStats & { win_rate: number }): string {
  let feedback = `🏏 **CRICKET PERFORMANCE ANALYSIS**\n\n`;
  feedback += `📊 Win Rate: ${data.win_rate}%\n\n`;

  if (data.win_rate >= 60) {
    feedback += `🏆 Outstanding! You're in excellent form!\n\n`;
  } else if (data.win_rate >= 45) {
    feedback += `👍 Solid performance! Keep working on consistency.\n\n`;
  } else {
    feedback += `📚 Focus on technique fundamentals.\n\n`;
  }

  const riskBalance = data.safe_moves > data.risky_moves;

  feedback += `**Batting Analysis:**\n\n`;
  
  if (!riskBalance) {
    feedback += `⚠️ **Shot Selection:**\n`;
    feedback += `You're taking too many risks. Balance aggression with defensive technique.\n\n`;
    feedback += `• Play the merit of each ball\n`;
    feedback += `• Build your innings before accelerating\n`;
    feedback += `• Leave balls outside off-stump early\n\n`;
  }

  feedback += `**Key Skills to Practice:**\n\n`;
  feedback += `🎯 **Timing:** Focus on meeting the ball at the right moment\n`;
  feedback += `👣 **Footwork:** Get to the pitch of the ball\n`;
  feedback += `👁️ **Watching the Ball:** Track it from bowler's hand to bat\n`;
  feedback += `🎪 **Shot Selection:** Choose the right shot for each delivery\n\n`;

  feedback += `💡 **Pro Tip:** The best batsmen build partnerships. Rotate strike and communicate with your partner!`;

  return feedback;
}

function generatePokerFeedback(data: GameStats & { win_rate: number }): string {
  let feedback = `♠️ **POKER PERFORMANCE ANALYSIS**\n\n`;
  feedback += `📊 Win Rate: ${data.win_rate}%\n\n`;

  if (data.win_rate >= 55) {
    feedback += `🏆 Excellent! You're a profitable player!\n\n`;
  } else if (data.win_rate >= 45) {
    feedback += `⚖️ Breaking even. Small adjustments can push you into profit.\n\n`;
  } else {
    feedback += `📚 Study fundamental strategy to improve your edge.\n\n`;
  }

  const blunderRate = data.blunders / data.matches;
  if (blunderRate > 0.2) {
    feedback += `⚠️ **Critical Mistakes:**\n`;
    feedback += `You're making costly errors. Focus on decision quality over speed.\n\n`;
    feedback += `**Reduce Mistakes:**\n`;
    feedback += `• Study pot odds and expected value\n`;
    feedback += `• Don't chase draws without proper odds\n`;
    feedback += `• Avoid emotional play after bad beats\n`;
    feedback += `• Take notes on opponents\n\n`;
  }

  feedback += `**Essential Poker Skills:**\n\n`;
  feedback += `📍 **Position Play:**\n`;
  feedback += `• Play more hands in late position\n`;
  feedback += `• Be tighter early position\n`;
  feedback += `• Use position to gain information\n\n`;

  feedback += `🎭 **Hand Reading:**\n`;
  feedback += `• Observe betting patterns\n`;
  feedback += `• Put opponents on ranges, not specific hands\n`;
  feedback += `• Adjust based on player types (tight/loose)\n\n`;

  feedback += `💰 **Bankroll Management:**\n`;
  feedback += `• Never risk more than 5% on one game\n`;
  feedback += `• Play at stakes you can afford\n`;
  feedback += `• Move down if you're losing\n\n`;

  feedback += `💡 **Key Principle:** Patience and discipline win in the long run. Don't play every hand!`;

  return feedback;
}

function generateBasketballFeedback(data: GameStats & { win_rate: number }): string {
  let feedback = `🏀 **BASKETBALL PERFORMANCE ANALYSIS**\n\n`;
  feedback += `📊 Win Rate: ${data.win_rate}%\n\n`;

  if (data.win_rate >= 60) {
    feedback += `🏆 Dominant performance! You're in championship form!\n\n`;
  } else if (data.win_rate >= 45) {
    feedback += `👍 Competitive play! Consistency will elevate your game.\n\n`;
  } else {
    feedback += `📚 Focus on fundamentals to build a stronger foundation.\n\n`;
  }

  feedback += `**Skills Development:**\n\n`;
  feedback += `🎯 **Shooting:**\n`;
  feedback += `• Practice form shooting daily\n`;
  feedback += `• Develop a consistent pre-shot routine\n`;
  feedback += `• Work on shooting off the dribble\n`;
  feedback += `• Practice free throws when tired\n\n`;

  feedback += `🏃 **Ball Handling:**\n`;
  feedback += `• Dribble with both hands equally\n`;
  feedback += `• Keep your head up while dribbling\n`;
  feedback += `• Practice change of pace moves\n`;
  feedback += `• Work on protecting the ball under pressure\n\n`;

  feedback += `🛡️ **Defense:**\n`;
  feedback += `• Stay in defensive stance\n`;
  feedback += `• Move your feet, don't reach\n`;
  feedback += `• Communicate with teammates\n`;
  feedback += `• Box out on every shot\n\n`;

  feedback += `💡 **Pro Tip:** Basketball is a team game. Great passers make everyone better!`;

  return feedback;
}

function generateTennisFeedback(data: GameStats & { win_rate: number }): string {
  let feedback = `🎾 **TENNIS PERFORMANCE ANALYSIS**\n\n`;
  feedback += `📊 Win Rate: ${data.win_rate}%\n\n`;

  if (data.win_rate >= 60) {
    feedback += `🏆 Outstanding! You're playing at a high level!\n\n`;
  } else if (data.win_rate >= 45) {
    feedback += `👍 Solid game! Work on consistency for better results.\n\n`;
  } else {
    feedback += `📚 Focus on technique and court positioning.\n\n`;
  }

  feedback += `**Technical Excellence:**\n\n`;
  feedback += `🎯 **Serve:**\n`;
  feedback += `• Develop a reliable first serve\n`;
  feedback += `• Place serves to opponent's weakness\n`;
  feedback += `• Practice serve variations (flat, slice, kick)\n`;
  feedback += `• Build a consistent ball toss\n\n`;

  feedback += `⚡ **Groundstrokes:**\n`;
  feedback += `• Master both forehand and backhand\n`;
  feedback += `• Hit with topspin for consistency\n`;
  feedback += `• Practice footwork and positioning\n`;
  feedback += `• Learn to hit on the rise\n\n`;

  feedback += `🎪 **Strategy:**\n`;
  feedback += `• Control the center of the court\n`;
  feedback += `• Mix up pace and spin\n`;
  feedback += `• Exploit opponent weaknesses\n`;
  feedback += `• Stay patient in rallies\n\n`;

  feedback += `💡 **Mental Game:** Stay focused point by point. Don't dwell on mistakes!`;

  return feedback;
}

function generateValorantFeedback(data: GameStats & { win_rate: number }): string {
  let feedback = `🎮 **VALORANT PERFORMANCE ANALYSIS**\n\n`;
  feedback += `📊 Win Rate: ${data.win_rate}%\n\n`;

  if (data.win_rate >= 55) {
    feedback += `🏆 Excellent! You're climbing the ranks!\n\n`;
  } else if (data.win_rate >= 45) {
    feedback += `⚖️ Room for improvement. Small refinements will boost your rank.\n\n`;
  } else {
    feedback += `📚 Focus on game sense and aim training.\n\n`;
  }

  const errorRate = data.blunders / data.matches;
  if (errorRate > 0.3) {
    feedback += `⚠️ **High Death Rate:**\n`;
    feedback += `You're making positioning errors. Play for your life!\n\n`;
    feedback += `• Check corners before peeking\n`;
    feedback += `• Don't over-peek\n`;
    feedback += `• Play off your teammates\n`;
    feedback += `• Use utility before entering sites\n\n`;
  }

  feedback += `**Core Skills:**\n\n`;
  feedback += `🎯 **Aim:**\n`;
  feedback += `• Practice in aim trainers daily (15-30 min)\n`;
  feedback += `• Deathmatch before ranked games\n`;
  feedback += `• Crosshair placement at head level\n`;
  feedback += `• Learn spray patterns for your weapons\n\n`;

  feedback += `🧠 **Game Sense:**\n`;
  feedback += `• Learn common angles and positions\n`;
  feedback += `• Listen to audio cues\n`;
  feedback += `• Communicate with team\n`;
  feedback += `• Understand economy system\n\n`;

  feedback += `⚡ **Agent Mastery:**\n`;
  feedback += `• Master 2-3 agents deeply\n`;
  feedback += `• Learn lineups for your agent\n`;
  feedback += `• Coordinate abilities with team\n`;
  feedback += `• Know when to use ultimates\n\n`;

  feedback += `💡 **Rank Up Tip:** Consistency beats flashy plays. Focus on winning rounds, not highlight reels!`;

  return feedback;
}

function generateLoLFeedback(data: GameStats & { win_rate: number }): string {
  let feedback = `⚔️ **LEAGUE OF LEGENDS ANALYSIS**\n\n`;
  feedback += `📊 Win Rate: ${data.win_rate}%\n\n`;

  if (data.win_rate >= 55) {
    feedback += `🏆 Great performance! You're climbing ELO!\n\n`;
  } else if (data.win_rate >= 45) {
    feedback += `⚖️ Hovering around 50%. Focus on macro play for improvement.\n\n`;
  } else {
    feedback += `📚 Study fundamentals. Every game is a learning opportunity.\n\n`;
  }

  feedback += `**Path to Improvement:**\n\n`;
  feedback += `🎯 **CS and Gold:**\n`;
  feedback += `• Aim for 7+ CS per minute\n`;
  feedback += `• Don't miss CS under tower\n`;
  feedback += `• Practice last-hitting in practice tool\n`;
  feedback += `• Balance farming with map pressure\n\n`;

  feedback += `🗺️ **Map Awareness:**\n`;
  feedback += `• Check minimap every 3-5 seconds\n`;
  feedback += `• Ward key areas (river, jungle)\n`;
  feedback += `• Track enemy jungler\n`;
  feedback += `• Ping MIA immediately\n\n`;

  feedback += `🎭 **Champion Mastery:**\n`;
  feedback += `• Focus on 2-3 champions\n`;
  feedback += `• Learn matchups deeply\n`;
  feedback += `• Know power spikes\n`;
  feedback += `• Practice combos in practice tool\n\n`;

  feedback += `🧠 **Macro Strategy:**\n`;
  feedback += `• Understand win conditions\n`;
  feedback += `• Take objectives after kills\n`;
  feedback += `• Know when to group vs split\n`;
  feedback += `• Don't chase kills, push advantages\n\n`;

  feedback += `💡 **Climb Faster:** Focus on YOUR play, not blaming teammates. You can only improve yourself!`;

  return feedback;
}

function generateFifaFeedback(data: GameStats & { win_rate: number }): string {
  let feedback = `⚽ **FIFA PERFORMANCE ANALYSIS**\n\n`;
  feedback += `📊 Win Rate: ${data.win_rate}%\n\n`;

  if (data.win_rate >= 60) {
    feedback += `🏆 Elite level! You're dominating matches!\n\n`;
  } else if (data.win_rate >= 45) {
    feedback += `👍 Competitive! Refine your tactics for better results.\n\n`;
  } else {
    feedback += `📚 Practice will improve your game awareness.\n\n`;
  }

  feedback += `**Gameplay Mastery:**\n\n`;
  feedback += `⚽ **Attacking:**\n`;
  feedback += `• Use driven passes for speed\n`;
  feedback += `• Practice timed finishing\n`;
  feedback += `• Learn effective skill moves (2-3 max)\n`;
  feedback += `• Make runs with L1/LB\n`;
  feedback += `• Play possession to create space\n\n`;

  feedback += `🛡️ **Defending:**\n`;
  feedback += `• Jockey instead of rushing tackles\n`;
  feedback += `• Use contain (A/X button)\n`;
  feedback += `• Cut passing lanes\n`;
  feedback += `• Don't pull CBs out of position\n`;
  feedback += `• Track opponent's runs\n\n`;

  feedback += `🎮 **Meta Tactics:**\n`;
  feedback += `• Master your formation\n`;
  feedback += `• Adjust tactics based on game state\n`;
  feedback += `• Use player instructions effectively\n`;
  feedback += `• Learn set piece routines\n\n`;

  feedback += `💡 **Pro Tip:** Patience in build-up beats pace abuse. Control the tempo!`;

  return feedback;
}

function generateCodFeedback(data: GameStats & { win_rate: number }): string {
  let feedback = `🎯 **CALL OF DUTY ANALYSIS**\n\n`;
  feedback += `📊 Win Rate: ${data.win_rate}%\n\n`;

  if (data.win_rate >= 55) {
    feedback += `🏆 Strong performance! You're fragging out!\n\n`;
  } else if (data.win_rate >= 45) {
    feedback += `⚖️ Decent stats. Sharpen your gun skill for better K/D.\n\n`;
  } else {
    feedback += `📚 Focus on positioning and map knowledge.\n\n`;
  }

  const deathRate = data.blunders / data.matches;
  if (deathRate > 0.3) {
    feedback += `⚠️ **High Death Rate:**\n`;
    feedback += `You're being too aggressive. Play smarter, not harder.\n\n`;
    feedback += `• Pre-aim common spots\n`;
    feedback += `• Don't sprint around corners\n`;
    feedback += `• Use cover effectively\n`;
    feedback += `• Know when to disengage\n\n`;
  }

  feedback += `**Improvement Areas:**\n\n`;
  feedback += `🎯 **Aim Training:**\n`;
  feedback += `• Practice in private matches daily\n`;
  feedback += `• Find your optimal sensitivity\n`;
  feedback += `• Learn recoil patterns\n`;
  feedback += `• Aim for upper chest/head\n\n`;

  feedback += `🗺️ **Map Control:**\n`;
  feedback += `• Learn spawns and rotations\n`;
  feedback += `• Hold power positions\n`;
  feedback += `• Control high-traffic areas\n`;
  feedback += `• Use equipment strategically\n\n`;

  feedback += `⚡ **Loadout:**\n`;
  feedback += `• Find a gun that fits your playstyle\n`;
  feedback += `• Optimize attachments for your needs\n`;
  feedback += `• Balance perks for advantage\n`;
  feedback += `• Have different classes for modes\n\n`;

  feedback += `💡 **Win More:** Stick with your team in objective modes. Lone wolves don't win!`;

  return feedback;
}

function generateGenericFeedback(data: GameStats & { win_rate: number }): string {
  let feedback = `🎮 **GAME PERFORMANCE ANALYSIS**\n\n`;
  feedback += `📊 Win Rate: ${data.win_rate}%\n\n`;

  if (data.win_rate >= 60) {
    feedback += `🏆 Excellent performance! You're playing at a high level!\n\n`;
  } else if (data.win_rate >= 45) {
    feedback += `👍 Solid performance! Keep practicing for improvement.\n\n`;
  } else {
    feedback += `📚 Focus on fundamentals. Every match is a learning opportunity!\n\n`;
  }

  feedback += `**General Improvement Tips:**\n\n`;
  feedback += `• Practice regularly to build muscle memory\n`;
  feedback += `• Study advanced strategies and techniques\n`;
  feedback += `• Learn from better players\n`;
  feedback += `• Analyze your mistakes\n`;
  feedback += `• Stay patient and positive\n\n`;

  feedback += `💡 **Remember:** Improvement takes time. Focus on consistent practice and learning!`;

  return feedback;
}
