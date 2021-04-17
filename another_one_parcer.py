import requests
from bs4 import BeautifulSoup



res = requests.get("https://www.gloria-jeans.ru/c/girls-schoolchild-footwear-no-season")

soup = BeautifulSoup(res.text, 'html.parser')
for item in soup.select(".js-name-product"):
    print(item.text)


for item in soup.select(".js-analytics-add-in-cart "):

    #print(item.div.attrs["data-price"])
    print(item.attrs["data-price"])