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
            self.warning.setText("")
            self.statusWindow = EditStatusClass(self.seat)
            self.statusWindow.show()
            self.accept()
        else:
            self.warning.setText("* 비밀번호가 틀렸습니다. 다시 입력해주세요")

    def showModal(self):
        return super().exec_()