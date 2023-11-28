import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import randint, random

form_class = uic.loadUiType("my_qt06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
      
    def drwStar(self,cnt):
        
        ret = ""
        for i in range(cnt):
            ret += "*"
        ret += "\n"
        return ret
        
    def myclick(self):
        a = self.pteFirst.toPlainText()
        b = self.pteLast.toPlainText()
        
        aa = int(a)
        bb = int(b)
        
        str = ""
        
        for i in range(aa,bb+1):
            str += self.drwStar(i)
        
        self.te.setPlainText(str)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())