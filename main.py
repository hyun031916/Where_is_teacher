import sys
from time import localtime, strftime
import calendar
from datetime import date

import pymysql
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from condition import StatusClass

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
main_ui = uic.loadUiType("start.ui")[0]

# conn = pymysql.connect(host="192.168.0.9", port=3307, user='newuser', password='zxcdsaqwe7845', db='python',charset="utf8")
conn = pymysql.connect(host="127.0.0.1", port=3307, user='root', password='1111', db='python', charset="utf8")

curs = conn.cursor(pymysql.cursors.DictCursor)

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.__timer = QTimer()
        self.resetInfo()
        self.statusBar()
        self.setupUi(self)
        self.startButton.clicked.connect(self.showTeacherRoom1)

    def resetInfo(self):
        for i in range(1, 30 + 1):
            sql = "select * from teacherseat where seatnum=" + str(i)
            curs.execute(sql)
            rows = curs.fetchall()
            for row in rows:
                pass
            if row['teacher'] != 0:
                mycursor = conn.cursor()
                sql2 = "UPDATE teacherseat set status=%s where seatnum = %s"
                data = (1, i)
                mycursor.execute(sql2, data)

                mycursor = conn.cursor()
                sql2 = "UPDATE teacherseat set message=%s where seatnum = %s"
                data = ("", i)
                mycursor.execute(sql2, data)

                conn.commit()
            else:
                continue

    def showTeacherRoom1(self):
        strtime = int(strftime("%H%M", localtime()))
        if strtime == 910 or strtime == 950 or strtime == 1000 or strtime == 1040 \
                or strtime == 1050 or strtime == 1130 or strtime == 1140 or strtime == 1220 \
                or strtime == 1330 or strtime == 1410 or strtime == 1420 or strtime == 1500 \
                or strtime == 1510 or strtime == 1550:  # 테스트떄 수정
            self.statusBar()

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
        self.seat_9.clicked.connect(self.statusButtonClicked1)
        self.seat_9.setText(self.getTeacherName(9))
        self.seat_9.setStyleSheet(self.getStatusColor(9))
        self.seat_10.clicked.connect(self.statusButtonClicked1)
        self.seat_10.setText(self.getTeacherName(10))
        self.seat_10.setStyleSheet(self.getStatusColor(10))
        self.seat_11.setText(self.getTeacherName(11))
        self.seat_11.setStyleSheet(self.getStatusColor(11))
        self.seat_12.clicked.connect(self.statusButtonClicked1)
        self.seat_12.setText(self.getTeacherName(12))
        self.seat_12.setStyleSheet(self.getStatusColor(12))
        self.seat_13.clicked.connect(self.statusButtonClicked1)
        self.seat_13.setText(self.getTeacherName(13))
        self.seat_13.setStyleSheet(self.getStatusColor(13))
        self.seat_14.clicked.connect(self.statusButtonClicked1)
        self.seat_14.setText(self.getTeacherName(14))
        self.seat_14.setStyleSheet(self.getStatusColor(14))
        self.seat_15.clicked.connect(self.statusButtonClicked1)
        self.seat_15.setText(self.getTeacherName(15))
        self.seat_15.setStyleSheet(self.getStatusColor(15))
        self.seat_16.clicked.connect(self.statusButtonClicked1)
        self.seat_16.setText(self.getTeacherName(16))
        self.seat_16.setStyleSheet(self.getStatusColor(16))
        self.seat_17.clicked.connect(self.statusButtonClicked1)
        self.seat_17.setText(self.getTeacherName(17))
        self.seat_17.setStyleSheet(self.getStatusColor(17))
        self.seat_18.clicked.connect(self.statusButtonClicked1)
        self.seat_18.setText(self.getTeacherName(18))
        self.seat_18.setStyleSheet(self.getStatusColor(18))
        self.seat_19.clicked.connect(self.statusButtonClicked1)
        self.seat_19.setText(self.getTeacherName(19))
        self.seat_19.setStyleSheet(self.getStatusColor(19))
        self.seat_20.clicked.connect(self.statusButtonClicked1)
        self.seat_20.setText(self.getTeacherName(20))
        self.seat_20.setStyleSheet(self.getStatusColor(20))
        # self.__timer.stop()
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.showTeacherRoom1)
        self.__timer.start(1000)

    def showTeacherRoom2(self):
        strtime = int(strftime("%H%M", localtime()))
        if strtime == 910 or strtime == 950 or strtime == 1000 or strtime == 1040 \
                or strtime == 1050 or strtime == 1130 or strtime == 1140 or strtime == 1220 \
                or strtime == 1330 or strtime == 1410 or strtime == 1420 or strtime == 1500 \
                or strtime == 1510 or strtime == 1550:  # 테스트떄 수정
            self.statusBar()

        main_ui = uic.loadUi("teacherroom2.ui", self)

        self.leftButton1.clicked.connect(self.showTeacherRoom1)
        self.rightButton1.clicked.connect(self.showTeacherRoom1)

        self.seat_21.clicked.connect(self.statusButtonClicked1)
        self.seat_21.setText(self.getTeacherName(21))
        self.seat_21.setStyleSheet(self.getStatusColor(21))
        self.seat_22.clicked.connect(self.statusButtonClicked1)
        self.seat_22.setText(self.getTeacherName(22))
        self.seat_22.setStyleSheet(self.getStatusColor(22))
        self.seat_23.clicked.connect(self.statusButtonClicked1)
        self.seat_23.setText(self.getTeacherName(23))
        self.seat_23.setStyleSheet(self.getStatusColor(23))
        self.seat_24.clicked.connect(self.statusButtonClicked1)
        self.seat_24.setText(self.getTeacherName(24))
        self.seat_24.setStyleSheet(self.getStatusColor(2))
        self.seat_25.clicked.connect(self.statusButtonClicked1)
        self.seat_25.setText(self.getTeacherName(25))
        self.seat_25.setStyleSheet(self.getStatusColor(25))
        self.seat_26.clicked.connect(self.statusButtonClicked1)
        self.seat_26.setText(self.getTeacherName(26))
        self.seat_26.setStyleSheet(self.getStatusColor(26))
        self.seat_27.clicked.connect(self.statusButtonClicked1)
        self.seat_27.setText(self.getTeacherName(27))
        self.seat_27.setStyleSheet(self.getStatusColor(27))
        self.seat_28.clicked.connect(self.statusButtonClicked1)
        self.seat_28.setText(self.getTeacherName(28))
        self.seat_28.setStyleSheet(self.getStatusColor(28))
        self.seat_29.clicked.connect(self.statusButtonClicked1)
        self.seat_29.setText(self.getTeacherName(29))
        self.seat_29.setStyleSheet(self.getStatusColor(29))
        self.seat_30.clicked.connect(self.statusButtonClicked1)
        self.seat_30.setText(self.getTeacherName(30))
        self.seat_30.setStyleSheet(self.getStatusColor(30))
        self.__timer.stop()
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.showTeacherRoom2)
        self.__timer.start(1000)

    def statusBar(self):
        my_date = date.today()
        day = calendar.day_name[my_date.weekday()]

        for i in range(1, 30 + 1):
            schedule = ""
            sql = "select * from teacherseat where seatnum=" + str(i)
            curs.execute(sql)
            rows = curs.fetchall()
            for info in rows:
                pass
            if info['teacher'] != 0:
            # if row['teacher'] != 0:
                sql = "select * from tschedule AS t JOIN teacherseat AS tch WHERE tch.seatnum = %s and tch.teacher = t.id"
                curs.execute(sql, (i))
                rows = curs.fetchall()
                for row in rows:
                    pass

                strtime = int(strftime("%H%M", localtime()))
                if (910 <= strtime <= 950):
                    schedule += day + "1"
                elif (1000 <= strtime <= 1040):
                    schedule += day + "2"
                elif (1050 <= strtime <= 1130):
                    schedule += day + "3"
                elif (1140 <= strtime <= 1220):
                    schedule += day + "4"
                elif (1330 <= strtime <= 1410):
                    schedule += day + "5"
                elif (1420 <= strtime <= 1500):
                    schedule += day + "6"
                elif (1510 <= strtime <= 1550):
                    schedule += day + "7"
                elif (1510 <= strtime <= 1550):
                    schedule += day + "7"
                else:
                    row[schedule] = None
                if strtime == 950 or strtime == 1040 or strtime == 1130 or strtime == 1220 \
                        or strtime == 1410 or strtime == 1500 or strtime == 1550:  # 테스트떄 수정
                    row[schedule] = None
                mycursor = conn.cursor()
                sql2 = "UPDATE teacherseat set status=%s where seatnum = %s"
                sql3 = "UPDATE teacherseat set message=%s where seatnum = %s"
                # elif (246 == strtime):
                #     schedule += day + "2"

                mycursor = conn.cursor()
                sql2 = "UPDATE teacherseat set status=%s where seatnum = %s"

                if (row[schedule] == None):
                    data = (1, i)
                    mycursor.execute(sql2, data)

                    data = ('', i)
                    mycursor.execute(sql3, data)
                else:
                    data = (0, i)
                    mycursor.execute(sql2, data)

                    data = (row[schedule], i)
                    mycursor.execute(sql3, data)

                conn.commit()
            else:
                continue

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
            if row['status'] == -1:
                str += "gray"
            elif row['status'] == 1:
                str += "lightgreen"
            elif row['status'] != 1:
                str += "red"
        print(str)
        print(row['status'])
        conn.commit()
        return str
        conn.close()


    def statusButtonClicked1(self):
        seat = str(self.sender().objectName()).split('_')
        seatnum = seat[-1]
        self.showStatus(seatnum)

    def showStatus(self, seatnum):
        sql = "select * from teacherseat where seatnum=" + seatnum
        curs.execute(sql)
        rows = curs.fetchall()
        for row in rows:
            pass
        if row['teacher'] != 0:
            self.statusWindow = StatusClass(seatnum)
            self.statusWindow.show()


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    main_window = WindowClass()
    # 프로그램 화면을 보여주는 코드
    main_window.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()