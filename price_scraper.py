
import requests
import time
from requests import get
import bs4
import urllib.request
from bs4 import BeautifulSoup
import json
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized') #
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
from selenium import webdriver

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}
def get_safeway_price():
    url = requests.get('https://www.safeway.com/shop/search-results.html?q=milk&zipcode=94611').text
    Scraper = BeautifulSoup(url,'lxml')
    product_container = Scraper.find('div', class_ = 'product-level-4')
   # print(product_container)
    Scraper.prettify()
    print(Scraper)

def get_amazon_price():
    driver = webdriver.Chrome()
    driver.get('https://www.safeway.com/shop/search-results.html?q=milk&zipcode=94611')
   # price = driver.find_element_by_xpath('//*[@id="pg136010121price"]')
    page = driver.page_source
    Scrapy = BeautifulSoup(driver.page_source,'lxml')
    Scrapy.prettify()
    print(Scrapy)
   # print(price.text)
get_amazon_price()

