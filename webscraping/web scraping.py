import requests
from bs4 import BeautifulSoup as B
url = "https://www.google.com/"
res = requests.get(url)
html = res.content
soup = B(html,)
for link in soup.find_all('a'):
    print(link.get('href'))
  