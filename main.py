import sys
from time import localtime, strftime
import calendar
from datetime import date

import pymysql
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from condition import StatusClass

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
main_ui = uic.loadUiType("start.ui")[0]
#option_ui = uic.loadUiType("status.ui")[0]

conn = pymysql.connect(host="192.168.0.9", port=3307, user='newuser', password='zxcdsaqwe7845', db='python', charset="utf8")
#conn = pymysql.connect(host="localhost", port=3307, user='root', password='1111', db='python', charset="utf8")
curs = conn.cursor(pymysql.cursors.DictCursor)

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, main_ui):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.startButton.clicked.connect(self.showTeacherRoom1)

        #self.pushButton_3.move(100,100)

    def showTeacherRoom1(self):
        #self.statusBar()
        main_ui = uic.loadUi("teacherroom1.ui", self)
        self.leftButton.clicked.connect(self.showTeacherRoom2)
        self.rightButton.clicked.connect(self.showTeacherRoom2)

        self.seat_1.clicked.connect(self.statusButtonClicked1)
        self.seat_1.setText(self.getTeacherName(1))
        self.seat_1.setStyleSheet(self.getStatusColor(1))
        self.seat_2.clicked.connect(self.statusButtonClicked1)
        self.seat_2.setText(self.getTeacherName(2))
        self.seat_2.setStyleSheet(self.getStatusColor(2))
        self.seat_3.clicked.connect(self.statusButtonClicked1)
        self.seat_3.setText(self.getTeacherName(3))
        self.seat_3.setStyleSheet(self.getStatusColor(3))
        self.seat_4.clicked.connect(self.statusButtonClicked1)
        self.seat_4.setText(self.getTeacherName(4))
        self.seat_4.setStyleSheet(self.getStatusColor(4))
        self.seat_5.clicked.connect(self.statusButtonClicked1)
        self.seat_5.setText(self.getTeacherName(5))
        self.seat_5.setStyleSheet(self.getStatusColor(5))
        self.seat_6.clicked.connect(self.statusButtonClicked1)
        self.seat_6.setText(self.getTeacherName(6))
        self.seat_6.setStyleSheet(self.getStatusColor(6))
        self.seat_7.clicked.connect(self.statusButtonClicked1)
        self.seat_7.setText(self.getTeacherName(7))
        self.seat_7.setStyleSheet(self.getStatusColor(7))
        self.seat_8.clicked.connect(self.statusButtonClicked1)
        self.seat_8.setText(self.getTeacherName(8))
        self.seat_8.setStyleSheet(self.getStatusColor(8))
        # self.__timer = QTimer()
        # self.__timer.timeout.connect(self.showTeacherRoom1)
        # self.__timer.start(1000)

    def showTeacherRoom2(self):
        self.statusBar()
        main_ui = uic.loadUi("teacherroom2.ui", self)

        self.leftButton.clicked.connect(self.showTeacherRoom1)
        self.rightButton.clicked.connect(self.showTeacherRoom1)

        self.seat_1.clicked.connect(self.statusButtonClicked1)
        self.seat_1.setText(self.getTeacherName(1))
        self.seat_1.setStyleSheet(self.getStatusColor(1))
        self.seat_2.clicked.connect(self.statusButtonClicked1)
        self.seat_2.setText(self.getTeacherName(2))
        self.seat_2.setStyleSheet(self.getStatusColor(2))
        self.seat_3.clicked.connect(self.statusButtonClicked1)
        self.seat_3.setText(self.getTeacherName(3))
        self.seat_3.setStyleSheet(self.getStatusColor(3))
        self.seat_4.clicked.connect(self.statusButtonClicked1)
        self.seat_4.setText(self.getTeacherName(4))
        self.seat_4.setStyleSheet(self.getStatusColor(4))
        self.seat_5.clicked.connect(self.statusButtonClicked1)
        self.seat_5.setText(self.getTeacherName(5))
        self.seat_5.setStyleSheet(self.getStatusColor(5))
        self.seat_6.clicked.connect(self.statusButtonClicked1)
        self.seat_6.setText(self.getTeacherName(6))
        self.seat_6.setStyleSheet(self.getStatusColor(6))
        self.seat_7.clicked.connect(self.statusButtonClicked1)
        self.seat_7.setText(self.getTeacherName(7))
        self.seat_7.setStyleSheet(self.getStatusColor(7))
        self.seat_8.clicked.connect(self.statusButtonClicked1)
        self.seat_8.setText(self.getTeacherName(8))
        self.seat_8.setStyleSheet(self.getStatusColor(8))
        # self.__timer = QTimer()
        # self.__timer.timeout.connect(self.showTeacherRoom2)
        # self.__timer.start(1000)

    def statusBar(self):
        my_date = date.today()
        day = calendar.day_name[my_date.weekday()]
        schedule = ""
        for i in range(1,8+1):
            sql = "select * from teacherseat where seatnum=" + i
            curs.execute(sql)
            rows = curs.fetchall()
            for row in rows:
                pass
            if row['teacher'] != 0:
                continue
            else:
                sql = "select * from tschedule AS t JOIN teacherseat AS tch WHERE tch.seatnum = %s and tch.teacher = t.id"
                curs.execute(sql, (i))
                rows = curs.fetchall()
                for row in rows:
                    pass

                strtime = int(strftime("%H%M", localtime()))
                if(910<= strtime <= 950):
                    schedule+=day+"1"
                elif(1000 <= strtime <= 1040):
                    schedule+=day+"2"
                elif (1050 <= strtime <= 1130):
                    schedule += day + "3"
                elif (1140 <= strtime <= 1220):
                    schedule += day + "4"
                elif (1330 <= strtime <= 1410):
                    schedule += day + "5"
                elif (1420 <= strtime <= 1500):
                    schedule += day + "6"
                elif (1510 <= strtime <=1550):
                    schedule += day + "7"
                elif(246==strtime):
                    schedule += day + "2"
                else:
                    row[schedule] = None
                mycursor = conn.cursor()
                sql2 = "UPDATE teacherseat set status=%s where seatnum = %s"

                if(row[schedule] == None):
                    data = (1, i)
                    mycursor.execute(sql2, data)
                else:
                    data = (0, i)
                    mycursor.execute(sql2, data)

                conn.commit()

    def getTeacherName(self, seatnum):
        sql = "select * from tschedule AS t JOIN teacherseat AS tch WHERE tch.seatnum = %s and tch.teacher = t.id"
        curs.execute(sql, (seatnum))

        rows = curs.fetchall()
        for row in rows:
            return row['name']

    def getStatusColor(self, seatnum):
        str = "background-color: "
        sql = "select * from teacherseat where seatnum = %s"
        curs.execute(sql, (seatnum))

        rows = curs.fetchall()
        for row in rows:
            if  row['status'] == -1:
                str += "gray"
            elif row['status'] == 1:
                str += "lightgreen"
            elif row['status'] != 1:
                str += "red"
        print(str)
        return str
        conn.close()


    def statusButtonClicked1(self):
        seat = str(self.sender().objectName()).split('_')
        seatnum = seat[-1]
        self.showStatus(seatnum)

    def showStatus(self,seatnum):
        sql = "select * from teacherseat where seatnum="+seatnum
        curs.execute(sql)
        rows = curs.fetchall()
        for row in rows:
            pass
        if row['teacher'] != 0:
            self.statusWindow = StatusClass(seatnum)
            self.statusWindow.show()


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    #WindowClass의 인스턴스 생성
    main_window = WindowClass()
    #프로그램 화면을 보여주는 코드
    main_window.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()