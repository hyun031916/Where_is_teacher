import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

import pymysql
from datetime import date
import calendar
from time import localtime, strftime
from password import PasswordClass

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
status_ui = uic.loadUiType("status_window.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class StatusClass(QDialog, status_ui) :
    schedule = ""
    my_date = date.today()
    day = calendar.day_name[my_date.weekday()]
    print(day)
    seat = 0
    status = [0, 1, 2, 3, 4, 5]   #0: 수업 중, 1: 자리에 있음, 2: 회의 중, 3: 휴식 중, 4: 식사 중, 5: 잠시 자리 비움
    def __init__(self, seatnum) :
        super().__init__()
        self.setupUi(self)
        self.seatnum = 0

        sql = "select * from tschedule AS t JOIN teacherseat AS tch WHERE tch.seatnum = %s and tch.teacher = t.id"
        curs.execute(sql, (seatnum))
        rows = curs.fetchall()
        for row in rows:
            pass
        self.teacherName.setText(row['name']+"선생님")
        # self.status.setText(self.statusBar)
        self.statusBar(seatnum)
        self.seat = seatnum
        self.editStatus.clicked.connect(self.editStatusButtonClicked)

    def setSeatNum(self, seatnum):
        self.seatnum = seatnum

    def ontimeout(self):
        print(self.seatnum)

    def statusBar(self, seatnum):
        sql = "select * from tschedule AS t JOIN teacherseat AS tch WHERE tch.seatnum = %s and tch.teacher = t.id"
        curs.execute(sql, (seatnum))
        rows = curs.fetchall()
        for row in rows:
            pass

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

        cursor1 = conn.cursor()
        sql2 = "UPDATE teacherseat set status=%s where seatnum = %s"
        sql3 = "UPDATE teacherseat set message=%s where seatnum = %s"
        if(row[self.schedule] == None):
            self.message.setText("자리에 있음")
            data = (StatusClass.status[1], seatnum)
            cursor1.execute(sql2, data)

            data = ("자리에 있음", seatnum)
            cursor1.execute(sql3, data)
        else:
            self.message.setText(row[self.schedule])
            data = (StatusClass.status[0], seatnum)
            cursor1.execute(sql2, data)

            data = (row[self.schedule], seatnum)
            cursor1.execute(sql3, data)

        conn.commit()

    def editStatusButtonClicked(self):
        self.showStatus()

    def showStatus(self):
        # self.statusWindow = EditStatusClass(self.seat)
        self.statusWindow = PasswordClass(self.seat)
        self.statusWindow.show()

# if __name__ == '_main_':
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