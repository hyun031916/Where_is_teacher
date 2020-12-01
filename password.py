import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import pymysql
from edit_status import EditStatusClass
#모듈 불러오기

conn = pymysql.connect(host="192.168.0.9", port=3307, user='newuser', password='zxcdsaqwe7845', db='python', charset="utf8")
# conn = pymysql.connect(host="localhost", port=3307, user='root', password='1111', db='python', charset="utf8")
curs = conn.cursor(pymysql.cursors.DictCursor)


#UI 파일 연결
status_ui = uic.loadUiType("password_window.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class PasswordClass(QDialog, status_ui) :
    def __init__(self, seatnum) :
        self.seat = seatnum
        super().__init__()
        self.setupUi(self)
        #전송 버튼 클릭 시
        self.checkPassword.clicked.connect(self.checkPass)


    def checkPass(self):
        if(self.tePassword.toPlainText()=="1111"):
            print("성공")
            self.warning.setText("")
            self.statusWindow = EditStatusClass(self.seat)
            self.statusWindow.show()
            StatusClass.status_ui = uic.loadUi("edit_status.ui")
        else:
            self.warning.setText("* 비밀번호가 틀렸습니다. 다시 입력해주세요")

# if __name__ == "__main__" :
#     #QApplication : 프로그램을 실행시켜주는 클래스
#     app = QApplication(sys.argv)
#     #WindowClass의 인스턴스 생성
#     main_window = PasswordClass(23)
#     #프로그램 화면을 보여주는 코드
#     main_window.show()
#     #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
#     app.exec_()