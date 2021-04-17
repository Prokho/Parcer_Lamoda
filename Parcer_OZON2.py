import requests
from bs4 import BeautifulSoup



res = requests.get("https://msk.metro-cc.ru/category/bakaleya/chipsy-suhari-sneki")

soup = BeautifulSoup(res.text, 'html.parser')
for item in soup.select(".catalog-item_name"):

    print(item.text)
    #print(soup.get_text())
    #print(item.select["href"])
    #print(item.select(".linkProduct")[0].attrs["data-ref"])
    #print(item.select(".lowestPrice")[0].attrs["data-price"])

for item in soup.select(".catalog-item_price-lvl_current"):
    print(item.text)



