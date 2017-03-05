import requests
import time
from datetime import datetime,timedelta

def ohlc_yesterday():
    """ returns OHLC_yesterday"""

    m = datetime.today()
    n= datetime.today()-timedelta(1) 
    url = 'https://www.cryptocompare.com/api/data/histoday/?e=Bitfinex&fsym=BTC&aggregate=1&limit=1&tsym=USD'
    p = requests.get(url)
    m = p.json()
    z = m['Data']
    my_data = z[0]
    return my_data['open'],my_data['high'],my_data['low'],my_data['close'] 

def ohlc_intervals(hours):
    """ returns OHLC_yesterday"""

    m = datetime.today()
    n= datetime.today()-timedelta(1) 
    url = 'https://www.cryptocompare.com/api/data/histohour/?e=Bitfinex&fsym=BTC&aggregate=%s&limit=2&tsym=USD'%hours
    p = requests.get(url)
    m = p.json()
    z = m['Data']
    my_data = z[-1]
    return my_data['open'],my_data['high'],my_data['low'],my_data['close']

print ohlc_intervals(4)

'''
{u'FirstValueInArray': True, u'TimeFrom': 1474502400, u'Type': 100, u'TimeTo': 1474588800, u'Aggrgated': False, 
u'Message': u'Battlecruiser operational.Make it happen.Set a course.Take it slow.', u'Data': [{u'volumeto': 
1385936.73118782, u'high': 598.7, u'low': 595.92, u'time': 1474502400.0, u'volumefrom': 2320.2161388399995, 
u'close': 596.8, u'open': 597.39}, 
{u'volumeto': 283528.1684918003, u'high': 597.69, u'low': 595.95, u'time': 1474588800.0, 
u'volumefrom': 474.92732176, u'close': 597.3, u'open': 595.95}], u'Response': u'Success'}
'''
