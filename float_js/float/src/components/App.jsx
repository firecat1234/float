import React, { useState } from "react";
import Chat from "./Chat";
import Sidebar from "./Sidebar";
import "../styles/App.css"; // Global styles

const App = () => {
  const [thoughts, setThoughts] = useState(["Welcome to float!"]); // ✅ Default array

  return (
    <div className="app-container">
      <Sidebar thoughts={thoughts} />
      <Chat />
    </div>
  );
};

export default App;
