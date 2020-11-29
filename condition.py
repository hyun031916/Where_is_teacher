import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 improt uic

import pymysql

#UI 파일 연결
form_class = uic.loadUiType("status_window.ui")



#모듈 불러오기

conn = pymysql.connect(host="127.0.0.1", port=3307, user='root', password='1111', db='python', charset="utf8")

curs = conn.cursor(pymysql.cursors.DictCursor)

sql = "select * from tschedule where id = %s"
curs.execute(sql, (1))

rows = curs.fetchall()
for row in rows:
    print(row)
    print(row['name'])
conn.close()
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        #label
        label1 = QLabel(row['name']+'선생님', self)
        label1.setAlignment(Qt.AlignVCenter)

        label2 = QLabel('선생님', self)
        font1 = label1.font()
        font1.setPointSize(20)
        label1.setFont(font1)

        layout = QVBoxLayout()
        layout.addWidget(label1)

        btn1 = QPushButton("닫기", self)
        btn1.move(20, 20)
        btn1.clicked.connect(QCoreApplication.instance().quit)

        self.setLayout(layout)

        #창의 제목
        self.setWindowTitle('선생님 상태')
        #위젯을 스크린의 x, y 위치로 이동
        self.move(300, 300)
        #위젯 크기를 너비, 높이로 조절
        self.resize(400, 200)
        #위젯을 스크린에 보여줌
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())