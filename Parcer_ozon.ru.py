import requests
from bs4 import BeautifulSoup



res = requests.get("https://www.kiabi.ru/mezhsezonnaya-rasprodazha-muzhchiny_326225")

soup = BeautifulSoup(res.text, 'html.parser')
for item in soup.select(".articleContent"):

    ##print(item.attrs["data-price"])
    print(item.select(".linkProduct")[0].attrs["data-ref"])
    print(item.select(".lowestPrice")[0].attrs["data-price"])







