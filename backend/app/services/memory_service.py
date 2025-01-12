# manages long term and short term memories

class MemoryService:

    def __init__(self):
        # placeholder for memory set up or retrieval of previous memory
        self.short_term_memory = []
        self.long_term_memory = []
    
    def store(self, memory):
        # add an element to short term memory, send to embedding function,
        # and store in long term if appropriate.
        # add timestamps, confidence score, data type, and expiration dates.
        self.short_term_memory.append(memory)
        print(f"memory: {memory} stored in short term.")
        # store in long term with embedding
        self.long_term_memory.append(memory)
        # TODO embed memory to long term database here.

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