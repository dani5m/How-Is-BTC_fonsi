from config import *
from tw import *
from crypto import *
import datetime
import time

tw = Tw(BAERER_TOKEN,API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_SECRET)
btc = Crypto("bitcoin")

while True :
    currentTime = datetime.datetime.now()
    if currentTime.minute == 0 or currentTime.minute == 30:
        btcVal = btc.crypto_obtainValue()
        tw.postTweet("The #Bitcoin is at " + btcVal + " now")
        time.sleep(174634560)



    




