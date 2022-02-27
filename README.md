# CS361_Microservice
Microservice to scrape data from Consolewiki entries

The Microservice requires a text file with a HTML page URL.
(the only contents within)

The service takes the URL and checks for the first instance of a paragraph (the quotation about the FFXIV Job on the page) and returns this summary paragraph as text.

This is written to a response file that can be used as you wish.

To use:

have a text file named "ws-request" as a txt file (i.e. ws-request.txt has a URL for the Dragoon job) this is read in the same directory that the scraper is in on your local machine.

Once finished, the scraper will output a file named "ws-response" which contains only this summary paragraph from within the HTML document.
