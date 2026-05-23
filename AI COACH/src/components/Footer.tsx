export default function Footer() {
  return (
    <footer className="bg-white border-t border-gray-200 mt-16">
      <div className="container mx-auto px-4 py-8">
        <div className="flex flex-col md:flex-row justify-between items-center">
          <div className="mb-4 md:mb-0">
            <p className="text-gray-600">
              © 2024 AI Game Coach. Powered by Advanced AI Technology
            </p>
          </div>
          <div className="flex space-x-6">
            <a href="#" className="text-gray-600 hover:text-indigo-600 transition-colors">
              Privacy
            </a>
            <a href="#" className="text-gray-600 hover:text-indigo-600 transition-colors">
              Terms
            </a>
            <a href="#" className="text-gray-600 hover:text-indigo-600 transition-colors">
              Support
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
}
