# Float Project

Float is a latent-thought based learning agent designed to run on locally managed hardware with a focus on privacy. It specializes in efficient latent modeling and is augmented by external systems.

## Overview

Float leverages advanced language models and a modular architecture to provide a robust platform for learning and interaction. It integrates with various tools and APIs to enhance its capabilities.

## Architecture

- **Language Models**: Utilizes Mistral, Google Pali+/Gemma, OAI API, and OpenCV.
- **Data Store**: Employs vector and graph databases for efficient world modeling.
- **Tool Calling**: Supports ETL, data augmentation, and training pipelines.
- **Modular Design**: Allows for easy replacement of internal models and features.
- **Reasoning and Observational Capabilities**: Uses special tokens for reasoning and learning.
- **Privacy**: Locally managed with encrypted memories and masked API calls.

## Setup Instructions

### Prerequisites

- **Python 3.8+**
- **Node.js 16+** with npm
- **Redis** (for Celery backend)
- **PostgreSQL** (if using a relational database)
- **Docker** (optional for containerized deployment)

### Backend Setup

1. **Create a Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. **Launch the Backend**:
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend Setup

1. **Install Dependencies**:
   ```bash
   cd frontend
   npm install
   ```

2. **Run the Development Server**:
   ```bash
   npm run dev
   ```

### Docker Deployment

1. **Build and Run the Backend Image**:
   ```bash
   docker build -t float-backend .
   docker run -p 8000:8000 float-backend
   ```

## Key Features

- **Model Context Management**: Manage and display the current model context.
- **Tool Integration**: Add and manage tools for enhanced functionality.
- **Privacy-Focused**: Designed to operate with a focus on user privacy.

For more detailed information, refer to the `Overview.txt` and `environment setup.md` files in the `docs/` directory.
