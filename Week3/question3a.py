import requests
from bs4 import BeautifulSoup as bs
import re
URL = "https://www.batimes.com.ar/"
html_text = requests.get(URL,headers={'User-Agent':'Mozilla/5.0'}).text
soup = bs(html_text,'html.parser')

def hasWord(tag):
    text = str(tag.find(text=True,recursive=False))
    if "Fernández" in text:
        return True
    return False
for i in soup.find_all(hasWord):
    print(i)
