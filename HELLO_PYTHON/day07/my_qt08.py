import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("my_qt08.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.txt = ""
        self.rnd = int(random() * 99)+1
        self.cnt = 0
        self.pb.clicked.connect(self.button_clicked)
        
    def restart(self):
        self.txt = ""
        self.rnd = int(random() * 99)
        self.te.setText("")
        self.le.setText("")
    
    def button_clicked(self):
        num = int(self.le.text())
        print(self.rnd)
        
        if num > self.rnd :
            self.txt += "DOWN입니다.\n"
            self.te.setText(self.txt)
            self.cnt += 1;
        elif num < self.rnd :
            self.txt += "UP입니다.\n"
            self.te.setText(self.txt)
            self.cnt += 1;
        elif num == self.rnd :
            QMessageBox.about(self, "정답", "맞췄습니다.")
            self.restart()
            
        if(self.cnt > 10) :
            QMessageBox.about(self, "10회", "GAME OVER")
            self.restart()
            
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
