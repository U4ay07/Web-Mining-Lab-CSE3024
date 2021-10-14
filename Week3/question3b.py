import requests
from bs4 import BeautifulSoup as bs
URL = "https://www.batimes.com.ar"
html_text = requests.get(URL,headers={'User-Agent':'Mozilla/5.0'}).text
soup = bs(html_text,'html.parser')

for i in soup.find_all('body',class_='bg-light'):
    for j in i.find_all('img'):
        print("\nImage tags in the web page are: \n")
        print('\n',j)

print('\n\nNumber of img tags is: [ ',len(i.find_all('img')),' ]')
