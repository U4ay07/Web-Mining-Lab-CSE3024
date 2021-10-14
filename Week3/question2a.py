import requests
from bs4 import BeautifulSoup as bs

url = "https://vit.ac.in/school/allfaculty/site/computer-applications"
html_text = requests.get(url).text
soup = bs(html_text,'html.parser')

for i in soup.find_all('h3',class_='title2'):
    print(i.text,end=" ")
    parent=i.parent
    list=[]
    for j in parent.find_all('p',recursive=True):
        list.append(j.text)
    if len(list)>2:
        print("\t-->["+list[2]+"]")
    else:
        print("\t-->[ ]")
