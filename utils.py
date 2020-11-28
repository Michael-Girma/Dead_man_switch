from cryptography.fernet import Fernet


def get_switch_input():
    # TODO: apply error checking mechanism since this is a dead man's switch
    twitter_handle = input("Twitter handle to listen on: ")
    reset_tweet = input("Tweet to stop the dead man's switch: ")
    kill_switch = input("Tweet to immediately destroy key(killswitch): ")
    time_interval = input("The time interval in seconds to check for tweets: ")
    file = input("Relative path to the file that is about to be encrypted: ")
    # Check if the program has R/W privileges

    return twitter_handle, reset_tweet, kill_switch, time_interval, file


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
