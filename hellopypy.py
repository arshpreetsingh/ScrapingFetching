from sqlalchemy import *
import time
import numpy as np
from decimal import Decimal
# using bitfinex APIs to get today's_ticker
from bitfinex.client import Client, TradeClient
client = Client()
trade = TradeClient('K4HJultQmdvroWCnNy5OMcXx7QfGoQgZw0vrkWmuV1Y','dFt4tsMFszh2vTGGvHqFEP3fkaaSniJ4zDA4pSWyJOM')

# we are inporting the Databse that is being created by bitfinex-boat

engine = create_engine('sqlite:////home/ubuntu/all_ticker.db')
metadata = MetaData(engine)
tickers = Table('ticker', metadata, autoload=True)

def find_nearest(array,value):
	""" gets the numpy array and timestamp as input and retunrs the nearest value"""
	
	idx = np.abs(array-value).argmin()
	return  array[idx]

def ohlc_past(hours):
	"""This function returns the seconds as input and retrun the required ohlc_4"""
	
	seconds = 3600*hours # converting hours into seconds
	time_delta = float('{:7f}'.format(time.time()-seconds))
	time_stamp = tickers.select(tickers.c.timestamp)
	timestamp_array = np.array([i[1] for i in time_stamp.execute()])
	time_stamp_value = find_nearest(timestamp_array,time_delta)	
	sql_statement = tickers.select(tickers.c.timestamp==time_stamp_value)
	match_list = [i for i in sql_statement.execute()]
	ohlc_delta = match_list[0]
	
     #1469192333.2017772, 660.03, 668.0, 660.0	
	# presently ohlc_delta is returning timedelta[1],lastprice[2],high[3],low[4] ::: now How to get close as well
	#return type(ohlc_delta[2])
	return (ohlc_delta[2]+ohlc_delta[3]+ohlc_delta[4]+ohlc_delta[2])/4.0


def ohlc4_today(symbol_used):

	'''returns open,high,low and close(yet not completed) this function will save in database'''
	
	ticker_data = client.ticker(symbol_used)
	today_data = client.today(symbol_used)
	return (ticker_data['last_price']+ticker_data['high']+ticker_data['low']+ticker_data['last_price'])/4.0


def ticker_last(symbol_used):

	'''returns open,high,low and close(yet not completed) this function will save in database'''
	
	ticker_data = client.ticker(symbol_used)
	today_data = client.today(symbol_used)
	return ticker_data['last_price']


'''
getDiff() =>
yesterday=security(tickerid, timeframe, ohlc4[1])
today=ohlc4
delta=today-yesterday
percentage=delta/yesterday
'''

def auto_order_buy(amount, price):

	order_made = trade.place_order(amount, price, side='buy', ord_type='market', symbol='btcusd', exchange='bitfinex')
	return order_made



def auto_order_sell(amount, price):

	order_made = trade.place_order(amount, price, side='sell', ord_type='market', symbol='btcusd', exchange='bitfinex')
	return order_made

def getDiff(symbol,hours):
	
	delta = ohlc4_today(symbol)-ohlc_past(hours)
	return delta/ohlc_past(hours)

'''
PineActivationFunctionLinear(v) => v
PineActivationFunctionTanh(v) => (exp(v) - exp(-v))/(exp(v) + exp(-v))
l0_0 = PineActivationFunctionLinear(getDiff())
l1_0 = PineActivationFunctionTanh(l0_0*0.8446488687)
'''
def main_call():
    while True:
        l0_0 = getDiff('btcusd',8)
        l1_0 = np.tanh(l0_0*0.8446488687)

        l1_1 = np.tanh(l0_0*-0.5674069006)
        l1_2 = np.tanh(l0_0*0.8676766445)

<lots of calculation here>

        l3_0 = np.tanh(l2_0*-0.1366382003 + l2_1*0.8161960822 + l2_2*-0.9458773183 + \
        l2_3*0.4692969576 + l2_4*0.0126710629 + l2_5*-0.0403001012 + l2_6*-0.0116244898 + l2_7*-0.4874816289 + l2_8*\
        -0.6392241448 + l2_9*-0.410338398 + l2_10*-0.1181027081 + l2_11*0.1075562037 + l2_12*-0.5948728252 \
        +l2_13*0.5593677345 + l2_14*-0.3642935247 + l2_15*-0.2867603217 + l2_16*0.142250271 + l2_17*-0.0535698019 \
        +l2_18*-0.034007685 + l2_19*-0.3594532426 + l2_20*0.2551095195 + l2_21*0.4214344983 + l2_22*0.8941621336 \
        +l2_23*0.6283377368 + l2_24*-0.7138020667 + l2_25*-0.1426738249 + l2_26*0.172671223 + l2_27*0.0714824385 \
        +l2_28*-0.3268182144 + l2_29*-0.0078989755 + l2_30*-0.2032828145 + l2_31*-0.0260631534 + l2_32*0.4918037012)
                    
        if(l3_0>0):
		#do whatever you did a candlestick ago? how to sort out this one?
            print l3_0
            print auto_order_buy('0.01',str(ticker_last('btcusd')))
        elif(l3_0<0):
            print l3_0
            print auto_order_sell('0.01',str(ticker_last('btcusd')))
        else:
            pass
            
