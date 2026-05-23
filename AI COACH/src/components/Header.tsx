export default function Header() {
  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 bg-gradient-to-br from-indigo-600 to-purple-600 rounded-xl flex items-center justify-center">
              <span className="text-white text-xl font-bold">AI</span>
            </div>
            <div>
              <h2 className="text-xl font-bold text-gray-800">AI Game Coach</h2>
              <p className="text-xs text-gray-500">Your Personal Gaming Assistant</p>
            </div>
          </div>
          <div className="hidden md:flex items-center space-x-6">
            <a href="#" className="text-gray-600 hover:text-indigo-600 transition-colors">
              About
            </a>
            <a href="#" className="text-gray-600 hover:text-indigo-600 transition-colors">
              Games
            </a>
            <a href="#" className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-6 py-2 rounded-lg hover:shadow-lg transition-shadow">
              Get Started
            </a>
          </div>
        </div>
      </div>
    </header>
  );
}
