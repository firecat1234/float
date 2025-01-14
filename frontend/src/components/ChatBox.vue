<template>
  <div class="chat-container">
    <!-- Messages Section -->
    <div class="messages">
      <div
        class="message"
        v-for="(msg, index) in messages"
        :key="index"
        :class="msg.sender"
      >
        {{ msg.content }}
      </div>
    </div>

    <!-- Input Section -->
    <div class="input-box">
      <input
        type="text"
        v-model="newMessage"
        placeholder="Type a message..."
        @keyup.enter="sendMessage"
      />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      newMessage: '',
      messages: [], // Stores chat messages
      thought: '', // Optional: Displays the bot's "thought process"
    };
  },
  methods: {
    async sendMessage() {
      if (this.newMessage.trim() === '') return;

      // Add user message to the chat
      this.messages.push({ sender: 'user', content: this.newMessage });

      try {
        // Send message to backend
        const response = await axios.post('/api/chat/', {
          message: this.newMessage,
        });

        // Add bot's response to the chat
        this.messages.push({
          sender: 'bot',
          content: response.data.message || 'No response from bot',
        });

        // Capture the bot's "thought process" (if provided)
        this.thought = response.data.thought || '';
      } catch (error) {
        console.error('Error sending message:', error);
        this.messages.push({
          sender: 'bot',
          content: 'Error connecting to backend. Please try again.',
        });
      }

      // Clear the input box
      this.newMessage = '';
    },
  },
};
</script>

<style>
/* Add styles for chat box */
.chat-container {
  flex: 1;
  width: 100%;
  max-width: 800px;
  display: flex;
  flex-direction: column;
  border-radius: 10px;
  background: linear-gradient(to bottom right, #d9e6f2, #ffffff);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
}

.message {
  padding: 0.5rem 1rem;
  border-bottom: 1px solid #eee;
}

.message.user {
  text-align: right;
  background-color: #e0f7fa;
}

.message.bot {
  text-align: left;
  background-color: #ffffff;
}

.input-box {
  display: flex;
  border-top: 1px solid #ccc;
  padding: 0.5rem;
}

.input-box input {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1rem;
}

.input-box button {
  margin-left: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.input-box button:hover {
  background-color: #0056b3;
}
</style>
