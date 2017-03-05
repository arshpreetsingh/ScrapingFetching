from bitfinex.client import Client, TradeClient
from decimal import Decimal
from sqlalchemy import *

client = Client()
trade = TradeClient('K4HJultQmdvroWCnNy5OMcXx7QfGoQgZw0vrkWmuV1Y','dFt4tsMFszh2vTGGvHqFEP3fkaaSniJ4zDA4pSWyJOM')

db = create_engine('sqlite:///all_ticker.db')
metadata = MetaData(db)

old_ticker = Table('ticker', metadata,
    Column('ticker_id', Integer, primary_key=True),
    Column('timestamp',Float),
    Column('last_price', Float),
    Column('high', Float),
    Column('low', Float),
)
    
old_ticker.create()
i = old_ticker.insert()

#we will run ohlc4 for every 4 hours, Old_ticker==> this will be last price of last 4 hours
def ohlc4_database(symbol_used=''):

	'''returns open,high,low and close(yet not completed) this function will save in database'''
	
	ticker_data = client.ticker(symbol_used)
	today_data = client.today(symbol_used)
	
	#old_ticker = (ticker_data['last_price']+ticker_data['high']+ticker_data['low']+ticker_data['last_price'])/4
	#old_ticker =  ticker_data['last_price'],ticker_data['high'],ticker_data['low'],ticker_data['last_price']
	
	return i.execute({'timestamp':ticker_data['timestamp'], 'last_price': ticker_data['last_price'],'high': ticker_data['high'],'low':ticker_data['low']})


while True:
	try:
		print ohlc4_database(symbol_used='btcusd')
	except:
		pass
