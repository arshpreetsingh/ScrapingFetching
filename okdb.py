from sqlalchemy import *

def create_db():
    db = create_engine('sqlite:////home/ubuntu/bitfine_trading/order_id.db')
    metadata = MetaData(db)
    old_ticker = Table('orders', metadata,Column('ticker_id', Integer, primary_key=True),Column('order_id',Float),)
    old_ticker.create()
    return old_ticker.insert()
   

'''
from sqlalchemy import *
db = create_engine('sqlite:////home/metal-machine/Desktop/order_id.db')
metadata = MetaData(db)
tickers = Table('orders', metadata, autoload=True)

m=tickers.insert({'order_id':200})
db.execute(m)

'''
