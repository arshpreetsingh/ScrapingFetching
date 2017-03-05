import urllib2
response = urllib2.urlopen('https://www.cryptocompare.com/api/data/histoday/?e=CCCAGG&fsym=BTC&limit=93&tsym=USD')
print(response.read())
