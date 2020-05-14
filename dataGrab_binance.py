import pandas as pd
import numpy as np
import requests

class DataGrab:

    def getBinanceSpot(self):

        def splitPair(tickerString):
            if tickerString[-4:] == 'USDT':
                return [tickerString.split('USDT')[0].lower(), 'usdt']
            elif tickerstring[-3:] == 'ETH':
                return [tickerString.split('ETH')[0].lower(), 'eth']
            elif tickerstring[-3:] == 'BTC':
                return [tickerString.split('BTC')[0].lower(), 'btc']
            elif tickerString[-3:] == 'BNB':
                return [tickerString.split('BNB')[0].lower(), 'bnb']
            return np.nan

        url = 'https://api.binance.com/api/v1/ticker/24hr'
        bnn_df = pd.DataFrame(requests.get(url).json())
        print(bnn_df)

a = DataGrab().getBinanceSpot()
print(a)