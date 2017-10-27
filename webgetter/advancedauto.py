import requests
import re
import time
from bs4 import BeautifulSoup
#gnad999
#gnad785
#PXD1273H
#MKD785
searchterm = "mkd785"
searchterm = searchterm.lower()
url = 'https://shop.advanceautoparts.com/web/PartSearchCmd?storeId=10151&catalogId=10051&langId=-1&pageId=partTypeList&actionSrc=Form&searchTerm=' + searchterm
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
counter = 0
while(soup.title.string == "Advance Auto Parts  - Down for Maintenance" or counter == 10):
    #time.sleep(1)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    counter += 1
    if counter == 10:
        print("Failed")

pattern = re.compile("(\$\d+\.\d+)")
script = soup.find("script", text=pattern)
if script:
    match = pattern.search(script.text)
    if match:
        price = match.group(0)
        print(price)

#print(r.status_code)
#print(soup.prettify())
#print(soup.p['class'])