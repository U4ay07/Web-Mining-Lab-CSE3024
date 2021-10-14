import requests
from bs4 import BeautifulSoup as bs
URL = "https://vit.ac.in/school/allfaculty/site/computer-applications"
html_text = requests.get(URL)
soup = bs(html_text.text,'html.parser')
print("The link and the classes of ")
for footer in soup.find_all('footer'):
    for div in footer.find_all('div',class_='footer_bottom'):
        for a in div.find_all('a'):
            if a.has_attr('class'):
                if len(a['class'])!=0:
                    print("Link: \t",a['href'],"\nClass: \t",a['class'])
