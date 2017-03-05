from bs4 import BeautifulSoup
import requests
import re
import json

#from imdb import IMDb

#ia = IMDb()

# have to use r.content
url = 'http://www.imdb.com/search/title?genres=family'
html = requests.get(url)
#print html.content
soup = BeautifulSoup(html.content, 'html.parser')
#print soup
#print soup
#links = soup.find_all('a')

#other_data = soup.find_all("div")
#other_data = soup.find_all("div",{"class":"lister-item-image float-left"})

other_data = soup.find_all("div",{"class":"lister-item-content"})
import re
for i in other_data:
    m = i.findChildren()[0].renderContents()
    #<a href="/title/tt3040964/?ref_=adv_li_tt">The Jungle Book</a>
    main_string = m.split()[5]
    m=re.finditer('(?<=/)\w+',main_string, flags=0)
    for movie_id_data in m:
        movie_id =movie_id_data.group()

    print 'movie-id:'+movie_id 
    title=i.findChildren()[2].renderContents()
    print "title:"+title
    year = i.findChildren()[3].renderContents()
    print "year:"+year
    cert = i.findChildren()[5].renderContents()
    print "cert:"+cert
    duration = i.findChildren()[7].renderContents()
    print "duration:"+duration
    genre = i.findChildren()[9].renderContents()
    print "genre:"+genre
    rating = i.findChildren()[13].renderContents()
    print "rating:"+rating
    plot = i.findChildren()[55].renderContents()
    print "plot:"+plot
    director = i.findChildren()[57].renderContents()
    print "director:"+director
    movie_cover = ia.get_movie(movie_id)
    print "movie-cover:"+movie_cover['full-size cover url']

    break



#other_data2 = soup.find_all("div",{"class":"lister-item-content"})

'''
for i in other_data2:
    #print i.findChildren()[9].renderContents()
    title=i.findChildren()[2].renderContents()
    year = i.findChildren()[3].renderContents()
    cert = i.findChildren()[5].renderContents()
    duration = i.findChildren()[7].renderContents()
    genre = i.findChildren()[9].renderContents()
    rating = i.findChildren()[13].renderContents()
    plot = i.findChildren()[55].renderContents()
    director = i.findChildren()[57].renderContents()
    break
'''
