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
        self.arr2d = [
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ]
        self.pb2d = []
        self.flag_xo = True
        self.flag_win = False
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
    
        self.myrender()
        
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
        self.flag_win = False
        self.flag_xo = True
    
    def mclick(self):
        str_xy = self.sender().toolTip().split(",")
        i = int(str_xy[0])
        j = int(str_xy[1])
        
        if self.flag_win :
            return
        
        if self.arr2d[i][j] > 0 :
            return
        
        if(self.flag_xo) :
            self.arr2d[i][j] = 1
            self.flag_xo = False
        
        else : 
            self.arr2d[i][j] = 2
            self.flag_xo = True
        
        self.myrender()
    
        flag_win = self.isWin()
        
    def isWin(self) :
        i = range(3)
        j = range(3)
        
        if (self.arr2d[i][0] and self.arr2d[i][1] and self.arr2d[i][2]) == 1 :
            QMessageBox.about(self,"","X 승리하였습니다")
            self.flag_win = True
        if (self.arr2d[0][j] and self.arr2d[1][j] and self.arr2d[2][j]) == 1 :
            QMessageBox.about(self,"","X 승리하였습니다")
            self.flag_win = True
        if (self.arr2d[0][0] and self.arr2d[1][1] and self.arr2d[2][2]) == 1 :
            QMessageBox.about(self, "","X 승리하였습니다")
            self.flag_win = True
        if (self.arr2d[0][2] and self.arr2d[1][1] and self.arr2d[2][0]) == 1 :
            QMessageBox.about(self,"","X 승리하였습니다")
            self.flag_win = True
        if (self.arr2d[i][0] and self.arr2d[i][1] and self.arr2d[i][2]) == 2 :
            QMessageBox.about(self,"","O 승리하였습니다")
            self.flag_win = True
        if (self.arr2d[0][j] and self.arr2d[1][j] and self.arr2d[2][j]) == 2 :
            QMessageBox.about(self,"","O 승리하였습니다")
            self.flag_win = True
        if (self.arr2d[0][0] and self.arr2d[1][1] and self.arr2d[2][2]) == 2 :
            QMessageBox.about(self, "","O 승리하였습니다")
            self.flag_win = True
        if (self.arr2d[0][2] and self.arr2d[1][1] and self.arr2d[2][0]) == 2 :
            QMessageBox.about(self,"","O 승리하였습니다")
            self.flag_win = True
            
        return False
    
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
