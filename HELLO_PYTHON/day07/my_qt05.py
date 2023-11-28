import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("my_qt05.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.button_clicked)
        
    def button_clicked(self):
        num = list(range(1,45+1))
        
        for i in range(1000):
            temp = num[0]
            rnd = int(random()*45)
            num[0] = num[rnd]
            num[rnd] = temp
        
        self.le1.setText(str(num[0]))
        self.le2.setText(str(num[1]))
        self.le3.setText(str(num[2]))
        self.le4.setText(str(num[3]))
        self.le5.setText(str(num[4]))
        self.le6.setText(str(num[5]))

if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
