import requests

r = requests.get('https://shop.advanceautoparts.com/web/PartSearchCmd?storeId=10151&catalogId=10051&langId=-1&pageId=partTypeList&actionSrc=Form&searchTerm=gnad999')
print(r.status_code)
print(r.text)
