import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
label = QLabel("연동 성공")
label.show()

print("Before event loop")
app.exec_()
print("After event loop")