import React, { createContext, useState } from "react";
import ReactDOM from "react-dom/client";
import App from "./components/App"; // Clean import path

// Create a Context for the global state
export const GlobalContext = createContext();

// Create a Provider component
const GlobalProvider = ({ children }) => {
  const [state, setState] = useState({
    context: null, // Initial state for model context
    // Add other global state variables here
  });

  return (
    <GlobalContext.Provider value={{ state, setState }}>
      {children}
    </GlobalContext.Provider>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <GlobalProvider>
      <App />
    </GlobalProvider>
  </React.StrictMode>,
);
