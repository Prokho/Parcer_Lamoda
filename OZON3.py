import requests
from bs4 import BeautifulSoup



res = requests.get("https://www.ozon.ru/highlight/muzhskaya-obuv-140725/")
print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
container = soup.select(".widget-search-result-container")
print(container)
container = container[0]
subcontainer = container.div

    #print(item.attrs["catalog-item_name"])
    #print(item.select(".linkProduct")[0].attrs["data-ref"])
    #print(item.select(".lowestPrice")[0].attrs["data-price"])



