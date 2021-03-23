import requests
from bs4 import BeautifulSoup



res = requests.get("https://www.lamoda.ru/c/33/")

soup = BeautifulSoup(res.text, 'html.parser')
for item in soup.select(".products-list-item"):

    print(item.attrs["data-price"])
    print(item.div.attrs["data-brand"])
    print(item.div.attrs["data-name"])




