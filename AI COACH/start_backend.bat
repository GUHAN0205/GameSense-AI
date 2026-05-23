@echo off
REM AI Game Coach - Backend Startup Script for Windows

echo.
echo ================================
echo AI Game Coach - Backend Startup
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed!
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo Found Python
python --version
echo.

REM Check if Flask is installed
python -c "import flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo Flask not found. Installing dependencies...
    python -m pip install -r requirements.txt
    echo.
)

REM Ask which backend to use
echo Which backend would you like to start?
echo.
echo 1) Simple Backend (Recommended - works without coach_agent.py)
echo 2) Enhanced Backend (Requires coach_agent.py)
echo.

set /p choice="Enter choice [1 or 2]: "

if "%choice%"=="1" (
    echo.
    echo Starting Simple Backend...
    echo.
    python backend_simple.py
) else if "%choice%"=="2" (
    if exist coach_agent.py (
        echo.
        echo Starting Enhanced Backend...
        echo.
        python backend_enhanced.py
    ) else (
        echo.
        echo coach_agent.py not found!
        echo Creating from mock...
        copy coach_agent_mock.py coach_agent.py
        echo Created coach_agent.py
        echo.
        echo Starting Enhanced Backend...
        echo.
        python backend_enhanced.py
    )
) else (
    echo Invalid choice. Starting Simple Backend...
    python backend_simple.py
)

pause
