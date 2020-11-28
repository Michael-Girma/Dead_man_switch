import twint

class init_listener:
    def __init__(self, twitter_handle):
        config = twint.Config()
        config.Limit = 5
        config.Store_object = True
        config.Username = twitter_handle
        self.config = config

    def get_latest_tweet(self):
        twint.run.Search(self.config)
        tweet_object = twint.output.tweet_list[0]
        return tweet_object