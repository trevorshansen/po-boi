import requests
import bs4
from bs4 import BeautifulSoup
import json
ssdweb = requests.get('https://www.frys.com/search?cat=-73810&nearbyStoreName=false&pType=pDisplay&fq=100404%20Internal').text
webpage = requests.get("https://www.frys.com/product/9956046?site=sa:Homepage%20Pod:Pod4").text
ssd = BeautifulSoup(ssdweb, 'lxml')
soup = BeautifulSoup(webpage, 'lxml')
#print(soup.prettify())
# match = soup.find("span", {'id': 'did_price1valuediv'}).text.strip("$")
allssd = ssd.find_all("li", {'id': 'did_price1valuediv'})

#print(match.prettify())
#print(allssd)

# find max page number
page = []
pages = ssd.find('ul', {'id' : 'pageNumber' }, class_ = "pagination pagination-sm")

ssd_prices = []
for prices in allssd:
    if prices.find("b") is not None:
        current_price = prices.b.text.strip("$")
        ssd_prices.append(current_price)
#print(ssd_prices)
ssd_prices = [float(i) for i in ssd_prices]
#print(ssd_prices)

ssdname = ssd.find_all("p", class_ = 'font_reg productDescp')
product_name = []
#print(ssdname)
for names in ssdname:
        current_name = names.find("a")
        if current_name is not None:
            product_name.append(current_name.text)
       # product_name.append(current_name)
#print(product_name)

# convert two list to one dictionary
ssd_dict = dict(zip(product_name, ssd_prices))
#print(ssd_dict)

ssd_json = json.dumps([{'SSD_Name': k, 'Price': v} for k,v in ssd_dict.items()], indent=4)

#print(ssd_json)

#print(json.dumps([{'SSD_Name': k, 'Price': v} for k,v in ssd_dict.items()], indent=4))

f = open("ssdprices.json", 'w')
print(ssd_json, file= f)
f.close()



