#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Load the key from the current directory named 'thekey.key'
def load_key():
    return open("thekey.key", "rb").read()

# Decrypt the contents of a file
def decrypt_file(file_name, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and writes it
    """
    f = Fernet(key)

    with open(file_name, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_name, "wb") as file:
        file.write(decrypted_data)

# Main logic
if __name__ == "__main__":
    path = '.'  # Current directory
    files = [file for file in os.listdir(path) if os.path.isfile(file) and file not in ["notbad.py", "thekey.key", "decrypt.py", "encrypt.py"]]

    secret_key = load_key()  # Load the previously generated key

    for file in files:
        decrypt_file(file, secret_key)
        print(f"File decrypted successfully: {file}")
