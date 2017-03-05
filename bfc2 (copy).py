from bs4 import BeautifulSoup
import numpy as np
import requests

url = 'http://python.org/'
links_repository=np.array([])


for link in soup.find_all('a'):
    all_urls.append(link.get('href'))

def scrape_base_url(url):
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        print link.get('href')
        np.append(links_repository,link.get('href'))
        np.save('links_repo.npy',links_repository)   
        return links_repository

print scrape_base_url(url)

#for i in links_repository:
 #   print i

'''
m = requests.get(all_urls[40])
data = r.text

soup = BeautifulSoup(data,'html.parser')
for link in soup.find_all('a'):
    print link.get('href')
'''
    
'''
A crawler is a program that starts with a url on the web (ex: http://python.org), 
fetches the web-page corresponding to that url, and parses all the links on that page into a repository of links. 
Next, it fetches the contents of any of the url from the repository just created, 
parses the links from this new content into the repository and continues 
this process for all links in the repository until stopped or after a given number of links are fetched.
'''
