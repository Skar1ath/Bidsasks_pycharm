import psycopg2

conn = psycopg2.connect("""
    host=rc1b-rnxiibv6aapdl63t.mdb.yandexcloud.net
    port=6432
    dbname=db1
    user=Skarlath
    password=A1!sweclo
    target_session_attrs=read-write
    sslmode=verify-full
 """)
print('Database connected')

cur = conn.cursor()
cur.execute('''

CREATE TABLE Bitmex_XBTUSD
(
SIDE TEXT NOT NULL,
SIZE FLOAT,
PRICE FLOAT
)

''')

conn.commit()
conn.close()