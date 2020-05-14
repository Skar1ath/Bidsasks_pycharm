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

SELECT DATE_FORMAT(CURDATE(), '%m/%d/%Y');
SET @SQL =CONCAT('CREATE TABLE `' ,DATE_FORMAT(CURDATE(), '%m/%d/%Y'), '` (id int(10))');
PREPARE stmt FROM @SQL;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

''')

conn.commit()
conn.close()