# provides security functions such as encryption and hashing
from cryptography.fernet import Fernet

class SecurityService:
    def __init__(self, key=None):
      if not key:
          print('No key set for encryption, use load_key or set_key')
      else:
          self.key = key

    def load_key(self, path):
      # loads a key for enc/dec from path
      print(f"key loaded from {path}")
      self.key = 'test key' #placeholder.

    def set_key(self, key):
      # sets the enc/dec key
        self.key = key

    def encrypt(self, plaintext):
        # Placeholder for encryption logic
      print(f"encrypting: {plaintext}")
      return "encrypted " + plaintext

    def decrypt(self, ciphertext):
        # Placeholder for decryption logic
      print(f"decrypting: {ciphertext}")
      return "decrypted " + ciphertext

    def hash(self, data):
        # Placeholder for hashing logic.
      print(f"hashing: {data}")
      return f"hashed: {data}"


    def encrypt(self, plaintext):
        cipher = Fernet(self.key)
        return cipher.encrypt(plaintext.encode()).decode()

    def decrypt(self, ciphertext):
        cipher = Fernet(self.key)
        return cipher.decrypt(ciphertext.encode()).decode()
