@echo off
echo ====================================
echo Quiz App - Startup Script
echo ====================================
echo.
echo Starting Backend (FastAPI)...
echo.

cd backend
pip install -r requirements.txt
start "Quiz App Backend" cmd /k "python main.py"

echo.
echo Waiting for backend to start...
timeout /t 3

echo.
echo Starting Frontend (React + Vite)...
echo.

cd ..\frontend
npm install
start "Quiz App Frontend" cmd /k "npm run dev"

echo.
echo ====================================
echo Both servers should now be running!
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
echo ====================================
pause
