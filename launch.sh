#!/bin/bash

# Default ports
BACKEND_PORT=8000
FRONTEND_PORT=5173

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --backend-port) BACKEND_PORT="$2"; shift ;;
        --frontend-port) FRONTEND_PORT="$2"; shift ;;
        *) echo "Unknown parameter: $1"; exit 1 ;;
    esac
    shift
done

# Function to print messages
print_message() {
    echo -e "\n[INFO] $1\n"
}

# Load nvm if available
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# Install nvm if not installed
if ! command -v nvm &> /dev/null; then
    print_message "nvm not found. Installing nvm..."
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
    source ~/.bashrc
fi

# Install Node.js and npm using nvm if not available
if ! command -v node &> /dev/null; then
    print_message "Node.js not found. Installing latest LTS version..."
    nvm install --lts
fi

# Check and create Python virtual environment
if [ ! -d ".venv" ]; then
    print_message "Creating Python virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r backend/requirements.txt
else
    print_message "Activating Python virtual environment..."
    source .venv/bin/activate
fi

# Kill existing backend or frontend processes
print_message "Killing existing backend and frontend processes (if any)..."
pkill -f "uvicorn app.main:app" || true
pkill -f "vite" || true

# Start backend server with custom port
print_message "Starting backend server on port $BACKEND_PORT..."
cd backend
if uvicorn app.main:app --reload --host 0.0.0.0 --port $BACKEND_PORT &> ../backend.log & then
    print_message "Backend is running on port $BACKEND_PORT. Logs: backend.log"
else
    print_message "Failed to start backend. Check backend.log for details."
    exit 1
fi
cd ..

# Start frontend server with custom port
if [ -d "frontend" ]; then
    print_message "Starting frontend development server on port $FRONTEND_PORT..."
    cd frontend
    if [ -f "package.json" ]; then
        npm install
        if VITE_PORT=$FRONTEND_PORT npm run dev &> ../frontend.log & then
            print_message "Frontend is running on port $FRONTEND_PORT. Logs: frontend.log"
        else
            print_message "Failed to start frontend. Check frontend.log for details."
        fi
    else
        print_message "Error: package.json not found in frontend directory. Skipping frontend setup."
    fi
    cd ..
else
    print_message "Frontend directory not found. Skipping frontend setup."
fi

# Final status messages
print_message "Backend running on http://localhost:$BACKEND_PORT"
print_message "Frontend running on http://localhost:$FRONTEND_PORT (if applicable)"

