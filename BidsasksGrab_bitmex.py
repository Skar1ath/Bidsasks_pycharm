import pandas as pd
import requests
import time
from time import gmtime

data = requests.get('https://www.bitmex.com/api/v1/orderBook/L2?symbol=XBT&depth=0').json()

for order in data:
    del order['symbol']
    del order['id']

side = []
order_size = []
price = []

for order in data:
    side.append(order['side'])
    order_size.append(order['size'])
    price.append(order['price'])

df = pd.DataFrame([side, order_size, price]).T
df.columns = ['Side', 'Size', 'Price']

asks = df.loc[df['Side'] == 'Sell']

cut_price_1 = asks['Price'].iloc[-1] + asks['Price'].iloc[-1]*0.01
cut_asks_1 = asks[asks.Price < cut_price_1]
sum_size_asks_1 = cut_asks_1['Size'].sum()

cut_price_5 = asks['Price'].iloc[-1] + asks['Price'].iloc[-1]*0.05
cut_asks_5 = asks[asks.Price < cut_price_5]
sum_size_asks_5 = cut_asks_5['Size'].sum()

cut_price_10 = asks['Price'].iloc[-1] + asks['Price'].iloc[-1]*0.1
cut_asks_10 = asks[asks.Price < cut_price_10]
sum_size_asks_10 = cut_asks_10['Size'].sum()

cut_price_20 = asks['Price'].iloc[-1] + asks['Price'].iloc[-1]*0.2
cut_asks_20 = asks[asks.Price < cut_price_20]
sum_size_asks_20 = cut_asks_20['Size'].sum()

cut_price_50 = asks['Price'].iloc[-1] + asks['Price'].iloc[-1]*0.5
cut_asks_50 = asks[asks.Price < cut_price_50]
sum_size_asks_50 = cut_asks_50['Size'].sum()

print(sum_size_asks_1, sum_size_asks_5, sum_size_asks_10, sum_size_asks_20, sum_size_asks_50)

bids = df.loc[df['Side'] == 'Buy']

cut_price_1 = bids['Price'].iloc[0] - bids['Price'].iloc[0]*0.01
cut_bids_1 = bids[bids.Price > cut_price_1]
sum_size_bids_1 = cut_bids_1['Size'].sum()

cut_price_5 = bids['Price'].iloc[0] - bids['Price'].iloc[0]*0.05
cut_bids_5 = bids[bids.Price > cut_price_5]
sum_size_bids_5 = cut_bids_5['Size'].sum()

cut_price_10 = bids['Price'].iloc[0] - bids['Price'].iloc[0]*0.1
cut_bids_10 = bids[bids.Price > cut_price_10]
sum_size_bids_10 = cut_bids_10['Size'].sum()

cut_price_20 = bids['Price'].iloc[0] - bids['Price'].iloc[0]*0.2
cut_bids_20 = bids[bids.Price > cut_price_20]
sum_size_bids_20 = cut_bids_20['Size'].sum()

cut_price_50 = bids['Price'].iloc[0] - bids['Price'].iloc[0]*0.5
cut_bids_50 = bids[bids.Price > cut_price_50]
sum_size_bids_50 = cut_bids_50['Size'].sum()

print(sum_size_bids_1, sum_size_bids_5, sum_size_bids_10, sum_size_bids_20, sum_size_bids_50)

timestr = time.strftime("%Y-%m-%d %H:%M:%S UTC", gmtime())
act_price = bids['Price'].iloc[0]

print(timestr, act_price)

orderbook_df = pd.DataFrame([timestr, act_price, sum_size_asks_1, sum_size_bids_1, sum_size_asks_5, sum_size_bids_5, sum_size_asks_10, sum_size_bids_10, sum_size_asks_20, sum_size_bids_20, sum_size_asks_50, sum_size_bids_50 ]).T
orderbook_df.columns = ['Time', 'Price', 'Asks_1%', 'Bids_1%', 'Asks_5%', 'Bids_5%','Asks_10%', 'Bids_10%','Asks_20%', 'Bids_20%','Asks_50%', 'Bids_50%',]

print(orderbook_df)

orderbook_df.to_csv('Bitmex_XBTUSD_1h', mode = 'a', header = False, index = False)