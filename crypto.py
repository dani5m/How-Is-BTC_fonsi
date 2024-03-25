from bs4 import BeautifulSoup 
import requests

def crypto_obtainValue():
    url = requests.get(f'https://awebanalysis.com/es/coin-details/bitcoin/')
    soup = BeautifulSoup(url.content, 'html.parser') # Crea un objeto BeautifulSoup para analizar el contenido HTML de la página web.
    result = soup.find('td', {'class': 'text-larger text-price'})
    format_result = result.text
    
    return format_result