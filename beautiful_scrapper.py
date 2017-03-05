#!/usr/bin/env python
# beautiful_scrapper.py

from bs4 import BeautifulSoup
import urlparse
import requests

def get_url_links(url):
    """ retunrs all href present in give URL"""

    raw_data  = requests.get(url)
    soup = BeautifulSoup(raw_data.text,"html.parser")
    for link in soup.find_all('a',href=True):
        link['href'] = urlparse.urljoin(url,link['href'])
        yield link['href'] 

if __name__=='__main__':
    
    url = 'http://python.org/'
    print 'Fetching from -->'+url
    links_repository=[link for link in get_url_links(url)] # Fetching all links from 'http://python.org/'
    print 'Done'
    print 'Fetching from -->'+links_repository[-11]
    links_repository_2=[link for link in get_url_links(links_repository[-11])] # Fetching all links from links_repository[-11]
    print links_repository_2
    print 'Done'

'''
A crawler is a program that starts with a url on the web (ex: http://python.org), 
fetches the web-page corresponding to that url, and parses all the links on that page into a repository of links.
 
Next, it fetches the contents of any of the url from the repository just created, 
parses the links from this new content into the repository and continues 
this process for all links in the repository until stopped or after a given number of links are fetched.
'''
