import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
main_ui = uic.loadUiType("start.ui")[0]
option_ui = uic.loadUiType("status.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, main_ui):
    btn = 0
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.startButton.clicked.connect(self.showTeacherRoom)

        #self.pushButton_3.move(100,100)

    def showTeacherRoom(self):
        main_ui = uic.loadUi("teacherroom.ui", self)
        self.seat_1.clicked.connect(self.statusButtonClicked1)
        self.seat_2.clicked.connect(self.statusButtonClicked1)
        self.seat_3.clicked.connect(self.statusButtonClicked1)
        self.seat_4.clicked.connect(self.statusButtonClicked1)
        self.seat_5.clicked.connect(self.statusButtonClicked1)

    def statusButtonClicked1(self):
        seat = str(self.sender().objectName()).split('_')
        seatnum = seat[-1]
        self.showStatus(seatnum)

    def showStatus(self,seatnum):
        print(seatnum)

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    #WindowClass의 인스턴스 생성
    main_window = WindowClass()
    #프로그램 화면을 보여주는 코드
    main_window.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()