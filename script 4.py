from bs4 import BeautifulSoup
import requests
url = "https://trendeconomy.ru/data/h2/Russia/TOTAL"
class_ = "vis-content"
r = requests.get(url)
html = BeautifulSoup (r.text)
t = html.find(class_= class_).text
print(t)