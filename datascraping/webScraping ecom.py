import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.in/s?k=iphone&crid=2HXHCZ9A4S03O&sprefix=iphone%2Caps%2C246&ref=nb_sb_noss_1"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

data = {'title': [], 'price': []}

#with open("sample.html", "r") as f:
#   html_doc = f.read()
r = requests.get(url, headers= headers)

soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())
spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price")

for span in spans:
    print(span.string)
    data["title"].append(span.string)


for price in prices:
    if("a-text-price" in price.get("class")):
        print(price.find("span").get_text())
        data["price"].append(price.find("span").get_text())
        if len(data["price"]) == len(data["title"]):
            break

df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv", index = False)


