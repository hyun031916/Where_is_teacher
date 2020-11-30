import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

import pymysql
from datetime import date
import calendar
from time import localtime, strftime

#모듈 불러오기

my_date = date.today()
day = calendar.day_name[my_date.weekday()]
print(day)

conn = pymysql.connect(host="192.168.0.9", port=3307, user='newuser', password='zxcdsaqwe7845', db='python', charset="utf8")
curs = conn.cursor(pymysql.cursors.DictCursor)

sql = "select * from tschedule where id = %s"
curs.execute(sql, (1))

rows = curs.fetchall()
for row in rows:
    print(row)
    print(row['name'])
conn.close()


#UI 파일 연결
form_class = uic.loadUiType("status_window.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class StatusClass(QDialog, form_class) :
    schedule = ""
    my_date = date.today()
    day = calendar.day_name[my_date.weekday()]
    print(day)
    def __init__(self, seatnum) :
        super().__init__()
        self.setupUi(self)
        self.seatnum = seatnum
        self.teacherName.setText(row['name']+"선생님")
        self.editStatus.clicked.connect(self.statusBar)

    def ontimeout(self):
        print(self.seatnum)

    def statusBar(self):
        strtime = strftime("%H%M", localtime())
        print(strtime)
        self.schedule+=day

# if __name__ == '__main__':
#     # QApplication : 프로그램을 실행시켜주는 클래스
#     app = QApplication(sys.argv)
#
#     # StatusClass의 인스턴스 생성
#     statusWindow = StatusClass()
#
#     # 프로그램 화면을 보여주는 코드
#     statusWindow.show()
#
#     # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
#     app.exec_()