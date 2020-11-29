import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *

dir = os.path.dirname(os.getcwd())

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exit = QAction(QIcon(dir+'/Images/delete.png'),'&Exit',self)
        exit.setShortcut('Ctrl+e')
        exit.setStatusTip('Exit application')
        exit.triggered.connect(QApplication.quit())

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exit)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    screen = app.primaryScreen()
    size = screen.size()
    w, h = 300,300
    ex.setGeometry(size.width()/2-w/2, size.height()/2-h/2,w,h)
    sys.exit(app.exec_())