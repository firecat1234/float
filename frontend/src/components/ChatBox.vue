<template>
    <div>
        <div class="chat-container">
        <div class="message" v-for="(message, index) in messages" :key="index"
          :class="{ 'sent': message.sender === 'user', 'received': message.sender === 'bot' }"
          >
            {{ message.content }}
        </div>
    </div>

    <div class="input-container">
        <input type="text" v-model="newMessage" @keyup.enter="sendMessage" placeholder="Enter a Message..." />
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
      messages: [],
      thought:'',
    };
  },
  methods: {
      async sendMessage() {
          if (this.newMessage.trim() === '') return;

          this.messages.push({sender: 'user', content: this.newMessage });

          try {
              const response = await axios.post('/api/chat/', {
                  message: this.newMessage
              });
              this.messages.push({sender:'bot', content: response.data.message})
              this.thought = response.data.thought;
          } catch(error) {
              console.error('Error sending message', error)
                this.messages.push({sender:'bot', content: 'Error in backend'})
          }
          this.newMessage = '';
      }
  },
}
</script>

<style scoped>
.chat-container {
  flex: 1;
  padding: 10px;
  overflow-y: scroll;
}
.input-container {
    padding: 10px;
    display: flex;
    border-top: solid 1px;
    gap:10px;
}

.message {
    padding: 10px;
    margin-bottom: 5px;
    border-radius: 5px;
    max-width: 70%;
}

.sent {
    background-color: #DCF8C6; /* user message bubble color */
    align-self: flex-end;
}
.received {
    background-color: #E5E5EA; /* bot message bubble color*/
    align-self: flex-start;
}

</style>