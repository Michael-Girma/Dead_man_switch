from apis import Listener
import utils
import time

def main():
    telegram_handle, reset_keyword, kill_switch, time_interval, file_path = utils.get_switch_input()
    listener = Listener(telegram_handle)
    listener.start_listening()

    print("[X] Encrypting sensitive file")
    key = utils.encrypt_file(file_path)

    check_in_time = time.time() + time_interval
    print("[X] Listening for incoming messages")

    while check_in_time > time.time():
        if listener.new_message:
            new_update = listener.get_new_update()
            new_message = new_update.message.text

            if kill_switch in new_message:
                new_update.message.reply_text("[X] Discarding decryption keys")
                break

            if reset_keyword in new_message:
                new_update.message.reply_text("[X] Decrypting files")
                success = utils.decrypt_file(file_path, key)
                print("[X] Decrypting files")
                if not success:
                    print("[X] Trouble decrypting, file maybe missing.\n[X] Writing key to file")
                    utils.write_key_to_file(file_path, key)
                listener.stop_polling()
                return
            else:
                new_update.message.reply_text(f"[X] Extending check-in time by {time_interval} seconds")
                check_in_time = time.time() + time_interval
        time.sleep(1)

    print("[X] Discarding Keys")
    key = "0" * len(key)
    print("[X] The key has been discarded.")
    listener.stop_polling()


if __name__ == "__main__":
    main()