import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("my_qt07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.num = ""
        
        self.pb1.clicked.connect(self.pb1_clicked)
        self.pb2.clicked.connect(self.pb2_clicked)
        self.pb3.clicked.connect(self.pb3_clicked)
        self.pb4.clicked.connect(self.pb4_clicked)
        self.pb5.clicked.connect(self.pb5_clicked)
        self.pb6.clicked.connect(self.pb6_clicked)
        self.pb7.clicked.connect(self.pb7_clicked)
        self.pb8.clicked.connect(self.pb8_clicked)
        self.pb9.clicked.connect(self.pb9_clicked)
        self.pb0.clicked.connect(self.pb0_clicked)
        
        self.pbCall.clicked.connect(self.pbCall_clicked)
            
    def pb1_clicked(self):
        self.num += self.pb1.text()
        self.le.SetText(str(self.num))
        
    def pb2_clicked(self):
        self.num += self.pb2.text()
        self.le.SetText(str(self.num))
    
    def pb3_clicked(self):
        self.num += self.pb3.text()
        self.le.SetText(str(self.num))
    
    def pb4_clicked(self):
        self.num += self.pb4.text()
        self.le.SetText(str(self.num))
    
    def pb5_clicked(self):
        self.num += self.pb5.text()
        self.le.SetText(str(self.num))
    
    def pb6_clicked(self):
        self.num += self.pb6.text()
        self.le.SetText(str(self.num))
    
    def pb7_clicked(self):
        self.num += self.pb7.text()
        self.le.SetText(str(self.num))
    
    def pb8_clicked(self):
        self.num += self.pb8.text()
        self.le.SetText(str(self.num))
        
    def pb9_clicked(self):
        self.num += self.pb9.text()
        self.le.SetText(str(self.num))
        
    def pb0_clicked(self):
        self.num += self.pb0.text()
        self.le.SetText(str(self.num))
    
    def pbCall_clicked(self):
        QMessageBox.about(self, "calling", "{} 번호로 전화중".format(str(self.num)))

if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
