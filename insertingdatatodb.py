import psycopg2
import pandas as pd

conn = psycopg2.connect("""
    host=rc1b-puqkx0scvllcr57p.mdb.yandexcloud.net
    port=6432
    dbname=db1
    user=user1
    password=A1!swepos
    target_session_attrs=read-write
    sslmode=verify-full
    """)

print('database connected')
cur = conn.cursor()

cur.execute('''

CREATE TABLE Bitmex_XBTUSD_
(
TIME TEXT NOT NULL
ASKS_1% FLOAT NOT NULL,
BIDS_1% FLOAT NOT NULL,
ASKS_5% FLOAT NOT NULL,
BIDS_5% FLOAT NOT NULL,
ASKS_10% FLOAT NOT NULL,
BIDS_10% FLOAT NOT NULL,
ASKS_20% FLOAT NOT NULL,
BIDS_20% FLOAT NOT NULL,
ASKS_50% FLOAT NOT NULL,
BIDS_50% FLOAT NOT NULL,
PRICE FLOAT NOT NULL
)

''')

df = pd.read_csv('/Users/Shelomov/PycharmProjects/Plotting Crypto Data/bitcoinity_data-4.csv.csv')
df.to_sql("Bitmex_XBTUSD", engine)
conn.close()
