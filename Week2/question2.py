import requests
from bs4 import BeautifulSoup as bs

url = "https://www.oriana.com/jewellery/gold-jewellery.html"
html_text = requests.get(url).text
soup = bs(html_text,'html.parser')
for i in soup.find_all('div',class_='product-item-info'):
    if(i.a.img['alt']):
        print(i.a.img['alt'])
