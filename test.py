import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import datetime


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('시작')
        btn1.clicked.connect(self.start_btn) # 함수와 버튼 연결

        btn2 = QPushButton('종료')
        btn2.clicked.connect(self.end_btn)

        btn3 = QPushButton('완전 종료')
        btn3.clicked.connect(self.close_btn)

        btn4 = QPushButton('리셋')
        btn4.clicked.connect(self.reset_btn)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        groupbox1 = QGroupBox('시작 시간')
        self.bx1 = QVBoxLayout()
        groupbox1.setLayout(self.bx1)

        groupbox2 = QGroupBox('종료 시간')
        self.bx2 = QVBoxLayout()
        groupbox2.setLayout(self.bx2)

        groupbox3 = QGroupBox('총 시간')
        self.bx3 = QVBoxLayout()
        groupbox3.setLayout(self.bx3)

        groupbox4 = QGroupBox('논 시간')
        self.bx4 = QVBoxLayout()
        groupbox4.setLayout(self.bx4)

        hbox = QHBoxLayout()
        hbox.addWidget(groupbox1)
        hbox.addWidget(groupbox2)
        hbox.addWidget(groupbox3)
        hbox.addWidget(groupbox4)
        hbox.addLayout(vbox)

        self.setWindowTitle('Chronometry')
        self.setLayout(hbox)
        self.setGeometry(100, 100, 600, 150)
        self.show()

    def start_btn(self):
        if self.bx1.count() > self.bx2.count() or (self.bx3.count() >= 1 and self.bx4.count() >= 1):
            return
        start_time = QTime.currentTime()
        self.bx1.addWidget(QLabel(start_time.toString()))

    def end_btn(self):
        if self.bx2.count() >= self.bx1.count() or (self.bx3.count() >= 1 and self.bx4.count() >= 1):
            return
        end_time = QTime.currentTime()
        self.bx2.addWidget(QLabel(end_time.toString()))

    def close_btn(self):
        if self.bx3.count() >= 1 or self.bx4.count() >= 1:
            return
        bx1_count = self.bx1.count()
        bx2_count = self.bx2.count()
        if bx1_count != bx2_count or (bx1_count == 0 or bx2_count == 0):
            return
        bx1_list = []
        bx2_list = []
        sum = 0
        for i in range(bx1_count):
            bx1_list.append(self.bx1.itemAt(i).widget().text())
            bx2_list.append(self.bx2.itemAt(i).widget().text())
            sum += time_cal(bx1_list[i], bx2_list[i])
        self.bx3.addWidget(QLabel(str(datetime.timedelta(seconds=sum))))
        play = time_cal(bx1_list[0], bx2_list[bx2_count - 1]) - sum
        self.bx4.addWidget(QLabel(str(datetime.timedelta(seconds=play))))

    def reset_btn(self):
        for i in range(self.bx1.count()):
            self.bx1.itemAt(i).widget().deleteLater()
        for i in range(self.bx2.count()):
            self.bx2.itemAt(i).widget().deleteLater()
        for i in range(self.bx3.count()):
            self.bx3.itemAt(i).widget().deleteLater()
        for i in range(self.bx4.count()):
            self.bx4.itemAt(i).widget().deleteLater()


def time_cal(a, b):
    a = a.split(':')
    b = b.split(':')
    a_s = int(a[0]) * 3600 + int(a[1]) * 60 + int(a[2])
    b_s = int(b[0]) * 3600 + int(b[1]) * 60 + int(b[2])
    return b_s - a_s


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())