import axios from "axios";

// 🔹 Auto-Decaying Memory Store
export const memoryStore = new Proxy(
  {},
  {
    set(target, key, value) {
      console.log(`🧠 Memory Updated: ${key} →`, value);

      target[key] = {
        data: value,
        timestamp: Date.now(),
        decay: value.importance || 1, // Default importance if not set
      };

      return true;
    },
    get(target, key) {
      if (!target[key]) return null;

      // Decay function
      const timeElapsed = (Date.now() - target[key].timestamp) / 1000;
      target[key].decay *= Math.exp(-0.01 * timeElapsed);

      if (target[key].decay < 0.1) {
        console.log(`💀 Memory Expired: ${key}`);
        delete target[key];
        return null;
      }

      return target[key].data;
    },
  },
);

// 🔹 Auto-Wrapping API Calls
export const apiWrapper = new Proxy(
  {},
  {
    get(_, endpoint) {
      return async (params = {}) => {
        console.log(`🌍 API Call: ${endpoint}`, params);

        try {
          const res = await axios.post(`/api/${endpoint}`, params);
          return res.data;
        } catch (err) {
          console.error(`❌ API Error (${endpoint}):`, err);
          return { error: "API request failed" };
        }
      };
    },
  },
);
