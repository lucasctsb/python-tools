from cryptography.fernet import Fernet
import os
import hashlib
import base64

def derive_key(key_str):
    return hashlib.sha256(key_str.encode()).digest()

def base64_url_encode(data):
    return base64.urlsafe_b64encode(data)

def encrypt_file(key, file_path):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()

        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

        # Get the file extension of the original file
        _, file_extension = os.path.splitext(file_path)
        encrypted_file_path = file_path + '.encrypted' + file_extension

        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        print("File encrypted successfully!")

    except FileNotFoundError:
        print("File not found!")

def main():
    print("File Encryption Tool")
    print("--------------------")

    key_input = input("Enter the encryption key: ")
    key = derive_key(key_input)
    encoded_key = base64_url_encode(key)

    file_path = input("Enter the path of the file to encrypt: ")

    if not os.path.isfile(file_path):
        print("Invalid file path.")
        return

    encrypt_file(encoded_key, file_path)

if __name__ == "__main__":
    main()
