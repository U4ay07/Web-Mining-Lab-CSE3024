import requests
from bs4 import BeautifulSoup as bs
#Extract the name,position of all faculty
#Extract the name,position of all notabil alumni.

url="https://chennai.vit.ac.in/computer-science-engineering-chennai/faculty/"
html_text = requests.get(url,verify=False).text
soup = bs(html_text,"html.parser")
for i in soup.find_all("h3",attrs={"class":"item-title"}):
    print("Faculty Name :",i.text)
    print("Faculty title :",i.find_next_sibling().text)
    print("\n")
