import tweepy

class Tw :
    def __init__(self,API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_SECRET) :
        self.auth = tweepy.OAuth1Session(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(self.auth)
    
    # Publish a Tweet    
    def postTweet(self, message) :
        self.api.update_status(status=message)
    
    # Reply to a Tweet
    def replyTweet(self, message, idTweet) :
        self.api.update_status(status=message, in_reply_to_status_id=idTweet)
        
    # Like to a Tweet
    def likeTweet(self, idTweet) :
        self.api.create_favorite(idTweet)
        
    # Retweet a Tweet
    def rtTweet(self, idTweet) :
        self.api.retweet(idTweet)
        
    
        