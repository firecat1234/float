import React, { useState } from "react";
import "../styles/SettingsModal.css"; // Add your own styling
//this is basically a placeholder right now. the switch to local mode button i want on top too.
//these are handled in the .env file, which is shared with python, can can be updated-then-hidden from ui in the future.
//please read the code a bit

const SettingsModal = ({ isOpen, onClose, configs, onSave }) => {
  const [localConfig, setLocalConfig] = useState(configs.local);
  const [apiConfig, setApiConfig] = useState(configs.api);

  if (!isOpen) return null; // Don’t render anything if modal is closed

  const handleSave = () => {
    onSave({ local: localConfig, api: apiConfig });
    onClose();
  };

  return (
    <div className="settings-overlay">
      <div className="settings-modal">
        <h2>Settings</h2>
        <h3>Local Configuration</h3>
        <label>
          Base URL:
          <input
            type="text"
            value={localConfig.baseURL}
            onChange={(e) =>
              setLocalConfig({ ...localConfig, baseURL: e.target.value })
            }
          />
        </label>
        <label>
          Token:
          <input
            type="text"
            value={localConfig.token}
            onChange={(e) =>
              setLocalConfig({ ...localConfig, token: e.target.value })
            }
          />
        </label>

        <h3>API Configuration</h3>
        <label>
          Base URL:
          <input
            type="text"
            value={apiConfig.baseURL}
            onChange={(e) =>
              setApiConfig({ ...apiConfig, baseURL: e.target.value })
            }
          />
        </label>
        <label>
          Token:
          <input
            type="text"
            value={apiConfig.token}
            onChange={(e) =>
              setApiConfig({ ...apiConfig, token: e.target.value })
            }
          />
        </label>

        <div className="modal-buttons">
          <button onClick={handleSave}>Save</button>
          <button onClick={onClose}>Cancel</button>
        </div>
      </div>
    </div>
  );
};

export default SettingsModal;
