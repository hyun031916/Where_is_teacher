import sys
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
curs = conn.cursor(pymysql.cursors.DictCursor)

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, main_ui):
    window = 0
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.startButton.clicked.connect(self.showTeacherRoom)

        #self.pushButton_3.move(100,100)
    def ontimeout(self):
        print('hello')
        self.repaint()

    def showTeacherRoom(self):
        main_ui = uic.loadUi("teacherroom.ui", self)
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
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.ontimeout)
        self.__timer.start(1000)

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
            if row['status'] == 1:
                str += "lightgreen"
            elif row['status'] == 0:
                str += "red"
        print(str)
        return str
        conn.close()


    def statusButtonClicked1(self):
        seat = str(self.sender().objectName()).split('_')
        seatnum = seat[-1]
        self.showStatus(seatnum)

    def showStatus(self,seatnum):
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