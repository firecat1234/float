# Environment Setup Guide

This document outlines the steps to set up the environment for the Float project, covering both backend and frontend components.

---

## Prerequisites

- **Python 3.8+** installed.
- **Node.js 16+** with npm.
- Redis (for Celery backend).
- PostgreSQL (if using a relational database).
- Optional: Docker for containerized deployment.

---

## Backend Setup

### **1. Virtual Environment Installation**

Instead of running commands manually, the setup script automates environment initialization:

```bash
# From the backend directory
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Alternatively, automate this with:
```bash
bash launch.sh  # For Linux/macOS
launch.bat       # For Windows
```

### **2. Backend Launch**

Once dependencies are installed:
```bash
uvicorn app.main:app --reload
```
This starts the API server on `http://localhost:8000`.

---

## Frontend Setup

### **1. Install Dependencies**

```bash
cd frontend
npm install
```

### **2. Start the Frontend Development Server**

```bash
npm run dev
```
The frontend server will be available on `http://localhost:5173`.

---

## Docker Deployment (Optional)

A `Dockerfile` is available for containerized deployment:

```dockerfile
FROM python:3.9
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ ./
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Build and Run the Image

```bash
docker build -t float-backend .
docker run -p 8000:8000 float-backend
```

For frontend, ensure Node.js dependencies are part of your image.

---

## Combined Setup with `make`

Use the included `Makefile` for streamlined setup and deployment:

```bash
make install  # Install backend dependencies
make run      # Start the backend server
make build    # Build the frontend assets
```

---

## Notes

- Use `setup.py` to manage backend dependency installation.
- Ensure Redis and PostgreSQL are running for Celery and database connections.
- Adjust `.env` variables for deployment-specific configurations.
