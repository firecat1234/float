import React, { useState } from "react";
import Chat from "./Chat";
import Sidebar from "./Sidebar";
import SettingsModal from "./SettingsModal";
import "../styles/App.css";

// Default configs
const defaultConfigs = {
  local: {
    baseURL: "http://localhost:8000",
    token: "LOCAL_TOKEN",
  },
  api: {
    baseURL: "https://externalapi.com",
    token: "EXTERNAL_TOKEN",
  },
};

const App = () => {
  const [thoughts, setThoughts] = useState(["Welcome to float!"]);
  const [apiMode, setApiMode] = useState("api");
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);
  const [configs, setConfigs] = useState(defaultConfigs);

  const toggleApiMode = () => {
    setApiMode((prevMode) => (prevMode === "api" ? "local" : "api"));
  };

  const openSettings = () => {
    setIsSettingsOpen(true);
  };

  const closeSettings = () => {
    setIsSettingsOpen(false);
  };

  const handleSaveConfigs = (newConfigs) => {
    setConfigs(newConfigs);
    // If you want your apiWrapper to pick these up dynamically,
    // you can store them in a global or pass them down as props.
  };

  return (
    <div className="app-container">
      <Sidebar thoughts={thoughts} />
      <div className="main-content">
        <div className="top-bar">
          <button onClick={toggleApiMode}>
            Switch to {apiMode === "api" ? "Local" : "API"} Mode
          </button>
          <button onClick={openSettings}>Settings</button>
        </div>
        <Chat mode={apiMode} configs={configs} />
      </div>

      <SettingsModal
        isOpen={isSettingsOpen}
        onClose={closeSettings}
        configs={configs}
        onSave={handleSaveConfigs}
      />
    </div>
  );
};

export default App;
