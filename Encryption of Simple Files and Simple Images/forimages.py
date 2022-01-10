import os
from cryptography.fernet import Fernet
def encrypt(filename, newfile, key):
   f = Fernet(key)
   with open(filename, "rb") as file:
   # read all file data
      file_data = file.read()
   # encrypt data
   encrypted_data = f.encrypt(file_data)
   # write the encrypted file
   with open(newfile, "wb") as file:
        file.write(encrypted_data)
def decrypt(filename, newfile, key):
     f = Fernet(key)
     with open(filename, "rb") as file:
     # read the encrypted data
        encrypted_data = file.read()
     # decrypt data
        decrypted_data = f.decrypt(encrypted_data)
     # write the original file
     with open(newfile, "wb") as file:
        file.write(decrypted_data)
key = Fernet.generate_key()
enc = encrypt("testimage.jpg", "e_ch6_secret_image.jpg", key)
dec = decrypt("e_ch6_secret_image.jpg", "d_ch6_secret_image.jpg", key)
