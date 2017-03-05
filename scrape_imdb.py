import urllib2
import urllib
from sqlalchemy import *
#m = urllib2.urlopen('http://www.omdbapi.com/?t=hello&y=&plot=short&r=json')
#m.read()
#urllib.quote_plus('sdkfbkds skdfbdskfh sakfdhbdsfhkvsda')
import time
import numpy as np
from decimal import Decimal
# using bitfinex APIs to get today's_ticker

# we are inporting the Databse that is being created by bitfinex-boat

engine = create_engine('mysql://root:Amber252556!@@localhost/imdb1')

metadata = MetaData(engine)
titles = Table('title', metadata, autoload=True)
a = titles.select(titles.c.title)
import time
import json

for i in a.execute():
    name=urllib.quote_plus(i[1])
    print name
    while True:
        try:
            m = urllib2.urlopen('http://www.omdbapi.com/?t=%s&y=&plot=short&r=json'%name)
            ww=json.loads(m.read())
            print ww
        except:
            pass
            print ww
       #time.sleep(3)
#(145609, u'2 Legit Shotgun Bayonette', None, 7, 2016, None, u'L2323', 145608, 1, 6, None, u'9a3b460dd923ce5e9feb1089229eeab9')
#timestamp_array = np.array([i[1] for i in time_stamp.execute()])
	
{"Title":"The Adventures of Buckaroo Banzai Across the 8th Dimension","Year":"1984","Rated":"PG","Released":"10 Aug 1984","Runtime":"103 min","Genre":"Adventure, Comedy, Romance","Director":"W.D. Richter","Writer":"Earl Mac Rauch","Actors":"Peter Weller, John Lithgow, Ellen Barkin, Jeff Goldblum","Plot":"Adventurer/surgeon/rock musician Buckaroo Banzai and his band of men, the Hong Kong Cavaliers, take on evil alien invaders from the eighth dimension.","Language":"English","Country":"USA","Awards":"5 nominations.",
"Poster":"http://ia.media-imdb.com/images/M/MV5BMTk3OTAwNDQwOF5BMl5BanBnXkFtZTgwOTE0MzQxMDE@._V1_SX300.jpg",
"Metascore":"N/A","imdbRating":"6.4","imdbVotes":"17,749",
"imdbID":"tt0086856","Type":"movie","Response":"True"}
