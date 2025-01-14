# manages long term and short term memories

class MemoryService:

    def __init__(self):
        # placeholder for memory set up or retrieval of previous memory
        self.short_term_memory = []
        self.long_term_memory = []
    
    def store(self, memory):
        self.short_term_memory.append(memory)
        print(f"Short-term memory: {memory}")
        embedded_memory = self._embed_memory(memory)
        self.long_term_memory.append(embedded_memory)
        print(f"Long-term memory: {embedded_memory}")


    def retrieve_short(self):
      # return all short term memory.
      return self.short_term_memory

    def retrieve_long(self, query):
      # perform search in long term memory
      print(f"searching long term memory with query: {query}")
      return f"results for query '{query}'" # placeholder result.

    def clear(self):
      # clear all memory
      self.short_term_memory = []
      self.long_term_memory = []
      print("all memory cleared.")

    def _embed_memory(self, memory):
        # Convert memory to vector embedding
        return {"vector": [0.1, 0.2, 0.3], "metadata": memory}
