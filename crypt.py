import argparse
import os
import json
from cryptography.fernet import Fernet

# File for storing key mappings
key_mapping_file = "key_mapping.json"

# Function to create a key
def create_key():
    return Fernet.generate_key()

# Function to save key mappings to a JSON file
def save_key_mapping(filename, key):
    mappings = load_key_mappings()
    mappings[filename] = key.decode()  # Store the key as a string
    with open(key_mapping_file, "w") as file:
        json.dump(mappings, file)

# Function to load key mappings from a JSON file
def load_key_mappings():
    if os.path.exists(key_mapping_file):
        with open(key_mapping_file, "r") as file:
            return json.load(file)
    return {}

# Function to encrypt a file
def encrypt_file(filename):
    if not os.path.exists(filename):
        print("File not found. Please ensure the filename is correct.")
        return

    key = create_key()
    fernet = Fernet(key)
    
    with open(filename, "rb") as file:
        data = file.read()
    
    encrypted_data = fernet.encrypt(data)
    
    with open(filename + "_encrypted", "wb") as file:
        file.write(encrypted_data)

    save_key_mapping(filename, key)
    print(f"File encrypted and saved as {filename}_encrypted")

# Function to decrypt a file
def decrypt_file(filename):
    if not os.path.exists(filename):
        print("File not found. Please ensure the filename is correct.")
        return

    mappings = load_key_mappings()
    original_filename = filename.replace("_encrypted", "")
    try:
        key_str = mappings[original_filename]
    except KeyError:
        print(f"No key found for {original_filename}. Please ensure it has been encrypted.")
        return

    key = key_str.encode()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(original_filename + "_decrypted", "wb") as file:
        file.write(decrypted_data)

    print(f"File decrypted and saved as {original_filename}_decrypted")

# Main function to handle argparse commands
def main():
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt files.",
        usage="python3 crypt.py {encrypt|decrypt} filename")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform: encrypt or decrypt")
    parser.add_argument("filename", help="Full path to the file to encrypt or decrypt")

# Check if no arguments were provided
    if len(os.sys.argv) == 1:
        parser.print_help()  
        os.sys.exit(1) 

    try:
        args = parser.parse_args()
    except SystemExit:
        print("\nInvalid command or arguments provided.\n")
        parser.print_help() 
        os.sys.exit(1)
    

    if args.action == "encrypt":
            encrypt_file(args.filename)
    elif args.action == "decrypt":
            decrypt_file(args.filename)
    else:
        print("Invälid action, try again.")

# Run the main function
if __name__ == "__main__":
    main()
