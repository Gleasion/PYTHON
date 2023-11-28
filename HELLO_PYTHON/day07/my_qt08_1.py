import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random


#UI파일 연결
form_class = uic.loadUiType("my_qt08.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.com = int(random()*99)+1
        self.setupUi(self)
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.MyClick)
        
    #pb가 눌리면 작동할 함수
    def MyClick(self) :
        mine = self.le.text()
        m = int(mine)
        txt = ""
        if self.com>m :
            txt = mine + "-----------UP\n"
        elif self.com<m :
            txt = mine + "---------DOWN\n"
        else :
            txt = mine + "------CORRECT\n"
        
        
        str_old = self.te.toPlainText()
        self.te.setText(str_old + txt)
        self.le.setText("")
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()