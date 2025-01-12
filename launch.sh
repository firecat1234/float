#!/bin/bash

# Check and create virtual environment
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    .venv/bin/pip install --upgrade pip
    .venv/bin/pip install -r backend/requirements.txt
fi

# Activate the virtual environment
source .venv/bin/activate

# Run the backend server
uvicorn app.main:app --reload

# Optional: Add logic to start the frontend
if [ -d "frontend" ]; then
    echo "Starting frontend development server..."
    cd frontend
    npm install
    npm run dev &
    cd ..
fi

# Inform the user
echo "Backend running on http://localhost:8000"
echo "Frontend running on http://localhost:5173 (if applicable)"
