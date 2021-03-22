import requests
from bs4 import BeautifulSoup

res = requests.get("http://psy-helper.com")

soup = BeautifulSoup(res.text, 'html.parser')
for item in soup.select(".product-title"):

    print(item.a.text)