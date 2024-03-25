from bs4 import BeautifulSoup 
import requests

class Crypto :
    def __init__(self, cryptoName) :
        self.cryptoName = cryptoName
    
    # Obtain de value of the crypto    
    def crypto_obtainValue(self):
        url = requests.get(f'https://awebanalysis.com/es/coin-details/{self.cryptoName}/')
        soup = BeautifulSoup(url.content, 'html.parser') # analize HTML content
        result = soup.find('td', {'class': 'text-larger text-price'})
        format_result = result.text
        
        return format_result

