# custom tokenizer using hugging face tokenizers

class CustomTokenizer:
  def __init__(self):
      # place to add special tokens, and define encoding / decoding functions.
      pass

  def encode(self, text):
    # turn text into tokens.
      return f"encoded: {text}"

  def decode(self, tokens):
      #turn tokens into text.
      return f"decoded: {tokens}"