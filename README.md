# Top-5-Medium-Search
Simple python script that lets you search for a topic in https://medium.com and opens the first 5 articles in new browser tabs.

Utilized:
- requests module to download the medium search page (using the search terms entered in command line)
- beautifulsoup(bs4) module to webscrape the links to the top 5 articles
- sys to grab the search terms from the command line
- webbrowser module to open the links in teh browser tabs
