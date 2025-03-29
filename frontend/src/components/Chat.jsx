import React, { useState } from "react";
import { memoryStore, apiWrapper } from "../utils/proxy";

const Chat = () => {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const sendMessage = async () => {
    if (!message.trim()) return;
    setResponse(""); // Clear previous UI
    setError(null);
    setLoading(true); // Start loading

    console.log("Sending message:", message);

    try {
      memoryStore["last_message"] = { content: message, importance: 5 };
      const res = await apiWrapper.chat({ message });

      console.log("API Response:", res);

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
    <div>
      <h1>float</h1>
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        disabled={loading}
      />
      <button onClick={sendMessage} disabled={loading}>
        {loading ? "Sending..." : "Send"}
      </button>
      {error && <p className="error">{error}</p>}
      <p>{response}</p>
    </div>
  );
};

export default Chat;
