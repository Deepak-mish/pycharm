import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_1?dchild=1&keywords=sony+a7&qid=1587276651&sr=8-1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id = "productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = price[0:5]

print(title.strip())
