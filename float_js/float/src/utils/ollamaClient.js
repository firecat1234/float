import { Ollama } from "ollama-js-client";

const ollama = new Ollama();

export async function streamOllamaResponse(prompt, setResponse) {
  const res = await fetch("http://localhost:11434/api/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ model: "mistral", prompt }),
  });

  if (!res.body) throw new Error("No response body");

  const reader = res.body.getReader();
  const decoder = new TextDecoder();

  let accumulatedText = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    accumulatedText += decoder.decode(value, { stream: true });
    setResponse(accumulatedText); // Update React state live
  }
}

export default streamOllamaResponse(prompt, setResponse);
