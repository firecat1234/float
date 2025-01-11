:: Activate the virtual environment
call .venv\Scripts\activate

:: Run the app
uvicorn app.main:app --reload
