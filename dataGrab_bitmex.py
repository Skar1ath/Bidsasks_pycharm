import pandas as pd
import requests
import time

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
timestr = time.strftime("%Y%m%d")
df.to_csv(timestr + '_Bitmex_XBTUSD.csv')