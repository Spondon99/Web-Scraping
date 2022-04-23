# Find items and prices on a static web page

import requests
from bs4 import BeautifulSoup


URL = "https://www.startech.com.bd/accessories/ear-phone/xiaomi-earphone"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("div", class_="p-item-price")

for result in results:
    price = result.text
    product = result.parent.h4.a.text

    print(product, "->", price)



