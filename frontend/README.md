# Float Frontend

This is the frontend for the Float project, a latent-thought based learning agent designed to run on locally managed hardware with a focus on privacy.

## Overview

The frontend is built using React, providing a modern and responsive user interface for interacting with the backend services. It includes components for managing model context, adding messages and tools, and displaying chat interactions.

## Project Structure

```
frontend/
│
├── src/
│   ├── components/
│   │   ├── forms/
│   │   │   ├── MessageForm.jsx
│   │   │   ├── ToolForm.jsx
│   │   ├── ContextManager.jsx
│   │   ├── Sidebar.jsx
│   │   ├── Chat.jsx
│   │   ├── App.jsx
│   ├── utils/
│   │   ├── apiClient.js
│   ├── styles/
│   ├── main.jsx
│
├── package.json
├── README.md
```

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Run the Development Server**:
   ```bash
   npm start
   ```

3. **Build for Production**:
   ```bash
   npm run build
   ```

## Key Features

- **Model Context Management**: Manage and display the current model context.
- **Message and Tool Forms**: Add messages and tools to the context.
- **Responsive UI**: Modern design with React.

For more information, refer to the backend documentation and the main project README.
