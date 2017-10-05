import requests

r = requests.get('http://www.autozone.com/')
print(r.status_code)
print(r.text)
