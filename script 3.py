from bs4 import BeautifulSoup
import requests
url = "https://rosrealt.ru/cena/?t=dinamika"
class_ = "table publication__table"
r = requests.get(url)
html = BeautifulSoup (r.text)
t = html.find(class_=class_).text
print(t)