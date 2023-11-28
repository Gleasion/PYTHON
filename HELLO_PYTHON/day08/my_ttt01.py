import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.Qt import QSize

form_class = uic.loadUiType("my_ttt01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myreset)
        
        for i in range(3) :
            for j in range(3) :
                pb = QPushButton("", self)
                pb.setIcon(QIcon('0.png'))
                pb.setIconSize(QSize(40,40))
                pb.setGeometry(i*42,j*42,40,40)
                pb.clicked.connect(self.mclick)
            
        self.flag_XO = True
        
    def mclick(self):
        if(self.flag_XO) :
            self.sender().setIcon(QIcon('1.png'))
            #self.flag_XO = False
        else :
            self.sender().setIcon(QIcon('2.png'))
            #self.flag_XO = True
        
        self.flag_XO = not self.flag_XO
            
    def myreset(self):
        self.sender().setIcon(QIcon('0.png'))
        
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
