#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Run the app
uvicorn app.main:app --reload

#mac/linux