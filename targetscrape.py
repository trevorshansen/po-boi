import requests
import bs4
from bs4 import BeautifulSoup

webpage = requests.get("https://www.target.com/p/2-milk-1gal-good-38-gather-8482/-/A-13276204").text
soup = BeautifulSoup(webpage, 'lxml')
#print(soup.prettify())
match = soup.find_all("span", {'data-test': 'product-price'},class_ = "h-text-bs")


#print(match.prettify())
print(soup.prettify())