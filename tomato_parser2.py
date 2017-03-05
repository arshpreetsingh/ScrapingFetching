url = 'https://www.rottentomatoes.com/m/101_dalmatians/'
from bs4 import BeautifulSoup
import requests
import re
import json
import time
import numpy as np
all_array = []
import re
html = requests.get(url)

soup = BeautifulSoup(html.content,'html.parser')
poster_image = soup.find_all("img",{"class":"posterImage"})
for i in poster_image:
    print i['src'] 
#tomato_rating = soup.find_all("span",{"class":"meter-value superPageFontColor"})
#tomato_rating
des_crip = soup.find_all("div",{"id":"movieSynopsis","class":"movie_synopsis clamp clamp-6","style":"clear:both"})
for i in des_crip:
    print i.string
other_values = soup.find_all("div",{"class":"col col-sm-19 col-xs-14 text-left"})
this_list = []
for i in other_values:
    print "########"
    print i.text
    time.sleep(3)
    print '########'
#<div class="col col-sm-19 col-xs-14 text-left">G</div>
#<div id="movieSynopsis" class="movie_synopsis clamp clamp-6" style="clear:both">
  #  print i
#<img 
##src="https://resizing.flixster.com/kS1J6VEDw32kn_Rt2sZHuxbOrkA=/206x305/v1.bTsxMTIwNzE0ODtqOzE3MTM5OzEyMDA7MjEwMDsyODAw" 
#class="posterImage">



