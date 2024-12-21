
from bs4 import BeautifulSoup
import requests
url = "https://xn----ctbjnaatncev9av3a8f8b.xn--p1ai/"
class_ = ("text-right")
r = requests.get(url)
html = BeautifulSoup (r.text)
t = html.find(class_= class_).text
print(t)