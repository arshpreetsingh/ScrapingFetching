from bs4 import BeautifulSoup
import requests
import re
import json
import time
import numpy as np
all_array = []

import re
my_regex=re.compile(r'tt\d\d\d\d\d\d\d')
for pages in xrange(0,2):
    url = 'http://www.imdb.com/search/title?genres=family&page='+str(pages)
    print url
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    other_data = soup.find_all("div",{"class":"lister-item-content"})
    #print html
    for i in other_data:
        m = i.findChildren()[0].renderContents()
        main_string = m.split()[5]
        m=re.finditer(my_regex,main_string, flags=0)
        for movie_id_data in m:
            movie_id =movie_id_data.group()
            all_array.append(movie_id)
            time.sleep(1)
            
live_array = np.array(all_array)
print 'this one'
print live_array

# now get DB array

# db vichon IDs di ikk array kadho, uston baad online IDS di array save karvao, 
# dona nu compare karke uniquie array save karwao fer us array de according DB ch entry marwao
