import requests
from bs4 import BeautifulSoup as bs

URL = "https://vit.ac.in/school/allfaculty/site/computer-applications"
html_text = requests.get(URL).text
soup = bs(html_text,'html.parser')

def traverse(parent, prefix):
  for node in parent.find_all(recursive=False):
    print(prefix+"-->"+node.name)
    traverse(node, prefix+" ")

def compare(bs):
  traverse(bs,"")

compare(soup)

