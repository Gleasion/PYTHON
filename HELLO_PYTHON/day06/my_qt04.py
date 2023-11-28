import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("my_qt04.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.button_clicked)
        
    def button_clicked(self):
        me = self.pteMine.toPlainText()
        
        com = ["홀","짝"]
                
        for i in range(100):
            temp = com[0]
            rnd = int(random()*2)
            com[0] = com[rnd]
            com[rnd] = temp
            
        txt = com[0]
        self.pteCom.setPlainText(str(com[0]))
        
        if me == txt :
            self.pteResult.setPlainText("이겼습니다.")
        else :
            self.pteResult.setPlainText("졌습니다.")

if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
