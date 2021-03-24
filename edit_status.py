from PyQt5.QtWidgets import *
from PyQt5 import uic

import pymysql
from datetime import date
import calendar


# conn = pymysql.connect(host="192.168.0.9", port=3307, user='newuser', password='zxcdsaqwe7845', db='python', charset="utf8")
conn = pymysql.connect(host="127.0.0.1", port=3307, user='root', password='1111', db='python', charset="utf8")
curs = conn.cursor(pymysql.cursors.DictCursor)


#UI 파일 연결
edit_status_ui = uic.loadUiType("edit_status.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class EditStatusClass(QDialog, edit_status_ui) :
    schedule = ""
    my_date = date.today()
    day = calendar.day_name[my_date.weekday()]
    status = {0:"수업 중", 1:"자리에 있음", 2:"회의 중", 3: "휴식 중", 4: "식사 중", 5: "잠시 자리 비움"}
    def __init__(self, seatnum) :
        super().__init__()
        self.setupUi(self)
        self.addComboBox()
        # self.updateMessage()
        self.editStatus.clicked.connect(self.saveChanges)
        self.seat = seatnum

        sql = "select * from tschedule AS t JOIN teacherseat AS tch WHERE tch.seatnum = %s and tch.teacher = t.id"
        curs.execute(sql, (seatnum))
        rows = curs.fetchall()
        for row in rows:
            pass
        self.teacherName.setText(row['name'] + "선생님")

    def addComboBox(self):
        # 0: 수업 중, 1: 자리에 있음, 2: 회의 중, 3: 휴식 중, 4: 식사 중, 5: 잠시 자리 비움
        for value in self.status.values():
            self.status_comboBox.addItem(value)

    def saveChanges(self, seat):
        sql = "UPDATE teacherseat set message=%s where seatnum = %s"
        data = (self.edit_message.toPlainText(), self.seat)
        curs.execute(sql, data)
        conn.commit()

        for key, value in self.status.items():
            if(self.status_comboBox.currentText()==value):
                sql = "UPDATE teacherseat set status = %s where seatnum = %s"
                data = (key, self.seat)
                curs.execute(sql, data)
                conn.commit()

        self.accept()