import requests
import select

res = requests.get("https://www.lamoda.ru/c/33/shoes-tufli")

f = open("data.html", "w", encoding="utf-8")
f.write(res.text)
position = 0
while position != -1:
    position = res.text.find('<div class="products-list-item_labels">', position)
    position_end = res.text.find('</div>', position)
    print(res.text[position:position_end])
    position = position_end


