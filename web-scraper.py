import requests
from bs4 import BeautifulSoup

#create file pointer to the request file
f = open('ws-request.txt', 'r+')

#After reading in the text as a URL address, close the file
URL = f.read()
f.close()

#Grab the page data from the URL with Requests
page = requests.get(URL)

#Create a Soup object with BS
#Then grab only the first instance of a paragraph from the document
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all('p')[0].get_text()

#Take the results from the scrape and output them to a response file
g = open('ws-response.txt', 'w+')
g.write(results)

#Once written, close the file
g.close()
