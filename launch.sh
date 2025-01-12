#!/bin/bash

# Load nvm if available
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# Check if nvm is installed
if ! command -v nvm &> /dev/null; then
    echo "nvm not found. Installing nvm..."
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
    source ~/.bashrc
fi

# Install Node.js and npm using nvm
if ! command -v node &> /dev/null; then
    echo "Node.js not found. Installing latest LTS version..."
    nvm install --lts
fi

# Check and create virtual environment
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r backend/requirements.txt
else
    source .venv/bin/activate
fi

# Start backend server
echo "Starting backend server..."
cd backend
uvicorn app.main:app --reload &> ../backend.log &
cd ..

# Start frontend server if available
if [ -d "frontend" ]; then
    echo "Starting frontend development server..."
    cd frontend
    if [ -f "package.json" ]; then
        npm install
        npm run dev &> ../frontend.log &
    else
        echo "Error: package.json not found in frontend directory. Skipping frontend setup."
    fi
    cd ..
fi

echo "Backend running on http://localhost:8000"
echo "Frontend running on http://localhost:5173 (if applicable)"
