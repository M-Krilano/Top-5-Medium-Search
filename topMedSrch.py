#!/usr/bin/env python3
# Description: Opens top 5 Medium articles in search results

import requests, sys, webbrowser, bs4

#display searching text while downloading Medium page
print('Searching...')

res = requests.get('https://medium.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result
# linkElems = soup.select('.postArticle-content a')
linkElems = soup.select('.postArticle-content a')
# linkElems = soup.find('href')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    # webbrowser.open(linkElems[i])
    webbrowser.open(linkElems[i].get('href'))
print('Done') 
