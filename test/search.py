import requests
from lxml import html
session_requests = requests.session()
url = "https://shop.advanceautoparts.com/"
result = session_requests.get(url)
tree = html.fromstring(result.text)