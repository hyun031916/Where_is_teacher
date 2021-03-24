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

# conn = pymysql.connect(host="192.168.0.9", port=3307, user='newuser', password='zxcdsaqwe7845', db='python', charset="utf8")
conn = pymysql.connect(host="127.0.0.1", port=3307, user='root', password='1111', db='python', charset="utf8")
curs = conn.cursor(pymysql.cursors.DictCursor)

#UI 파일 연결
status_ui = uic.loadUiType("status_window.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class StatusClass(QDialog, status_ui) :
    schedule = ""
    my_date = date.today()
    day = calendar.day_name[my_date.weekday()]
    seat = 0
    statusDic = {0:"수업 중", 1:"자리에 있음", 2:"회의 중", 3: "휴식 중", 4: "식사 중", 5: "잠시 자리 비움"}
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

    def statusBar(self, seatnum):
        sql = "select * from tschedule AS t JOIN teacherseat AS tch WHERE tch.seatnum = %s and tch.teacher = t.id"
        curs.execute(sql, (seatnum))
        rows = curs.fetchall()
        for row in rows:
            pass

        sql2 = "SELECT * FROM teacherseat where seatnum = "+seatnum
        curs.execute(sql2)
        seatrows = curs.fetchall()
        for seatrow in seatrows:
            pass

        self.message.setText(seatrow['message'])

        for key, value in self.statusDic.items():
            if(seatrow['status']==key):
                self.status.setText(value)
        conn.commit()

    def editStatusButtonClicked(self):
        self.showStatus()

    def showStatus(self):
        # self.statusWindow = EditStatusClass(self.seat)
        self.statusWindow = PasswordClass(self.seat)
        self.statusWindow.show()
        r = self.statusWindow.showModal()
        if r:
            self.accept()