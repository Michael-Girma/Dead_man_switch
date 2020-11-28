import apis
import utils
import time

def main():
    twitter_id, reset_tweet, kill_switch, time_interval, file_path = utils.get_switch_input()
    listener = apis.init_listener(twitter_id)

    key = utils.encrypt(file_path)

    last_tweet_time = {}
    while True:
        latest_tweet = listener.get_latest_tweet()
        new_tweet = utils.check_time(latest_tweet, last_tweet_time)
        if not new_tweet:
            print("[X] discarding encryption key")
            return

        last_tweet_time["datestamp"] = latest_tweet.datestamp
        last_tweet_time["timestamp"] = latest_tweet.timestamp

        if reset_tweet in latest_tweet.tweet:
            print("[X] Decrypting files, Good to see you're not dead :)")
            success = utils.decrypt_file(file_path, key)
            if not success:
                print("[X] Couldn't Decrypt the files. writing key to file")
                utils.write_key_to_file(file_path, key)
            return

        elif kill_switch in latest_tweet.tweet:
            print("[X] discarding encryption key")
            return

        print("[X] Restarting Timer")
        time.sleep(time_interval)