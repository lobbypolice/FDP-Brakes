import requests
#http://www.autozone.com/searchresult?searchText=MKD1204&vehicleSetFromSearch=false&keywords=MKD1204
url = "http://www.autozone.com/searchresult?searchText=MKD1204&vehicleSetFromSearch=false&keywords=MKD1204"
r = requests.get("http://www.autozone.com/searchresult?searchText=MKD1204&vehicleSetFromSearch=false&keywords=MKD1204", allow_redirects=False)
print(r.text)