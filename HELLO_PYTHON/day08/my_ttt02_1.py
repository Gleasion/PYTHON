import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.Qt import QSize

form_class = uic.loadUiType("my_ttt02.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag_xo = True
        self.flag_over = False
        self.arr2d = [
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ]
        self.pb2d = []
        self.pb.clicked.connect(self.myreset)
        
        for i in range(3) :
            line = []
            for j in range(3) :
                pb = QPushButton("", self)
                pb.setToolTip("{},{}".format(i,j))
                pb.setIcon(QIcon('0.png'))
                pb.setIconSize(QSize(40,40))
                pb.setGeometry(j*42,i*42,40,40)
                pb.clicked.connect(self.mclick)
                line.append(pb)
            self.pb2d.append(line)
    
    def myrender(self):
        for i in range(3) :
            for j in range(3) :
                if self.arr2d[i][j] == 0:
                    self.pb2d[i][j].setIcon(QIcon('0.png'))
                elif self.arr2d[i][j] == 1 :
                    self.pb2d[i][j].setIcon(QIcon('1.png'))
                elif self.arr2d[i][j] == 2:
                    self.pb2d[i][j].setIcon(QIcon('2.png'))
    
    def myreset(self):
        for i in range(3) :
            for j in range(3) :
                self.arr2d[i][j] = 0
        self.myrender()
        self.flag_over = False
        self.flag_xo = True
    
    def mclick(self):
        if self.flag_over :
            return
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2d[i][j] > 0 :
            return
        if self.flag_xo :
            self.arr2d[i][j] = 1
        else : 
            self.arr2d[i][j] = 2
        self.myrender()
        
        flag_over = self.isOver()
        
        if flag_over :
            if self.flag_xo :
                QMessageBox.about(self, "tiktaktoe", "X 승리")
            else:
                QMessageBox.about(self, "tiktaktoe", "O 승리")
            self.flag_over = True
        
        self.flag_xo = not self.flag_xo
        
    def isOver(self):
        xo = 2
        if self.flag_xo :
            xo = 1
        
        a2 = self.arr2d
        
        if a2[0][0] == xo and a2[0][1] == xo and a2[0][2] == xo : return True
        if a2[1][0] == xo and a2[1][1] == xo and a2[1][2] == xo : return True
        if a2[2][0] == xo and a2[2][1] == xo and a2[2][2] == xo : return True
        
        if a2[0][0] == xo and a2[1][0] == xo and a2[2][0] == xo : return True
        if a2[0][1] == xo and a2[1][1] == xo and a2[2][1] == xo : return True
        if a2[0][2] == xo and a2[1][2] == xo and a2[2][2] == xo : return True
        
        if a2[0][0] == xo and a2[1][1] == xo and a2[2][2] == xo : return True
        if a2[2][0] == xo and a2[1][1] == xo and a2[0][2] == xo : return True
     
        return False
        
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
