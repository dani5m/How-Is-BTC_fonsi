import tweepy

class Tw :
    def __init__(self,BAERER_TOKEN,API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_SECRET) :
        self.client = tweepy.Client(BAERER_TOKEN,API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_SECRET)
    
    # Publish a Tweet    
    def postTweet(self, message) :
        self.client.create_tweet(text= message)
    
    # Reply to a Tweet
    def replyTweet(self, message, idTweet) :
        self.client.create_tweet(text=message, in_reply_to_tweet_id=idTweet)
        
    # Like to a Tweet
    def likeTweet(self, idTweet) :
        self.client.create_favorite(idTweet)
        
    # Retweet a Tweet
    def rtTweet(self, idTweet) :
        self.client.retweet(idTweet)

        
    
        