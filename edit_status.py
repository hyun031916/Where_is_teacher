import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

import pymysql
from datetime import date
import calendar
from time import localtime, strftime


conn = pymysql.connect(host="192.168.0.9", port=3307, user='newuser', password='zxcdsaqwe7845', db='python', charset="utf8")
#conn = pymysql.connect(host="localhost", port=3307, user='root', password='1111', db='python', charset="utf8")
curs = conn.cursor(pymysql.cursors.DictCursor)


#UI 파일 연결
edit_status_ui = uic.loadUiType("edit_status.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class EditStatusClass(QDialog, edit_status_ui) :
    schedule = ""
    my_date = date.today()
    day = calendar.day_name[my_date.weekday()]
    print(day)
    def __init__(self, seatnum) :
        super().__init__()
        self.setupUi(self)
        self.addComboBox()
        # self.updateMessage()
        self.editStatus.clicked.connect(self.saveChanges)


        sql = "select * from tschedule AS t JOIN teacherseat AS tch WHERE tch.seatnum = %s and tch.teacher = t.id"
        curs.execute(sql, (seatnum))
        print(seatnum)
        rows = curs.fetchall()
        for row in rows:
            pass
        self.teacherName.setText(row['name'] + "선생님")

    def addComboBox(self):
        self.status_comboBox.addItem("자리에 있음")
        self.status_comboBox.addItem("수업하고 있음")
        self.status_comboBox.addItem("쉬는 중임")
        self.status_comboBox.addItem("점심시간임")

    # def updateMessage(self):
    #     self.edit_message.setPlaceholderText("메세지를 입력하세요")

    def saveChanges(self, seat):
        print(self.edit_message.toPlainText())

        sql = "UPDATE teacherseat set message=%s where seatnum = %s"
        data = (self.edit_message.toPlainText, seat)
        # mycursor.execute(sql2, data)
        # curs.execute(sql, (seatnum))
        # print(seatnum)
        rows = curs.fetchall()
        for row in rows:
            pass
        curs.execute(sql, data)

# if _name_ == 'main':
#     # QApplication : 프로그램을 실행시켜주는 클래스
#     app = QApplication(sys.argv)
#
#     # StatusClass의 인스턴스 생성
#     statusWindow = EditStatusClass()
#
#     # 프로그램 화면을 보여주는 코드
#     statusWindow.show()
#
#     # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
#     app.exec_()