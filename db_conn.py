import pymysql

#접속
conn = pymysql.connect(host="127.0.0.1", port=3307, user='root', password='1111', db='python', charset="utf8")

curs = conn.cursor(pymysql.cursors.DictCursor)

sql = "select * from tschedule where id = %s"
curs.execute(sql, (1))

rows = curs.fetchall()
for row in rows:
    print(row)

conn.close()
