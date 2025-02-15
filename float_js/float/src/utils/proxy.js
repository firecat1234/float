import axios from "axios";

/**
 * Vite exposes front-end environment variables via import.meta.env.
 * Make sure your .env keys start with "VITE_".
 */
const localBaseURL =
  import.meta.env.VITE_LOCAL_BASE_URL || "http://localhost:8000";
const localToken = import.meta.env.VITE_LOCAL_TOKEN || "LOCAL_TOKEN";

const apiBaseURL =
  import.meta.env.VITE_EXTERNAL_API_URL || "https://externalapi.com";
const apiToken = import.meta.env.VITE_API_KEY || "EXTERNAL_TOKEN";

/**
 * 🔹 Auto-Decaying Memory Store
 * This uses a Proxy to store data with a "decay" factor that
 * decreases over time. Once decay < 0.1, the key is removed.
 */
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

      // Calculate how long it's been since we set this key
      const timeElapsed = (Date.now() - target[key].timestamp) / 1000; // seconds
      // Decay the importance factor
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

/**
 * 🔹 Auto-Wrapping API Calls with Mode Selection
 * This proxy intercepts property access (e.g., apiWrapper.chat),
 * then performs a POST to the chosen endpoint (local or api).
 */
export const apiWrapper = new Proxy(
  {},
  {
    get(_, endpoint) {
      return async (params = {}) => {
        // Extract the mode from params, default to "api"
        const { mode = "api", ...rest } = params;

        // Build a small config object for each mode
        const configs = {
          local: {
            baseURL: localBaseURL,
            token: localToken,
          },
          api: {
            baseURL: apiBaseURL,
            token: apiToken,
          },
        };

        // Use the requested mode config, or fall back to "api"
        const config = configs[mode] || configs.api;

        console.log(`🌍 API Call: ${endpoint} [${mode}]`, rest);

        try {
          // Example: POST to "<baseURL>/api/<endpoint>"
          const res = await axios.post(
            `${config.baseURL}/api/${endpoint}`,
            rest,
            {
              headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${config.token}`,
              },
            },
          );
          return res.data;
        } catch (err) {
          console.error(`❌ API Error (${endpoint}):`, err);
          return { error: "API request failed" };
        }
      };
    },
  },
);
