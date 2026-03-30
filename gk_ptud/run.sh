#!/bin/bash

echo "===================================="
echo "Quiz App - Startup Script"
echo "===================================="
echo ""
echo "Starting Backend (FastAPI)..."
echo ""

cd backend
pip install -r requirements.txt
python main.py &
BACKEND_PID=$!

echo ""
echo "Waiting for backend to start..."
sleep 3

echo ""
echo "Starting Frontend (React + Vite)..."
echo ""

cd ../frontend
npm install
npm run dev &
FRONTEND_PID=$!

echo ""
echo "===================================="
echo "Both servers are running!"
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:5173"
echo "===================================="
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for both processes
wait
