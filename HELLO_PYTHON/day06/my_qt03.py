import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("my_qt03.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.button_clicked)
        
    def button_clicked(self):
        dan = int(self.le.text())
        
        txt = ""
        for i in range(1,9):
            txt += "{} * {} = {}\n".format(dan,i,dan*i)
            self.te.setText(txt)

if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
