
from sqlalchemy import *

#engine = create_engine('mysql+pymysql://root:Amber252556!@@localhost/mdb_final')
#engine = create_engine('sqlite:///:', echo=True)

engine = create_engine('sqlite:////home/metal-machine/Desktop/sqlalchemy_example.db')
metadata= MetaData(engine)
 

omdb_data = Table('positions1', metadata,
    Column('omdb_id', Integer, primary_key=True),
    Column('status', String(200)),
    Column('timestamp', Float),
    Column('symbol', String(200)),
    Column('amount', Float),
    Column('base', Float),
    Column('swap', Float),
    Column('pl', Float),)

omdb_data.create()
mm = omdb_data.insert()

mm.execute({'status':'hello'})

omdb_data2 = Table('positions2', metadata,
    Column('omdb_id', Integer, primary_key=True),
    Column('status', String(200)),
    Column('timestamp', Float),
    Column('symbol', String(200)),
    Column('amount', Float),
    Column('base', Float),
    Column('swap', Float),
    Column('pl', Float),)

omdb_data2.create()
mm = omdb_data2.insert()

'''
for i in m:
    movie_info = imdb.get_title_by_id(i)
    mm.execute({'title':str(movie_info.title), 'poster':str(movie_info.poster_url),'cover':str(movie_info.cover_url),\
    'imdb_rating':float(movie_info.rating),'genre':str(movie_info.genres),'plot':str(movie_info.plot_outline),'year':float(movie_info.year),\
    'movie_id':i,'runtime':float(movie_info.runtime)})
    time.sleep(10)
'''
