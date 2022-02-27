import requests
from bs4 import BeautifulSoup

f = open('ws-request.txt', 'r+')
URL = f.read()
#print(URL)
f.close()
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all('p')[0].get_text()

print(results)

g = open('ws-response.txt', 'w+')
g.write(results)
g.close()
