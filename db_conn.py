import pymysql

#접속
conn = pymysql.connect(host="192.168.0.9", port=3307, user='newuser', password='zxcdsaqwe7845', db='python', charset="utf8")

curs = conn.cursor(pymysql.cursors.DictCursor)

sql = "select * from tschedule where id = %s"
curs.execute(sql, (1))

rows = curs.fetchall()
for row in rows:
    print(row)

conn.close()
