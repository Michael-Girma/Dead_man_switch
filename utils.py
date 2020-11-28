from cryptography.fernet import Fernet


def get_switch_input():
    # TODO: apply error checking mechanism since this is a dead man's switch
    telegram_handle = input("Telegram handle to listen on: ")
    reset_keyword = input("keyword to stop the dead man's switch: ")
    kill_switch = input("Keyword to immediately destroy key(kill switch): ")
    time_interval = int(input("The time interval in seconds to check for messages: "))
    file = input("Relative path to the file that is about to be encrypted: ")
    # Check if the program has R/W privileges

    return telegram_handle, reset_keyword, kill_switch, time_interval, file


def encrypt_file(file_path):
    # Encrypt the file and returns the key
    key = Fernet.generate_key()
    f = Fernet(key)

    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

    return key


def decrypt_file(file_path, key):
    # Decrypts the file and returns status boolean
    f = Fernet(key)
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = f.decrypt(encrypted_data)

        with open(file_path, "wb") as file:
            file.write(decrypted_data)
        return True

    except Exception:
        return False


def write_key_to_file(file_path, key):
    with open("keys.txt", "a") as key_file:
        key_file.write(f"The key for {file_path}: ${key}")
    return
