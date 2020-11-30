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
#conn = pymysql.connect(host="localhost", port=3307, user='root', password='1111', db='python', charset="utf8")
curs = conn.cursor(pymysql.cursors.DictCursor)

# sql = "select t.name from tschedule AS t JOIN teacherseat AS tch WHERE t.id = tch.teacher"
# curs.execute(sql, (1))
#
# rows = curs.fetchall()
# for row in rows:
#     print(row)
#     print(row['name'])
# conn.close()


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
        self.seatnum = 0
        sql = "select * from tschedule AS t JOIN teacherseat AS tch WHERE tch.seatnum = %s and tch.teacher = t.id"
        curs.execute(sql, (seatnum))
        print(seatnum)
        rows = curs.fetchall()
        for row in rows:
            print(row['name'])
        print(rows)
        self.teacherName.setText(row['name']+"선생님")
        # self.status.setText(self.statusBar)
        self.statusBar(seatnum)

    def setSeatNum(self, seatnum):
        self.seatnum = seatnum

    def ontimeout(self):
        print(self.seatnum)

    def statusBar(self, seatnum):
        sql = "select * from tschedule AS t JOIN teacherseat AS tch WHERE tch.seatnum = %s and tch.teacher = t.id"
        curs.execute(sql, (seatnum))
        print(seatnum)
        rows = curs.fetchall()
        for row in rows:
            print(row['name'])
        print(rows)

        strtime = int(strftime("%H%M", localtime()))
        if(910<= strtime <= 950):
            self.schedule+=day+"1"
        elif(1000 <= strtime <= 1040):
            self.schedule+=day+"2"
        elif (1050 <= strtime <= 1130):
            self.schedule += day + "3"
        elif (1140 <= strtime <= 1220):
            self.schedule += day + "4"
        elif (1330 <= strtime <= 1410):
            self.schedule += day + "5"
        elif (1420 <= strtime <= 1500):
            self.schedule += day + "6"
        elif (1510 <= strtime <=1550):
            self.schedule += day + "7"
        elif(106<strtime):
            self.schedule += day + "3"

        if(row[self.schedule] == None):
            self.status.setText("자리에 있음")
            print(row[self.schedule])
        else :
            self.status.setText(row[self.schedule])

# if _name_ == '_main_':
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