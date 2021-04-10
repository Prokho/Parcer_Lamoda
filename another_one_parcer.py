import requests
from bs4 import BeautifulSoup



res = requests.get("https://www.gloria-jeans.ru/search?q=%3Apriority%3AinStock%3Atrue%3AproductLabelType%3ASALE%3AcategoryPathAge%3AMALE%3Acategory%3Aboys-jeans")

soup = BeautifulSoup(res.text, 'html.parser')
for item in soup.select(".js-product-ref-link"):
    print(item)
    item_price = item.select(".strike-diag js-old-price-info")
    print(item_price)
    #print(item.select(".lowestPrice")[0].attrs["data-price"])
