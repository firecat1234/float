# Variables
ENV=.venv

# Targets
setup:
	python3 -m venv $(ENV)
	$(ENV)/bin/pip install -r requirements.txt

run:
	$(ENV)/bin/uvicorn app.main:app --reload

test:
	$(ENV)/bin/pytest tests/

clean:
	rm -rf $(ENV)
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete


### we probably use this for deployment, or docker. over launch. 

#make setup   # Sets up the environment
#make run     # Launches the app
#make test    # Runs the test suite
#make clean   # Cleans up build artifacts
