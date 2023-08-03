from cryptography.fernet import Fernet
import os
import hashlib
import base64

def derive_key(key_str):
    return hashlib.sha256(key_str.encode()).digest()

def base64_url_encode(data):
    return base64.urlsafe_b64encode(data)

def decrypt_file(key, encrypted_file_path):
    try:
        with open(encrypted_file_path, 'rb') as file:
            encrypted_data = file.read()

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        original_file_path = encrypted_file_path[:-len('.encrypted')]

        with open(original_file_path, 'wb') as original_file:
            original_file.write(decrypted_data)

        print("File decrypted successfully!")

    except FileNotFoundError:
        print("Encrypted file not found!")

def main():
    print("File Decryption Tool")
    print("--------------------")

    key_input = input("Enter the decryption key: ")
    key = derive_key(key_input)
    encoded_key = base64_url_encode(key)

    encrypted_file_path = input("Enter the path of the encrypted file to decrypt: ")

    if not os.path.isfile(encrypted_file_path):
        print("Invalid file path.")
        return

    decrypt_file(encoded_key, encrypted_file_path)

if __name__ == "__main__":
    main()
