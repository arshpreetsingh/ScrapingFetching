import urllib2
import urllib
from sqlalchemy import *
#import omdb
#m = urllib2.urlopen('http://www.omdbapi.com/?t=hello&y=&plot=short&r=json')
#m.read()
#urllib.quote_plus('sdkfbkds skdfbdskfh sakfdhbdsfhkvsda')
import time
import numpy as np
from decimal import Decimal
# using bitfinex APIs to get today's_ticker

# we are inporting the Databse that is being created by bitfinex-boat

engine = create_engine('sqlite:////home/metal-machine/Desktop/sqlalchemy.db')
metadata= MetaData(engine)
omdb_data = Table('omdb_data', metadata,
    Column('omdb_id', Integer, primary_key=True),
    Column('title', String(200)),
    Column('poster', String(200)),
    Column('imdb_rating', Float),
    Column('tomato_user_rating', Float),
    Column('rated', String(200)),
    Column('type', String(200)),
    Column('genre', String(200)),
    Column('plot', String(400)),
    Column('runtime', String(400)),
)

omdb_data.create()
mm = omdb_data.insert()
# i.execute({'timestamp':ticker_data['timestamp'], 'last_price': ticker_data['last_price'],'high': t$

print mm

'''

import time
import json

#print (np.array([i for i in a.execute()])).size
a = np.load('/home/metal-machine/new_last.npy')
for i in a:


  try:
        m=omdb.get(title=i, fullplot=True, tomatoes=True)
        # ethon shuru karna hai kall nu
        print mm.execute({'title':m['title'], 'poster': m['poster'],'imdb_rating':m['imdb_rating'],'$
        time.sleep(4)
    except:
        pass
'''
