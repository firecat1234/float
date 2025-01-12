#!/bin/bash

# Check if curl is installed
if ! command -v curl &> /dev/null
then
    echo "curl not found. Please install curl to proceed."
    exit 1
fi

# Check for nvm and install Node.js if necessary
if ! command -v nvm &> /dev/null
then
    echo "nvm not found. Installing nvm..."
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
    source ~/.bashrc
fi

# Install Node.js and npm using nvm
if ! command -v node &> /dev/null
then
    echo "Node.js not found. Installing latest LTS version..."
    nvm install --lts
fi

# Check and create virtual environment
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    if ! .venv/bin/pip install --upgrade pip; then
        echo "Failed to upgrade pip. Exiting."
        exit 1
    fi
    if ! .venv/bin/pip install -r backend/requirements.txt; then
        echo "Failed to install backend requirements. Exiting."
        exit 1
    fi
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
