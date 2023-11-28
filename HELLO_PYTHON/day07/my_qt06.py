import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("my_qt06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.button_clicked)
    
    def drawStar(self,cnt):
        ret = ""
        for i in range(cnt):
            ret += "*";
        ret += "\n"
        return ret
    
    def button_clicked(self):
        first = int(self.pteFrist.toPlainText())
        last = int(self.pteLast.toPlainText())
        
        star= ""
        
        for i in range(first, last+1) :
            star += self.drawStar(i)
    
        self.te.setText(star)

if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
