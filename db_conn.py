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

#
# if conn.open:
#     with conn.cursor() as curs:
#         print("connected")

#커서 가져오기
# cursor = conn.cursor()
#
# #sql 문 만들기
# sql = "SELECT * FROM 'tschedule'"
# cursor.excute(sql)
#
# result = cursor.fetchall()
# for res in result:
#     print(res)

# conn.close()