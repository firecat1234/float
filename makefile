# Variables
ENV=.venv
FRONTEND_DIR=frontend

# Targets
setup:
	# Set up backend environment
	python3 -m venv $(ENV)
	$(ENV)/bin/pip install -r requirements-backend.txt
	# Set up frontend environment
	cd $(FRONTEND_DIR) && npm install

run:
	# Run backend
	$(ENV)/bin/uvicorn app.main:app --reload

build:
	# Build frontend
	cd $(FRONTEND_DIR) && npm run build

start:
	# Run frontend and backend
	make -j2 run run-frontend

run-frontend:
	# Run frontend
	cd $(FRONTEND_DIR) && npm run dev

clean:
	# Clean backend and frontend artifacts
	rm -rf $(ENV)
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	cd $(FRONTEND_DIR) && rm -rf node_modules dist

test:
	# Run tests for backend
	$(ENV)/bin/pytest tests/

all:
	# Full setup and run
	make setup && make start

#make setup   # Sets up the environment
#make run     # Launches the app
#make build   # Builds frontend assets
#make start   # Runs both backend and frontend
#make clean   # Cleans up build artifacts
