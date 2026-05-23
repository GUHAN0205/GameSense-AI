#!/bin/bash

# AI Game Coach - Backend Startup Script
# This script helps you start the backend easily

echo "🚀 AI Game Coach - Backend Startup"
echo "=================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    if ! command -v python &> /dev/null
    then
        echo "❌ Python is not installed!"
        echo "Please install Python 3.8+ from https://www.python.org/"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "✅ Found Python: $PYTHON_CMD"

# Check Python version
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
echo "✅ Python version: $PYTHON_VERSION"
echo ""

# Check if Flask is installed
if ! $PYTHON_CMD -c "import flask" &> /dev/null
then
    echo "⚠️  Flask not found. Installing dependencies..."
    $PYTHON_CMD -m pip install -r requirements.txt
    echo ""
fi

# Ask which backend to use
echo "Which backend would you like to start?"
echo ""
echo "1) Simple Backend (Recommended - works without coach_agent.py)"
echo "2) Enhanced Backend (Requires coach_agent.py)"
echo ""
read -p "Enter choice [1 or 2]: " choice

case $choice in
    1)
        echo ""
        echo "🚀 Starting Simple Backend..."
        echo ""
        $PYTHON_CMD backend_simple.py
        ;;
    2)
        if [ -f "coach_agent.py" ]; then
            echo ""
            echo "🚀 Starting Enhanced Backend..."
            echo ""
            $PYTHON_CMD backend_enhanced.py
        else
            echo ""
            echo "⚠️  coach_agent.py not found!"
            echo "Creating from mock..."
            cp coach_agent_mock.py coach_agent.py
            echo "✅ Created coach_agent.py"
            echo ""
            echo "🚀 Starting Enhanced Backend..."
            echo ""
            $PYTHON_CMD backend_enhanced.py
        fi
        ;;
    *)
        echo "Invalid choice. Starting Simple Backend..."
        $PYTHON_CMD backend_simple.py
        ;;
esac
