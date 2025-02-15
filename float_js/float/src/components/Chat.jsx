import React, { useState } from "react";
import { memoryStore, apiWrapper } from "../utils/proxy";
import "../styles/Chat.css";

const Chat = ({ mode }) => {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const sendMessage = async () => {
    if (!message.trim()) return;
    setResponse("");
    setError(null);
    setLoading(true);

    try {
      memoryStore["last_message"] = { content: message, importance: 5 };
      const res = await apiWrapper.chat({ message, mode });

      if (res.error) {
        throw new Error(res.error);
      }

      memoryStore["last_ai_response"] = { content: res.message, importance: 4 };
      setResponse(res.message);
    } catch (err) {
      setError("Something went wrong. Please try again.");
      console.error("Chat API Error:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <h1 className="chat-header">Float AI Chat</h1>
      <input
        className="chat-input"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        disabled={loading}
        placeholder="Type your message..."
      />
      <button className="chat-button" onClick={sendMessage} disabled={loading}>
        {loading ? "Sending..." : "Send Message"}
      </button>
      {error && <p className="chat-error">{error}</p>}
      <p className="chat-response">{response}</p>
    </div>
  );
};

export default Chat;
