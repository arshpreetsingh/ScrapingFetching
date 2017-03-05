from bs4 import BeautifulSoup
import requests
import re
import json
import time
import numpy as np
all_array = []
import re
for pages in xrange(0,200000):
    url = 'http://www.imdb.com/search/title?genres=family&page='+str(pages)
    print url
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    other_data = soup.find_all("div",{"class":"lister-item-content"})
    #print html
    for i in other_data:
        m = i.findChildren()[0]
        print m['href']
        #m = i.findChildren()[0].renderContents()
        #print m['href']
       # main_string = m.split()[5]
        #print main_string['href']
        #m=re.finditer('(?<=/)\w+',main_string, flags=0)
        #for movie_id_data in m:
         #   print movie_id_data.group()
