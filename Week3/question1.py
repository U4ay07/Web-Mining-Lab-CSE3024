import requests
from bs4 import BeautifulSoup as bs
URL = "https://www.vit.ac.in"
html_text = requests.get(URL).text
soup = bs(html_text,'html.parser')
print(soup.title)
print("\n")
print("All anchor tags with nav-link are: \n")
for i in soup.find_all('a',class_='nav-link'):
	print("->",i.text)
