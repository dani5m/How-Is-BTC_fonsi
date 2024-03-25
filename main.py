import tweepy
from bs4 import BeautifulSoup 
import requests

# creedenciales twitter
API_KEY = "hZ0rduAYNWVtgfrXtyvvQXKdq"
API_SECRET = "MEabgOrj6nONK3YjY37dSl58rk2CUpefNTlq0QTkLflACdZ7Dm"
ACCESS_TOKEN = "1143621107452403712-umuWj26Jmh6zwz3R1d696jTPgJZ4MG"
ACCESS_SECRET = "SUe9cWFD2ewuKUS73Vy1JfkuTCGaWnc7WKVshkQ5kpkIM"
BAERER_TOKEN = "AAAAAAAAAAAAAAAAAAAAABbnswEAAAAAO2PFGTbRaFOcAFPUE7tmqIspoQ0%3DhNeyfIRtqxeuQhtbe5RLiAAnRU7fROJrViFOWxLB3bwk6blku8"

client = tweepy.Client(BAERER_TOKEN,API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_SECRET)

# obtener valor bitcoin
def obtenerValorBitcoin():
    # text-larger text-price
    url = requests.get(f'https://awebanalysis.com/es/coin-details/bitcoin/')
    soup = BeautifulSoup(url.content, 'html.parser') # Crea un objeto BeautifulSoup para analizar el contenido HTML de la página web.
    result = soup.find('td', {'class': 'text-larger text-price'})
    format_result = result.text
    
    return format_result

valueB = obtenerValorBitcoin()
tweet = "The #Bitcoin is at " + valueB + " now"
print(tweet)


# client.create_tweet(text= "Hola")

