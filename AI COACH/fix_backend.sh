#!/bin/bash
# One-command fix for backend issues

clear
echo "╔════════════════════════════════════════════════════╗"
echo "║   AI Game Coach - Backend Auto-Fixer              ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

# Determine Python command
if command -v python3 &> /dev/null; then
    PYTHON="python3"
    PIP="pip3"
elif command -v python &> /dev/null; then
    PYTHON="python"
    PIP="pip"
else
    echo "❌ ERROR: Python not found!"
    echo ""
    echo "Install Python from: https://www.python.org/downloads/"
    exit 1
fi

echo "✓ Python found: $($PYTHON --version)"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
$PIP install Flask flask-cors requests -q
echo "✓ Dependencies installed"
echo ""

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file..."
    echo "VITE_API_URL=http://localhost:5000" > .env
    echo "✓ .env created"
    echo ""
fi

# Check backend file
if [ ! -f "backend_simple.py" ]; then
    echo "❌ ERROR: backend_simple.py not found!"
    echo "Are you in the correct directory?"
    echo "Current: $(pwd)"
    exit 1
fi

echo "✓ All checks passed!"
echo ""
echo "╔════════════════════════════════════════════════════╗"
echo "║   Starting Backend Server...                      ║"
echo "║   KEEP THIS TERMINAL OPEN!                        ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

$PYTHON backend_simple.py
