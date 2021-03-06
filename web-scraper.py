import requests
from bs4 import BeautifulSoup

#Stage base of URL
site = "https://ffxiv.consolegameswiki.com/wiki/"

#Array of all jobs in FFXIV
jobs = ["Paladin", "Warrior", "Dark Knight", "Gunbreaker",
        "White Mage", "Scholar", "Astrologian", "Sage",
        "Dragoon", "Reaper", "Monk", "Samurai", "Ninja",
        "Bard", "Machinist", "Dancer",
        "Black Mage", "Summoner", "Red Mage", "Blue Mage"]

#grab job title from request file, then throw into job var
f = open('ws-request.txt', 'r+')
job = f.read()

#replace any spaces with underscores for a valid URL
job.replace(" ", "_")
f.close()

#parse to correct string for URL
URL = site + job

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
