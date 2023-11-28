import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("my_qt09.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb.clicked.connect(self.button_clicked)
        self.com = self.random()
        print(self.com)
        
    def random(self):
        num = list(range(1,9+1))
        
        for i in range(1000) :
            rnd = int(random()*9)
            temp = num[0]
            num[0] = num[rnd]
            num[rnd] = temp
        com = "{}{}{}".format(num[0],num[1],num[2])
        return com
        
    def getStrike(self,me,com):
        ret = 0
        m1 = me[0:1]
        m2 = me[1:2]
        m3 = me[2:3]
        
        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]
        
        if m1 == c1 : ret += 1
        if m2 == c2 : ret += 1
        if m3 == c3 : ret += 1
        
        return ret
    
    def getBall(self,me,com):
        ret = 0
        m1 = me[0:1]
        m2 = me[1:2]
        m3 = me[2:3]
        
        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]
        
        if m1 == c2 or m1 == c3 : ret += 1
        if m2 == c1 or m2 == c3 : ret += 1
        if m3 == c1 or m3 == c2 : ret += 1
        
        return ret
    
    def button_clicked(self):
        me = self.le.text()
        s = self.getStrike(me, self.com)
        b = self.getBall(me, self.com)
        self.te.setText("{}--------{}S{}B".format(me,s,b))
            
        if s == 3 :
            QMessageBox.about(self,"정답","축하합니다.")
            self.te.setText("{}--------{}S{}B".format(me,self.s, self.b))

            
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
