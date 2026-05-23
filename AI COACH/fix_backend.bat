@echo off
REM One-command fix for backend issues

cls
echo.
echo ====================================================
echo    AI Game Coach - Backend Auto-Fixer
echo ====================================================
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    echo.
    echo Install Python from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python found
python --version
echo.

REM Install dependencies
echo Installing dependencies...
pip install Flask flask-cors requests >nul 2>&1
echo Dependencies installed
echo.

REM Check .env
if not exist .env (
    echo Creating .env file...
    echo VITE_API_URL=http://localhost:5000 > .env
    echo .env created
    echo.
)

REM Check backend file
if not exist backend_simple.py (
    echo ERROR: backend_simple.py not found!
    echo Are you in the correct directory?
    echo Current: %CD%
    pause
    exit /b 1
)

echo All checks passed!
echo.
echo ====================================================
echo    Starting Backend Server...
echo    KEEP THIS WINDOW OPEN!
echo ====================================================
echo.

python backend_simple.py
pause
