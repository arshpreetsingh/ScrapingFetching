from bs4 import BeautifulSoup
import requests
import re
import json
import time
import numpy as np
import re
from sqlalchemy import *
engine2 = create_engine('mysql+pymysql://root:Amber252556!@@localhost/rotten_tomato')

metadata2= MetaData(engine2)

omdb_data = Table('rotten3', metadata2,
    Column('id', Integer, primary_key=True),
    Column('url', String(500)),
    Column('poster_image', String(500)),
    Column('plot', String(10000)),
    Column('other_values',String(500)),
    Column('title', String(500)),
)

omdb_data.create()
mm = omdb_data.insert()

base_url = 'https://www.rottentomatoes.com/top/bestofrt/top_100_kids__family_movies'
url = 'https://www.rottentomatoes.com'

html = requests.get(base_url)

movies_list = []
movies_url_list = []

soup = BeautifulSoup(html.content, 'html.parser')
other_data = soup.find_all("a",{"class":"unstyled articleLink","target":"_top","data-pageheader":""})

for i in other_data:
    movies_url_list.append(url+str(i["href"]))
    movies_list.append(i.string)

for single,movie_name in zip(movies_url_list,movies_list):
    try:
        time.sleep(2)
        html2 = requests.get(single)
        soup = BeautifulSoup(html2.content,'html.parser')
        other_values = soup.find_all("div",{"class":"col col-sm-19 col-xs-14 text-left"})
        poster_image = soup.find_all("img",{"class":"posterImage"})
        des_crip = soup.find_all("div",{"id":"movieSynopsis","class":"movie_synopsis clamp clamp-6","style":"clear:both"})
        for j,m,i in zip(poster_image,des_crip,other_values):
        #print 'poster_image'
            mm.execute({'poster_image':str(j['src']),'plot':m.string,'other_values':str(i.string),'title':movie_name,'url':str(single)})
    except:
        pass
