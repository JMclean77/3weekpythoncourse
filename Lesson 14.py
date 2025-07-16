from wsgiref import headers

import requests
from bs4 import BeautifulSoup
from lxml import etree, html
"""
url= "https://quotes.toscrape.com/"

headers= { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

}
response= requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        quote_text= quote.find("span", class_="text").text
        print(quote_text)

#print(soup.prettify())

"""


url= "https://books.toscrape.com/"

response = requests.get(url)

tree = html.fromstring(response.text)

book_section = tree.xpath('//article[contains(@class, "product_pod")]/h3/a/@title')
print(book_section)


