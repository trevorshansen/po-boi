import requests
import time
from requests import get
import bs4
from bs4 import BeautifulSoup
import json
ssd_names = []
ssd_prices = []
pages = [int(i) for i in range(0,4)]
rows = [0,20,40,60]

def jsondata(key, value):
    #converts to dict
    ssd_dict = dict(zip(key, value))
    ssd_json = json.dumps([{'SSD_Name': k, 'Price': v} for k, v in ssd_dict.items()], indent=4)
    writejsonfile(ssd_json)


def writejsonfile(jsonobj):
    f = open("ssdprices2.json", 'w')
    print(jsonobj, file= f)
    f.close()

for page in pages:
    Solid_state_url = requests.get(f'https://www.frys.com/search?cat=-73810&nearbyStoreName=false&pType=pDisplay&fq=100404%20Internal&resultpage={page}&start={rows[page]}&rows=20').text
    ssd_scraper = BeautifulSoup(Solid_state_url, 'lxml')
    ssd_price = ssd_scraper.find_all("li", {'id': 'did_price1valuediv'})
    # get prices
    for prices in ssd_price:
        if prices.find("b") is not None:
            current_price = prices.b.text.strip('$')
            ssd_prices.append(current_price)
    #get names
    ssdname = ssd_scraper.find_all("p", class_='font_reg productDescp')
    for names in ssdname:
        current_name = names.find("a")
        if current_name is not None:
            ssd_names.append(current_name.text)

jsondata(ssd_names,ssd_prices)






