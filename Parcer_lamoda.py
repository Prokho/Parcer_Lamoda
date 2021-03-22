import requests
from bs4 import BeautifulSoup



res = requests.get("https://www.lamoda.ru/c/33/shoes-tufli")

soup = BeautifulSoup(res.text, 'html.parser')
for item in soup.select(".products-list-item_labels"):

    print(item.text)


