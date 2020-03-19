import sys
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import shutil
import os.path

class Window3(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("<h3> 3 X 3 Matrix <h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(500,50)
        self.label.move(150, 20) #gumana na sana to isa pa

        self.history = open("Determinant History.txt", 'w')
        self.history.write("History\n")
        self.history.close()
       

        self.setWindowTitle("Determinant Calculator")
        self.setGeometry(420, 100, 500, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(80, 80)
        self.textbox1.resize(100,30)
        

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(180, 80)
        self.textbox2.resize(100,30)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(280,80)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(80, 110)
        self.textbox4.resize(100,30)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(180, 110)
        self.textbox5.resize(100,30)

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(280, 110)
        self.textbox6.resize(100,30)

        self.textbox7 = QLineEdit(self)
        self.textbox7.move(80, 140)
        self.textbox7.resize(100,30)

        self.textbox8 = QLineEdit(self)
        self.textbox8.move(180, 140)
        self.textbox8.resize(100,30)

        self.textbox9 = QLineEdit(self)
        self.textbox9.move(280, 140)
        self.textbox9.resize(100,30)

        self.det = QLineEdit(self)
        self.det.setText("")
        self.det.move(380, 170)
        self.det.resize(100, 30)

        self.text = QLabel("<h3>Determinant:<h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(265, 175)
        self.text.resize(120, 30)
        
        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Submit input")
        self.button.move(50,350)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Clear all ")
        self.button.move(200,350)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(350,350)
        self.button.clicked.connect(self.back) 

        self.button = QPushButton('History', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Determinant History")
        self.button.move(200,400)
        self.button.clicked.connect(self.DHistory) 

        

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(680,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()

    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
        self.textbox6.setText("")
        self.textbox7.setText("")
        self.textbox8.setText("")
        self.textbox9.setText("")
        self.det.setText("")
        

    def data(self):
        if self.textbox1.text() != "" and self.textbox2.text() != "" and self.textbox3.text() != "" and self.textbox4.text() != "" and self.textbox5.text() != "" and self.textbox6.text() != "" and self.textbox7.text() != "" and self.textbox8.text() != "" and self.textbox9.text() != "":
            a = int(self.textbox1.text())
            b = int(self.textbox2.text())
            c = int(self.textbox3.text())
            d = int(self.textbox4.text())
            e = int(self.textbox5.text())
            f = int(self.textbox6.text())
            g = int(self.textbox7.text())
            h = int(self.textbox8.text())
            i = int(self.textbox9.text())
            self.matrix_computation(a, b, c, d, e, f, g, h, i)
        elif self.textbox1.text() == "" and self.textbox2.text() == "" and self.textbox3.text() == "" and self.textbox4.text()== "" and self.textbox5.text() == "" and self.textbox6.text() == "" and self.textbox7.text() == "" and self.textbox8.text() == "" and self.textbox9.text() == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)
        elif self.textbox1.text() == "" or self.textbox2.text() == "" or self.textbox3.text() == "" or self.textbox4.text() == "" or self.textbox5.text() == "" or self.textbox6.text() == "" or self.textbox7.text() == "" or self.textbox8.text() == "" or self.textbox9.text() == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)
    def back(self):
        Window3.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = Window()
        self.mnwndw.show()
    def DHistory(self):
        self.open = DHistory()
        self.open.show()
    def matrix_computation(self, a ,b ,c, d, e, f, g, h, i):
        A = (a*e*i)
        B = (b*f*g)
        C = (c*d*h)
        D = (c*e*g)
        E = (a*f*h)
        F = (b*d*i)

        Determinate = (A + B + C) - (D + E + F)
        self.det.setText(f"{Determinate}")
        submitting = QMessageBox.information(self, "Processing", "Data being processed. Do you wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes )
        if submitting == QMessageBox.Yes and a != "" and b != "" and c != "" and d != "" and e != "" and f != "" and g != "" and h != "" and i != "":
            self.history = open("Determinant History.txt", 'a')
            self.history.write("Inputs\n" + str(a) + "\n")
            self.history.write(str(b) + "\n")
            self.history.write(str(c) + "\n")
            self.history.write(str(d) + "\n")
            self.history.write(str(e) + "\n")
            self.history.write(str(f) + "\n")
            self.history.write(str(g) + "\n")
            self.history.write(str(h) + "\n")
            self.history.write(str(i) + "\n")
            self.history.write("Determinate is \n" + str(Determinate))
            self.history.close()
            QMessageBox.information(self, "Processed", "Data has been processed", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and a == "" and b == "" and c == "" and d == "" and e == "" and f == "" and g == "" and h == "" and i == "":
            pass
        elif submitting == QMessageBox.No and a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == "" or i == "":
            QMessageBox.warning(self, "Blank Field", "Please don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)

class DHistory(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("<h3> 3 x 3 History <h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(500,50)
        self.label.move(150, 20)

        self.setWindowTitle("Determinant History")
        self.setGeometry(420, 100, 500, 500)

        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.history = open("Determinant History.txt", 'r')
            self.history.read()
            self.history.close()
        else:
            QMessageBox.warning(self, "Does not exist", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)
        
        self.setWindowIcon(QIcon('custom.ico'))
        self.textans = QTextEdit(self)
        self.textans.setText("")
        self.textans.resize(450, 350)

        self.pushButton = QPushButton("Clear", self)
        self.pushButton.move(50, 370)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Clear History")

        self.pushButton.clicked.connect(self.del_rec)

        self.pushButton = QPushButton("Show", self)
        self.pushButton.move(150, 370)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Show History")

        self.pushButton.clicked.connect(self.show_his)

        self.pushButton = QPushButton("Exit", self)
        self.pushButton.move(350, 370)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Close Window")

        self.pushButton.clicked.connect(self.returning)

    def del_rec(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            os.remove('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt')
            self.textans.clear()
        else:
            QMessageBox.warning(self, "No File", "File does not exist!", QMessageBox.Ok, QMessageBox.Ok)
    def show_his(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.historia = open("Determinant History.txt",'r')
            text = self.historia.read()
            self.textans.setText(text)
            self.historia.close()
        else:
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)
    def returning(self):
        self.close()

class Window4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("<h3> 4 X 4 Matrix <h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(500,50)
        self.label.move(200, 20)

        self.history = open("History4D.txt", 'w')
        self.history.write(" 4 x 4 History")
        self.history.close()

        self.setWindowTitle("Determinant Calculator")
        self.setGeometry(380, 100, 600, 500)

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(50, 80)
        self.textbox1.resize(100,30)
    
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(150, 80)
        self.textbox2.resize(100,30)
        

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(250, 80)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(350,80)
        self.textbox4.resize(100,30)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(50, 110)
        self.textbox5.resize(100,30)

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(150, 110)
        self.textbox6.resize(100,30)

        self.textbox7 = QLineEdit(self)
        self.textbox7.move(250, 110)
        self.textbox7.resize(100,30)

        self.textbox8 = QLineEdit(self)
        self.textbox8.move(350, 110)
        self.textbox8.resize(100,30)

        self.textbox9 = QLineEdit(self)
        self.textbox9.move(50, 140)
        self.textbox9.resize(100,30)

        self.textbox10 = QLineEdit(self)
        self.textbox10.move(150, 140)
        self.textbox10.resize(100,30)

        self.textbox11 = QLineEdit(self)
        self.textbox11.move(250, 140)
        self.textbox11.resize(100,30)

        self.textbox12 = QLineEdit(self)
        self.textbox12.move(350, 140)
        self.textbox12.resize(100,30)

        self.textbox13 = QLineEdit(self)
        self.textbox13.move(50, 170)
        self.textbox13.resize(100,30)

        self.textbox14 = QLineEdit(self)
        self.textbox14.move(150, 170)
        self.textbox14.resize(100,30)

        self.textbox15 = QLineEdit(self)
        self.textbox15.move(250, 170)
        self.textbox15.resize(100,30)

        self.textbox16 = QLineEdit(self)
        self.textbox16.move(350, 170)
        self.textbox16.resize(100,30)

        self.det = QLineEdit(self)
        self.det.setText("")
        self.det.move(450, 200)
        self.det.resize(100, 30)

        self.text = QLabel("<h3>Determinant:<h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(340, 204)
        self.text.resize(150, 30)
        
        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Submit input")
        self.button.move(50,350)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Clear all ")
        self.button.move(250,350)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(450,350)
        self.button.clicked.connect(self.back)
        
        self.button = QPushButton('History', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Show History")
        self.button.move(250,390)
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.button.clicked.connect(self.historyy)
        else:
            QMessageBox.warning(self, "Does not exist", "No existing history", QMessageBox.Ok, QMessageBox.Ok)

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(680,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()

    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
        self.textbox6.setText("")
        self.textbox7.setText("")
        self.textbox8.setText("")
        self.textbox9.setText("")
        self.textbox10.setText("")
        self.textbox11.setText("")
        self.textbox12.setText("")
        self.textbox13.setText("")
        self.textbox14.setText("")
        self.textbox15.setText("")
        self.textbox16.setText("")
        self.det.setText("")
        
    def data(self):
        if self.textbox1.text() != "" and self.textbox2.text() != "" and self.textbox3.text() != "" and self.textbox4.text() != "" and self.textbox5.text() != "" and self.textbox6.text() != "" and self.textbox7.text() != "" and self.textbox8.text() != "" and self.textbox9.text() != "" and self.textbox10.text() != "" and self.textbox11.text() != "" and self.textbox12.text() != "" and self.textbox13.text() != "" and self.textbox14.text() != "" and self.textbox15.text() != "" and self.textbox16.text() != "":
            a = int(self.textbox1.text())
            b = int(self.textbox2.text())
            c = int(self.textbox3.text())
            d = int(self.textbox4.text())
            e = int(self.textbox5.text())
            f = int(self.textbox6.text())
            g = int(self.textbox7.text())
            h = int(self.textbox8.text())
            i = int(self.textbox9.text())
            j = int(self.textbox10.text())
            k = int(self.textbox11.text())
            l = int(self.textbox12.text())
            m = int(self.textbox13.text())
            n = int(self.textbox14.text())
            o = int(self.textbox15.text())
            p = int(self.textbox16.text())
            paintEngine = int(self.textbox16.text())
            self.matrix_computation(a, b, c, d, e, f, g, h, i,j,k,l,m,n,o,p)
        elif self.textbox1.text() == "" and self.textbox2.text() == "" and self.textbox3.text() == "" and self.textbox4.text() == "" and self.textbox5.text() == "" and self.textbox6.text() == "" and self.textbox7.text() == "" and self.textbox8.text() == "" and self.textbox9.text() == "" and self.textbox10.text() == "" and self.textbox11.text() == "" and self.textbox12.text() == "" and self.textbox13.text() == "" and self.textbox14.text() == "" and self.textbox15.text() == "" and self.textbox16.text() == "":
            QMessageBox.warning(self, "Invalid", "Please input a number", QMessageBox.Ok, QMessageBox.Ok)
        elif self.textbox1.text() == "" or self.textbox2.text() == "" or self.textbox3.text() == "" or self.textbox4.text() == "" or self.textbox5.text() == "" or self.textbox6.text() == "" or self.textbox7.text() == "" or self.textbox8.text() == "" or self.textbox9.text() == "" or self.textbox10.text() == "" or self.textbox11.text() == "" or self.textbox12.text() == "" or self.textbox13.text() == "" or self.textbox14.text() == "" or self.textbox15.text() == "" or self.textbox16.text() == "":
            QMessageBox.warning(self, "Invalid", "Please input a number", QMessageBox.Ok, QMessageBox.Ok)
    
    def back(self):
        Window4.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = Window()
        self.mnwndw.show()
    
    def historyy(self):
        self.w = History_Win4()
        self.w.show()

    def matrix_computation(self, a, b, c, d, e, f, g, h, i,j,k,l,m,n,o,p):
        A = a*((f*(k*p-l*o)) - (g*(j*p-l*n)) + (h*(j*o-k*n)))
        B = b*((e*(k*p-l*o)) - (g*(i*p-l*m)) + (h*(i*o-k*m)))
        C = c*((e*(j*p-l*n)) - (f*(i*p-l*m)) + (h*(i*n-j*m)))
        D = d*((e*(j*o-k*n)) - (f*(i*o-k*m)) + (g*(i*n-j*m)))

        Determinate = A-B+C-D
        self.det.setText(f"{Determinate}")
        submitting = QMessageBox.information(self, "Response", "Your Response is being submitted. Do you want to proceed?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if submitting == QMessageBox.Yes and a != "" and b != "" and c != "" and d != "" and e != "" and f != "" and g != "" and h != "" and i != "" and j != "" and k != "" and l != "" and m != "" and n != "" and o != "" and p != "":
            self.historia = open("History4D.txt", 'a')
            self.historia.write("Inputs\n" + str(a)+"\n")
            self.historia.write(str(b)+"\n")
            self.historia.write(str(c)+"\n")
            self.historia.write(str(d)+"\n")
            self.historia.write(str(e)+"\n")
            self.historia.write(str(f)+"\n")
            self.historia.write(str(g)+"\n")
            self.historia.write(str(h)+"\n")
            self.historia.write(str(i)+"\n")
            self.historia.write(str(j)+"\n")
            self.historia.write(str(k)+"\n")
            self.historia.write(str(l)+"\n")
            self.historia.write(str(m)+"\n")
            self.historia.write(str(n)+"\n")
            self.historia.write(str(o)+"\n")
            self.historia.write(str(p)+"\n")
            self.historia.write("Determinate" + "is" + str(Determinate)+"\n")
            self.historia.close()

            QMessageBox.information(self, "Data processed", "Data has been processed, Thank You!", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and a == "" and b == "" and c == "" and d == "" and e == "" and f == "" and g == "" and h == "" and i == "" and j == "" and k == "" and l == "" and m == "" and n == "" and o == "" and p == "":
            pass
        elif submitting == QMessageBox.No and a != "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == "" or i == "" or j == "" or k == "" or l == "" or m == "" or n == "" or o == "" or p == "":
            QMessageBox.warning(self, "Blank field", "Do not leave any field unanswered!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Error input", "Number only please!", QMessageBox.Ok, QMessageBox.Ok)

class History_Win4(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Matrix Calculator"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.historia = open("History4D.txt", 'r')
            self.historia.read()
            self.historia.close()
        else:
            QMessageBox.warning(self, "Does not exist", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)

        self.setGeometry(self.top, self.left, self.width, self.height)

        self.setWindowIcon(QIcon('custom.ico'))
        self.textans = QTextEdit(self)
        self.textans.setText("")
        self.textans.resize(630, 450)

        self.pushButton = QPushButton("clear", self)
        self.pushButton.move(50, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Clear History")

        self.pushButton.clicked.connect(self.del_rec)

        self.pushButton = QPushButton("Show", self)
        self.pushButton.move(250, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Show History")

        self.pushButton.clicked.connect(self.show_his)

        self.pushButton = QPushButton("Exit", self)
        self.pushButton.move(450, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Close Window")

        self.pushButton.clicked.connect(self.returning)


    def del_rec(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            os.remove('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt')
            self.textans.clear()
        else:    
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)

        
    def show_his(self, matrix_computation):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.historia = open("History4D.txt",'r')
            text = self.historia.read()
            self.textans.setText(text)
            self.historia.close()
        else:
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)
    def returning(self):
        self.close()


class Window2(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("<h3>2 X 2 Matrix <h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(500,50)
        self.label.move(155, 25)

        self.history = open("History2d.txt", 'w')
        self.history.write("2x2 History\n")
        self.history.close()
       
        self.setWindowTitle("Determinant Calculator")
        self.setGeometry(500, 100, 500, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(150,80)
        self.textbox1.resize(100,30)
        
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(150, 110)
        self.textbox3.resize(100,30)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(250, 80)
        self.textbox2.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(250, 110)
        self.textbox4.resize(100,30)

        self.det = QLineEdit(self)
        self.det.setText("")
        self.det.move(350, 140)

        self.text = QLabel("<h3>Determinant:<h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(240, 145)
        self.text.resize(120, 30)
        
        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight : bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Submit input")
        self.button.move(50,350)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight : bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Clear all ")
        self.button.move(200,350)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight : bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(350,350)
        self.button.clicked.connect(self.back) 

        self.button = QPushButton('History', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight : bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Show History")
        self.button.move(200,390)
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.button.clicked.connect(self.historys)
        else:
            QMessageBox.warning(self, "Does not exist", "No existing history", QMessageBox.Ok, QMessageBox.Ok)

        
        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(680,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()
       

    @pyqtSlot()

    def Window_3(self):
        self.wndw3 = Window3()
        self.wndw3.show()
        Window2.close(self)

    def back(self):
        Window2.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = Window()
        self.mnwndw.show()
    def historys(self):
        self.open = His_Win2()
        self.open.show()

    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.det.setText("")
      

    def data(self):
        if self.textbox1.text() != "" and self.textbox2.text() != "" and self.textbox3.text() != "" and self.textbox4.text() != "":
            a = int(self.textbox1.text())
            b = int(self.textbox2.text())
            c = int(self.textbox3.text())
            d = int(self.textbox4.text())
            self.matrix_computation(a, b, c, d)
        elif self.textbox1.text() == "" and self.textbox2.text() == "" and self.textbox3.text() == "" and self.textbox4.text() == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blanks", QMessageBox.Ok, QMessageBox.Ok)
        elif self.textbox1.text() == "" or self.textbox2.text() == "" or self.textbox3.text() == "" or self.textbox4.text() == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blanks", QMessageBox.Ok, QMessageBox.Ok)
    

    def matrix_computation(self, a ,b ,c, d):

        Determinate = (a*d)-(b*c)
        self.det.setText(f"{Determinate}")
        submitting = QMessageBox.information(self, "Response", "Response being submitted. Do you wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if submitting == QMessageBox.Yes and a != "" and b != "" and c != "" and d != "":
            self.historia = open("History2d.txt", 'a')
            self.historia.write("Inputs\n" + str(a)+"\n")
            self.historia.write(str(b)+"\n")
            self.historia.write(str(c)+"\n")
            self.historia.write(str(d)+"\n")
            self.historia.write("Determinate is " + str(Determinate))
            self.historia.close()
class His_Win2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "2x2 History"
        self.setGeometry(500, 100, 500, 500)
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.historia = open("History2d.txt", 'r')
            self.historia.read()
            self.historia.close()
        else:
            QMessageBox.warning(self, "Does not exist", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)

        self.setWindowIcon(QIcon('custom.ico'))
        self.textans = QTextEdit(self)
        self.textans.setText("")
        self.textans.resize(450, 350)

        self.pushButton = QPushButton("Clear", self)
        self.pushButton.move(50, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Clear History")

        self.pushButton.clicked.connect(self.del_rec)

        self.pushButton = QPushButton("Show", self)
        self.pushButton.move(150, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Show History")

        self.pushButton.clicked.connect(self.show_his)

        self.pushButton = QPushButton("Exit", self)
        self.pushButton.move(350, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Close Window")

        self.pushButton.clicked.connect(self.returning)

    def del_rec(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            os.remove('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt')
            self.textans.clear()
        else:    
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)
    def show_his(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.historia = open("History2d.txt",'r')
            text = self.historia.read()
            self.textans.setText(text)
            self.historia.close()
        else:
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)
    def returning(self):
        self.close()

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Determinant Calculator"
        
        self.pushButton = QPushButton("2 X 2", self)
        self.pushButton.move(100, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt ; }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.window2) 

        self.pushButton = QPushButton("3 X 3", self)
        self.pushButton.move(300, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.window3)

        self.pushButton = QPushButton("4 X 4", self)
        self.pushButton.move(500, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.window4)             
        

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight : bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(300,450)
        self.button.clicked.connect(self.back)

        self.main_window()

    def main_window(self):
       
        self.label = QLabel("<h3>Matrix Calculator<h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: white;}')
        
        self.label.resize(500,50)
        self.label.move(210, 50) 
        self.setWindowTitle(self.title)
        self.setGeometry(350, 100, 700, 500)
     
        #background
        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(680,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        self.show()

    def back(self):
        Window.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = MainWindow()
        self.mnwndw.show()
    
    def window2(self):
        self.w = Window2()
        self.w.show()
        MainWindow.close(self)
    
    def window3(self):
        self.w = Window3()
        self.w.show()
        MainWindow.close(self)
    
    def window4(self):
        self.w = Window4()
        self.w.show()
        MainWindow.close(self)

class WindowAdd2x2(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("<h3> Addition <h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(500,50)
        self.label.move(430, 10)

        self.history = open("HistoryAdd2.txt", 'w')
        self.history.write("History\n")
        self.history.close()
       
        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(80, 80)
        self.textbox1.resize(100,30)
        

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(180, 80)
        self.textbox2.resize(100,30)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(80, 110)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(180, 110)
        self.textbox4.resize(100,30)

        self.textbox1a = QLineEdit(self)
        self.textbox1a.move(480, 80)
        self.textbox1a.resize(100,30)
        

        self.textbox2a = QLineEdit(self)
        self.textbox2a.move(580, 80)
        self.textbox2a.resize(100,30)

        self.textbox3a = QLineEdit(self)
        self.textbox3a.move(480, 110)
        self.textbox3a.resize(100,30)

        self.textbox4a = QLineEdit(self)
        self.textbox4a.move(580, 110)
        self.textbox4a.resize(100,30)

        self.det1 = QLineEdit(self)
        self.det1.setText("")
        self.det1.move(700, 200)
        self.det1.resize(100, 30)

        self.det2 = QLineEdit(self)
        self.det2.setText("")
        self.det2.move(800, 200)
        self.det2.resize(100, 30)

        self.det3 = QLineEdit(self)
        self.det3.setText("")
        self.det3.move(700, 230)
        self.det3.resize(100, 30)

        self.det4 = QLineEdit(self)
        self.det4.setText("")
        self.det4.move(800, 230)
        self.det4.resize(100, 30)

        self.text = QLabel("<h3>Answer: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(600, 234)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix A: <h3>", self)
        self.text.setFont(QFont('Times',10 , QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(80, 60)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix B: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(480, 60)
        self.text.resize(150, 30)
        
        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Submit input")
        self.button.move(50,350)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Clear all ")
        self.button.move(450,350)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(850,350)
        self.button.clicked.connect(self.back) 

        self.button = QPushButton('History', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Show History")
        self.button.move(450,390)
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.button.clicked.connect(self.historycc)
        else:
            QMessageBox.warning(self, "Does not exist", "No existing history", QMessageBox.Ok, QMessageBox.Ok)

        

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(800,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()
    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
       
        self.textbox1a.setText("")
        self.textbox2a.setText("")
        self.textbox3a.setText("")
        self.textbox4a.setText("")
        self.det1.setText("")
        self.det2.setText("")
        self.det3.setText("")
        self.det4.setText("")
        
    def data(self):
        if self.textbox1.text() != "" and self.textbox2.text() != "" and self.textbox3.text() != "" and self.textbox4.text() != "" and self.textbox1a.text() != "" and self.textbox2a.text() != "" and self.textbox3a.text() != "" and self.textbox4a.text() != "":
            a = int(self.textbox1.text())
            b = int(self.textbox2.text())
            c = int(self.textbox3.text())
            d = int(self.textbox4.text())
            e = int(self.textbox1a.text())
            f = int(self.textbox2a.text())
            g = int(self.textbox3a.text())
            h = int(self.textbox4a.text())
            self.matrix_computation(a, b, c, d, e, f, g, h)
        elif self.textbox1.text() == "" and self.textbox2.text() == "" and self.textbox3.text() == "" and self.textbox4.text() == "" and self.textbox1a.text() == "" and self.textbox2a.text() == "" and self.textbox3a.text() == "" and self.textbox4a.text() == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)
        elif self.textbox1.text() == "" or self.textbox2.text() == "" or self.textbox3.text() == "" or self.textbox4.text() == "" or self.textbox1a.text() == "" or self.textbox2a.text() == "" or self.textbox3a.text() == "" or self.textbox4a.text() == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)
    
    def back(self):
        WindowAdd2x2.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = WindowADD()
        self.mnwndw.show()

    def historycc(self):
        self.open = HisA2()
        self.open.show()

    def matrix_computation(self,a, b, c, d, e, f, g, h):
        A = (a+e)
        B = (b+f)
        C = (c+g)
        D = (d+h)
        

        Determinate1 = A
        Determinate2 = B
        Determinate3 = C
        Determinate4 = D
       
        

        self.det1.setText(f"{Determinate1}")
        self.det2.setText(f"{Determinate2}")
        self.det3.setText(f"{Determinate3}")
        self.det4.setText(f"{Determinate4}")
        submitting = QMessageBox.information(self, "Processing", "Response being submitted. Do you wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if submitting == QMessageBox.Yes and a != "" and b != "" and c != "" and d != "" and e != "" and f != "" and g != "" and h != "":
            self.historia = open("HistoryAdd2.txt", 'a')
            self.historia.write("Inputs\n" + str(a)+"\n")
            self.historia.write(str(b)+"\n")
            self.historia.write(str(c)+"\n")
            self.historia.write(str(d)+"\n")
            self.historia.write(str(e)+"\n")
            self.historia.write(str(f)+"\n")
            self.historia.write(str(g)+"\n")
            self.historia.write(str(h)+"\n")
            self.historia.write("(1,1) is " + str(Determinate1)+"\n")
            self.historia.write("(1,2) is " + str(Determinate2) + "\n")
            self.historia.write("(2,1) is " + str(Determinate3)+"\n")
            self.historia.write("(2,2) is " + str(Determinate4)+"\n")
            self.historia.close()
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and a == "" and b == "" and c == "" and d == "" and e == "" and f == "" and g == "" and h == "":
            pass
        elif submitting == QMessageBox.No and a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)

class HisA2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "2x2 Addition History"
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.history = open("HistoryAdd2.txt", 'r')
            self.history.read()
            self.history.close()
        else:
            QMessageBox.warning(self, "Error", "History does not exists!", QMessageBox.Ok, QMessageBox.Ok)

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
        self.setWindowIcon(QIcon('custom.ico'))
        self.textans = QTextEdit(self)
        self.textans.setText("")
        self.textans.resize(800, 450)

        self.pushButton = QPushButton("Clear", self)
        self.pushButton.move(150, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Clear History")

        self.pushButton.clicked.connect(self.del_rec)

        self.pushButton = QPushButton("Show", self)
        self.pushButton.move(350, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Show History")

        self.pushButton.clicked.connect(self.show_his)

        self.pushButton = QPushButton("Exit", self)
        self.pushButton.move(550, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Close Window")

        self.pushButton.clicked.connect(self.returning)

    def del_rec(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            os.remove('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt')
            self.textans.clear()
        else:    
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)

    def show_his(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.hopn = open("HistoryAdd2.txt",'r')
            text = self.hopn.read()
            self.textans.setText(text)
            self.hopn.close()
        else:
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)
    def returning(self):
        self.close()

class WindowAdd3x3(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("<h3> Addition <h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(500,50)
        self.label.move(430, 10)

        self.history = open("HistoryAdd3.txt", 'w')
        self.history.write("History\n")
        self.history.close()

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1050, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(80, 80)
        self.textbox1.resize(100,30)
        

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(180, 80)
        self.textbox2.resize(100,30)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(280,80)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(80, 110)
        self.textbox4.resize(100,30)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(180, 110)
        self.textbox5.resize(100,30)

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(280, 110)
        self.textbox6.resize(100,30)

        self.textbox7 = QLineEdit(self)
        self.textbox7.move(80, 140)
        self.textbox7.resize(100,30)

        self.textbox8 = QLineEdit(self)
        self.textbox8.move(180, 140)
        self.textbox8.resize(100,30)

        self.textbox9 = QLineEdit(self)
        self.textbox9.move(280, 140)
        self.textbox9.resize(100,30)

        self.textbox1a = QLineEdit(self)
        self.textbox1a.move(480, 80)
        self.textbox1a.resize(100,30)
        

        self.textbox2a = QLineEdit(self)
        self.textbox2a.move(580, 80)
        self.textbox2a.resize(100,30)

        self.textbox3a = QLineEdit(self)
        self.textbox3a.move(680,80)
        self.textbox3a.resize(100,30)

        self.textbox4a = QLineEdit(self)
        self.textbox4a.move(480, 110)
        self.textbox4a.resize(100,30)

        self.textbox5a = QLineEdit(self)
        self.textbox5a.move(580, 110)
        self.textbox5a.resize(100,30)

        self.textbox6a = QLineEdit(self)
        self.textbox6a.move(680, 110)
        self.textbox6a.resize(100,30)

        self.textbox7a = QLineEdit(self)
        self.textbox7a.move(480, 140)
        self.textbox7a.resize(100,30)

        self.textbox8a = QLineEdit(self)
        self.textbox8a.move(580, 140)
        self.textbox8a.resize(100,30)

        self.textbox9a = QLineEdit(self)
        self.textbox9a.move(680, 140)
        self.textbox9a.resize(100,30)

        self.det1 = QLineEdit(self)
        self.det1.setText("")
        self.det1.move(700, 200)
        self.det1.resize(100, 30)

        self.det2 = QLineEdit(self)
        self.det2.setText("")
        self.det2.move(800, 200)
        self.det2.resize(100, 30)

        self.det3 = QLineEdit(self)
        self.det3.setText("")
        self.det3.move(900, 200)
        self.det3.resize(100, 30)

        self.det4 = QLineEdit(self)
        self.det4.setText("")
        self.det4.move(700, 230)
        self.det4.resize(100, 30)

        self.det5 = QLineEdit(self)
        self.det5.setText("")
        self.det5.move(800, 230)
        self.det5.resize(100, 30)

        self.det6 = QLineEdit(self)
        self.det6.setText("")
        self.det6.move(900, 230)
        self.det6.resize(100, 30)

        self.det7 = QLineEdit(self)
        self.det7.setText("")
        self.det7.move(700, 260)
        self.det7.resize(100, 30)

        self.det8 = QLineEdit(self)
        self.det8.setText("")
        self.det8.move(800, 260)
        self.det8.resize(100, 30)

        self.det9 = QLineEdit(self)
        self.det9.setText("")
        self.det9.move(900, 260)
        self.det9.resize(100, 30)

        self.text = QLabel("<h3>Answer: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(600, 234)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix A: <h3>", self)
        self.text.setFont(QFont('Times',10 , QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(80, 60)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix B: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(480, 60)
        self.text.resize(150, 30)

        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Submit input")
        self.button.move(50,350)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Clear all ")
        self.button.move(450,350)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(850,350)
        self.button.clicked.connect(self.back) 

        self.button = QPushButton('History', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Show History")
        self.button.move(450,390)
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.button.clicked.connect(self.historycc)
        else:
            QMessageBox.warning(self, "Does not exist", "No existing history", QMessageBox.Ok, QMessageBox.Ok)

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(800,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()
    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
        self.textbox6.setText("")
        self.textbox7.setText("")
        self.textbox8.setText("")
        self.textbox9.setText("")
        self.textbox1a.setText("")
        self.textbox2a.setText("")
        self.textbox3a.setText("")
        self.textbox4a.setText("")
        self.textbox5a.setText("")
        self.textbox6a.setText("")
        self.textbox7a.setText("")
        self.textbox8a.setText("")
        self.textbox9a.setText("")

        self.det1.setText("")
        self.det2.setText("")
        self.det3.setText("")
        self.det4.setText("")
        self.det5.setText("")
        self.det6.setText("")
        self.det7.setText("")
        self.det8.setText("")
        self.det9.setText("")

        

    def data(self):
        if self.textbox1.text() != "" and self.textbox2.text() != "" and self.textbox3.text() != "" and self.textbox4.text() != "" and self.textbox5.text() != "" and self.textbox6.text() != "" and self.textbox7.text() != "" and self.textbox8.text() != ""and self.textbox9.text() != ""and self.textbox1a.text() != ""and self.textbox2a.text() != ""and self.textbox3a.text() != ""and self.textbox4a.text() != ""and self.textbox5a.text() != ""and self.textbox6a.text() != ""and self.textbox7a.text() != ""and self.textbox8a.text() != ""and self.textbox9a.text() != "":
            a = int(self.textbox1.text())
            b = int(self.textbox2.text())
            c = int(self.textbox3.text())
            d = int(self.textbox4.text())
            e = int(self.textbox5.text())
            f = int(self.textbox6.text())
            g = int(self.textbox7.text())
            h = int(self.textbox8.text())
            i = int(self.textbox9.text())
            j = int(self.textbox1a.text())
            k = int(self.textbox2a.text())
            l = int(self.textbox3a.text())
            m = int(self.textbox4a.text())
            n = int(self.textbox5a.text())
            o = int(self.textbox6a.text())
            p = int(self.textbox7a.text())
            q = int(self.textbox8a.text())
            r = int(self.textbox9a.text())
            self.matrix_computation(a, b, c, d, e, f, g, h, i, j,k,l,m,n,o,p,q,r,)
       

    def back(self):
        WindowAdd3x3.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = WindowADD()
        self.mnwndw.show()

    def historycc(self):
        self.open = HisA3()
        self.open.show()

    def matrix_computation(self,a, b, c, d, e, f, g, h, i, j,k,l,m,n,o,p,q,r,):
        A = (a+j)
       
        B = (b+k)
        C = (c+l)
        D = (d+m)
        E = (e+n)
        F = (f+o)
        G = (g+p)
        H = (h+q)
        I = (i+r)

        Determinate1 = A
        Determinate2 = B
        Determinate3 = C
        Determinate4 = D
        Determinate5 = E
        Determinate6 = F
        Determinate7 = G
        Determinate8 = H
        Determinate9 = I
        

        self.det1.setText(f"{Determinate1}")
        self.det2.setText(f"{Determinate2}")
        self.det3.setText(f"{Determinate3}")
        self.det4.setText(f"{Determinate4}")
        self.det5.setText(f"{Determinate5}")
        self.det6.setText(f"{Determinate6}")
        self.det7.setText(f"{Determinate7}")
        self.det8.setText(f"{Determinate8}")
        self.det9.setText(f"{Determinate9}")
        submitting = QMessageBox.information(self, "Processing", "Response being submitted. Do you wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if submitting == QMessageBox.Yes and a != "" and b != "" and c != "" and d != "" and e != "" and f != "" and g != "" and h != ""and i != ""and j != ""and k != ""and l != ""and m != ""and n != ""and o != ""and p != ""and q != ""and r != "":

            self.historia = open("HistoryAdd3.txt", 'a')
            self.historia.write("Inputs\n" + str(a)+"\n")
            self.historia.write(str(b)+"\n")
            self.historia.write(str(c)+"\n")
            self.historia.write(str(d)+"\n")
            self.historia.write(str(e)+"\n")
            self.historia.write(str(f)+"\n")
            self.historia.write(str(g)+"\n")
            self.historia.write(str(h)+"\n")
            self.historia.write(str(i)+"\n")
            self.historia.write(str(j)+"\n")
            self.historia.write(str(k)+"\n")
            self.historia.write(str(l)+"\n")
            self.historia.write(str(m)+"\n")
            self.historia.write(str(n)+"\n")
            self.historia.write(str(o)+"\n")
            self.historia.write(str(p)+"\n")
            self.historia.write(str(q)+"\n")
            self.historia.write(str(r)+"\n")
            self.historia.write("(1,1) is " + str(Determinate1)+"\n")
            self.historia.write("(1,2) is " + str(Determinate2) + "\n")
            self.historia.write("(1,3) is " + str(Determinate3)+"\n")
            self.historia.write("(2,1) is " + str(Determinate4)+"\n")
            self.historia.write("(2,2) is " + str(Determinate5)+"\n")
            self.historia.write("(2,3) is " + str(Determinate6)+"\n")
            self.historia.write("(3,1) is " + str(Determinate7)+"\n")
            self.historia.write("(3,2) is " + str(Determinate8)+"\n")
            self.historia.write("(3,3) is " + str(Determinate9)+"\n")
            
            self.historia.close()
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and a == "" and b == "" and c == "" and d == "" and e == "" and f == "" and g == "" and h == ""and i == ""and j == ""and k ==""and l == ""and m == ""and n == ""and o == ""and p == ""and q == ""and r == "":
            pass
        elif submitting == QMessageBox.No and a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == ""or i == ""or j == ""or k == ""or l == ""or m == ""or n == ""or o == ""or p == ""or q == ""or r == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)

class HisA3(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "3x3 Addition History"
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.history = open("HistoryAdd3.txt", 'r')
            self.history.read()
            self.history.close()
        else:
            QMessageBox.warning(self, "Error", "History does not exists!", QMessageBox.Ok, QMessageBox.Ok)

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
        self.setWindowIcon(QIcon('custom.ico'))
        self.textans = QTextEdit(self)
        self.textans.setText("")
        self.textans.resize(800, 450)

        self.pushButton = QPushButton("Clear", self)
        self.pushButton.move(150, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Clear History")

        self.pushButton.clicked.connect(self.del_rec)

        self.pushButton = QPushButton("Show", self)
        self.pushButton.move(350, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Show History")

        self.pushButton.clicked.connect(self.show_his)

        self.pushButton = QPushButton("Exit", self)
        self.pushButton.move(550, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Close Window")

        self.pushButton.clicked.connect(self.returning)

    def del_rec(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            os.remove('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt')
            self.textans.clear()
        else:    
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)

    def show_his(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.hopn = open("HistoryAdd3.txt",'r')
            text = self.hopn.read()
            self.textans.setText(text)
            self.hopn.close()
        else:
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)
    def returning(self):
        self.close()

class WindowAdd4x4(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("<h3> Addition <h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(500,50)
        self.label.move(430, 10)

        self.history = open("HistoryAdd4.txt", 'w')
        self.history.write("History\n")
        self.history.close()

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(50, 80)
        self.textbox1.resize(100,30)
    
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(150, 80)
        self.textbox2.resize(100,30)
        

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(250, 80)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(350,80)
        self.textbox4.resize(100,30)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(50, 110)
        self.textbox5.resize(100,30)

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(150, 110)
        self.textbox6.resize(100,30)

        self.textbox7 = QLineEdit(self)
        self.textbox7.move(250, 110)
        self.textbox7.resize(100,30)

        self.textbox8 = QLineEdit(self)
        self.textbox8.move(350, 110)
        self.textbox8.resize(100,30)

        self.textbox9 = QLineEdit(self)
        self.textbox9.move(50, 140)
        self.textbox9.resize(100,30)

        self.textbox10 = QLineEdit(self)
        self.textbox10.move(150, 140)
        self.textbox10.resize(100,30)

        self.textbox11 = QLineEdit(self)
        self.textbox11.move(250, 140)
        self.textbox11.resize(100,30)

        self.textbox12 = QLineEdit(self)
        self.textbox12.move(350, 140)
        self.textbox12.resize(100,30)

        self.textbox13 = QLineEdit(self)
        self.textbox13.move(50, 170)
        self.textbox13.resize(100,30)

        self.textbox14 = QLineEdit(self)
        self.textbox14.move(150, 170)
        self.textbox14.resize(100,30)

        self.textbox15 = QLineEdit(self)
        self.textbox15.move(250, 170)
        self.textbox15.resize(100,30)

        self.textbox16 = QLineEdit(self)
        self.textbox16.move(350, 170)
        self.textbox16.resize(100,30)

        self.textbox1a = QLineEdit(self)
        self.textbox1a.move(580, 80)
        self.textbox1a.resize(100,30)
    
        self.textbox2a = QLineEdit(self)
        self.textbox2a.move(680, 80)
        self.textbox2a.resize(100,30)
        

        self.textbox3a = QLineEdit(self)
        self.textbox3a.move(780, 80)
        self.textbox3a.resize(100,30)

        self.textbox4a = QLineEdit(self)
        self.textbox4a.move(880,80)
        self.textbox4a.resize(100,30)

        self.textbox5a = QLineEdit(self)
        self.textbox5a.move(580, 110)
        self.textbox5a.resize(100,30)

        self.textbox6a = QLineEdit(self)
        self.textbox6a.move(680, 110)
        self.textbox6a.resize(100,30)

        self.textbox7a = QLineEdit(self)
        self.textbox7a.move(780, 110)
        self.textbox7a.resize(100,30)

        self.textbox8a = QLineEdit(self)
        self.textbox8a.move(880, 110)
        self.textbox8a.resize(100,30)

        self.textbox9a = QLineEdit(self)
        self.textbox9a.move(580, 140)
        self.textbox9a.resize(100,30)

        self.textbox10a = QLineEdit(self)
        self.textbox10a.move(680, 140)
        self.textbox10a.resize(100,30)

        self.textbox11a = QLineEdit(self)
        self.textbox11a.move(780, 140)
        self.textbox11a.resize(100,30)

        self.textbox12a = QLineEdit(self)
        self.textbox12a.move(880, 140)
        self.textbox12a.resize(100,30)

        self.textbox13a = QLineEdit(self)
        self.textbox13a.move(580, 170)
        self.textbox13a.resize(100,30)

        self.textbox14a = QLineEdit(self)
        self.textbox14a.move(680, 170)
        self.textbox14a.resize(100,30)

        self.textbox15a = QLineEdit(self)
        self.textbox15a.move(780, 170)
        self.textbox15a.resize(100,30)

        self.textbox16a = QLineEdit(self)
        self.textbox16a.move(880, 170)
        self.textbox16a.resize(100,30)

        self.det1 = QLineEdit(self)
        self.det1.setText("")
        self.det1.move(580, 300)
        self.det1.resize(100, 30)

        self.det2 = QLineEdit(self)
        self.det2.setText("")
        self.det2.move(680, 300)
        self.det2.resize(100, 30)

        self.det3 = QLineEdit(self)
        self.det3.setText("")
        self.det3.move(780, 300)
        self.det3.resize(100, 30)

        self.det4 = QLineEdit(self)
        self.det4.setText("")
        self.det4.move(880, 300)
        self.det4.resize(100, 30)

        self.det5 = QLineEdit(self)
        self.det5.setText("")
        self.det5.move(580, 330)
        self.det5.resize(100, 30)

        self.det6 = QLineEdit(self)
        self.det6.setText("")
        self.det6.move(680, 330)
        self.det6.resize(100, 30)

        self.det7 = QLineEdit(self)
        self.det7.setText("")
        self.det7.move(780, 330)
        self.det7.resize(100, 30)

        self.det8 = QLineEdit(self)
        self.det8.setText("")
        self.det8.move(880, 330)
        self.det8.resize(100, 30)

        self.det9 = QLineEdit(self)
        self.det9.setText("")
        self.det9.move(580, 360)
        self.det9.resize(100, 30)

        self.det10 = QLineEdit(self)
        self.det10.setText("")
        self.det10.move(680, 360)
        self.det10.resize(100, 30)

        self.det11 = QLineEdit(self)
        self.det11.setText("")
        self.det11.move(780, 360)
        self.det11.resize(100, 30)

        self.det12 = QLineEdit(self)
        self.det12.setText("")
        self.det12.move(880, 360)
        self.det12.resize(100, 30)

        self.det13 = QLineEdit(self)
        self.det13.setText("")
        self.det13.move(580, 390)
        self.det13.resize(100, 30)

        self.det14 = QLineEdit(self)
        self.det14.setText("")
        self.det14.move(680, 390)
        self.det14.resize(100, 30)

        self.det15 = QLineEdit(self)
        self.det15.setText("")
        self.det15.move(780, 390)
        self.det15.resize(100, 30)

        self.det16 = QLineEdit(self)
        self.det16.setText("")
        self.det16.move(880, 390)
        self.det16.resize(100, 30)

        self.text = QLabel("<h3>Answer: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(580, 275)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix A: <h3>", self)
        self.text.setFont(QFont('Times',10 , QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(50, 55)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix B: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(580, 55)
        self.text.resize(150, 30)

        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Submit input")
        self.button.move(50,360)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Clear all ")
        self.button.move(200,360)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(350,360)
        self.button.clicked.connect(self.back) 

        self.button = QPushButton('History', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Show History")
        self.button.move(200,390)
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.button.clicked.connect(self.historycc)
        else:
            QMessageBox.warning(self, "Does not exist", "No existing history", QMessageBox.Ok, QMessageBox.Ok)

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(800,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()
    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
        self.textbox6.setText("")
        self.textbox7.setText("")
        self.textbox8.setText("")
        self.textbox9.setText("")
        self.textbox10.setText("")
        self.textbox11.setText("")
        self.textbox12.setText("")
        self.textbox13.setText("")
        self.textbox14.setText("")
        self.textbox15.setText("")
        self.textbox16.setText("")
    
        self.textbox1a.setText("")
        self.textbox2a.setText("")
        self.textbox3a.setText("")
        self.textbox4a.setText("")
        self.textbox5a.setText("")
        self.textbox6a.setText("")
        self.textbox7a.setText("")
        self.textbox8a.setText("")
        self.textbox9a.setText("")
        self.textbox10a.setText("")
        self.textbox11a.setText("")
        self.textbox12a.setText("")
        self.textbox13a.setText("")
        self.textbox14a.setText("")
        self.textbox15a.setText("")
        self.textbox16a.setText("")

        self.det1.setText("")
        self.det2.setText("")
        self.det3.setText("")
        self.det4.setText("")
        self.det5.setText("")
        self.det6.setText("")
        self.det7.setText("")
        self.det8.setText("")
        self.det9.setText("")
        self.det10.setText("")
        self.det11.setText("")
        self.det12.setText("")
        self.det13.setText("")
        self.det14.setText("")
        self.det15.setText("")
        self.det16.setText("")


        

    def data(self):
        if self.textbox1.text() != "" and self.textbox2.text() !=  "" and self.textbox3.text() != "" and self.textbox4.text() != "" and self.textbox5.text() != "" and self.textbox6.text() != ""and self.textbox7.text() != "" and self.textbox8.text() != ""and  self.textbox9.text() != "" and self.textbox10.text() != "" and self.textbox11.text() != "" and self.textbox12.text() != "" and self.textbox13.text() != "" and self.textbox14.text() != "" and self.textbox15.text() != "" and self.textbox16.text() != "":
            a = int(self.textbox1.text())
            b = int(self.textbox2.text())
            c = int(self.textbox3.text())
            d = int(self.textbox4.text())
            e = int(self.textbox5.text())
            f = int(self.textbox6.text())
            g = int(self.textbox7.text())
            h = int(self.textbox8.text())
            i = int(self.textbox9.text())
            j = int(self.textbox10.text())
            k = int(self.textbox11.text())
            l = int(self.textbox12.text())
            m = int(self.textbox13.text())
            n = int(self.textbox14.text())
            o = int(self.textbox15.text())
            p = int(self.textbox16.text())
            

            aa = int(self.textbox1a.text())
            bb = int(self.textbox2a.text())
            cc = int(self.textbox3a.text())
            dd = int(self.textbox4a.text())
            ee = int(self.textbox5a.text())
            ff = int(self.textbox6a.text())
            gg = int(self.textbox7a.text())
            hh = int(self.textbox8a.text())
            ii = int(self.textbox9a.text())
            jj = int(self.textbox10a.text())
            kk = int(self.textbox11a.text())
            ll = int(self.textbox12a.text())
            mm = int(self.textbox13a.text())
            nn = int(self.textbox14a.text())
            oo = int(self.textbox15a.text())
            pp = int(self.textbox16a.text())
            self.matrix_computation(a, b, c, d, e, f, g, h, i, j,k,l,m,n,o,p,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp)
        

    def back(self):
        WindowAdd4x4.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = WindowADD()
        self.mnwndw.show()

    def historycc(self):
        self.open = HisA4()
        self.open.show()

    def matrix_computation(self,a, b, c, d, e, f, g, h, i, j,k,l,m,n,o,p,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp):
        A = (a+aa)
        B = (b+bb)
        C = (c+cc)
        D = (d+dd)
        E = (e+ee)
        F = (f+ff)
        G = (g+gg)
        H = (h+hh)
        I = (i+ii)
        J = (j+jj)
        K = (k+kk)
        L = (l+ll)
        M = (m+mm)
        N = (n+nn)
        O = (o+oo)
        P = (p+pp)

        Determinate1 = A
        Determinate2 = B
        Determinate3 = C
        Determinate4 = D
        Determinate5 = E
        Determinate6 = F
        Determinate7 = G
        Determinate8 = H
        Determinate9 = I
        Determinate10 = J
        Determinate11 = K
        Determinate12 = L
        Determinate13 = M
        Determinate14 = N
        Determinate15 = O
        Determinate16 = P
        

        self.det1.setText(f"{Determinate1}")
        self.det2.setText(f"{Determinate2}")
        self.det3.setText(f"{Determinate3}")
        self.det4.setText(f"{Determinate4}")
        self.det5.setText(f"{Determinate5}")
        self.det6.setText(f"{Determinate6}")
        self.det7.setText(f"{Determinate7}")
        self.det8.setText(f"{Determinate8}")
        self.det9.setText(f"{Determinate9}")
        self.det10.setText(f"{Determinate10}")
        self.det11.setText(f"{Determinate11}")
        self.det12.setText(f"{Determinate12}")
        self.det13.setText(f"{Determinate13}")
        self.det14.setText(f"{Determinate14}")
        self.det15.setText(f"{Determinate15}")
        self.det16.setText(f"{Determinate16}")
        self.historia = open("HistoryAdd4.txt", 'a')
        self.historia.write("Inputs\n" + str(a)+"\n")
        self.historia.write(str(b)+"\n")
        self.historia.write(str(c)+"\n")
        self.historia.write(str(d)+"\n")
        self.historia.write(str(e)+"\n")
        self.historia.write(str(f)+"\n")
        self.historia.write(str(g)+"\n")
        self.historia.write(str(h)+"\n")
        self.historia.write(str(i)+"\n")
        self.historia.write(str(j)+"\n")
        self.historia.write(str(k)+"\n")
        self.historia.write(str(l)+"\n")
        self.historia.write(str(m)+"\n")
        self.historia.write(str(n)+"\n")
        self.historia.write(str(o)+"\n")
        self.historia.write(str(p)+"\n")
            
        self.historia.write(str(aa)+"\n")
        self.historia.write(str(bb)+"\n")
        self.historia.write(str(cc)+"\n")
        self.historia.write(str(dd)+"\n")
        self.historia.write(str(ee)+"\n")
        self.historia.write(str(ff)+"\n")
        self.historia.write(str(gg)+"\n")
        self.historia.write(str(hh)+"\n")
        self.historia.write(str(ii)+"\n")
        self.historia.write(str(jj)+"\n")
        self.historia.write(str(kk)+"\n")
        self.historia.write(str(ll)+"\n")
        self.historia.write(str(mm)+"\n")
        self.historia.write(str(nn)+"\n")
        self.historia.write(str(oo)+"\n")
        self.historia.write(str(pp)+"\n")
        self.historia.write("(1,1) is " + str(Determinate1)+"\n")
        self.historia.write("(1,2) is " + str(Determinate2) + "\n")
        self.historia.write("(1,3) is " + str(Determinate3)+"\n")
        self.historia.write("(1,4) is " + str(Determinate4)+"\n")
        self.historia.write("(2,1) is " + str(Determinate5)+"\n")
        self.historia.write("(2,2) is " + str(Determinate6)+"\n")
        self.historia.write("(2,3) is " + str(Determinate7)+"\n")
        self.historia.write("(2,4) is " + str(Determinate8)+"\n")
        self.historia.write("(3,1) is " + str(Determinate9)+"\n")
        self.historia.write("(3,2) is " + str(Determinate10)+"\n")
        self.historia.write("(3,3) is " + str(Determinate11) + "\n")
        self.historia.write("(3,4) is " + str(Determinate12)+"\n")
        self.historia.write("(4,1) is " + str(Determinate13)+"\n")
        self.historia.write("(4,2) is " + str(Determinate14)+"\n")
        self.historia.write("(4,3) is " + str(Determinate15)+"\n")
        self.historia.write("(4,4) is " + str(Determinate16)+"\n")
        self.historia.close()     
   
class HisA4(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "4x4 Addition History"
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.history = open("HistoryAdd4.txt", 'r')
            self.history.read()
            self.history.close()
        else:
            QMessageBox.warning(self, "Error", "History does not exists!", QMessageBox.Ok, QMessageBox.Ok)

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
        self.setWindowIcon(QIcon('custom.ico'))
        self.textans = QTextEdit(self)
        self.textans.setText("")
        self.textans.resize(800, 450)

        self.pushButton = QPushButton("Clear", self)
        self.pushButton.move(150, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Clear History")

        self.pushButton.clicked.connect(self.del_rec)

        self.pushButton = QPushButton("Show", self)
        self.pushButton.move(350, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Show History")

        self.pushButton.clicked.connect(self.show_his)

        self.pushButton = QPushButton("Exit", self)
        self.pushButton.move(550, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Close Window")

        self.pushButton.clicked.connect(self.returning)

    def del_rec(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            os.remove('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt')
            self.textans.clear()
        else:    
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)

    def show_his(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.hopn = open("HistoryAdd4.txt",'r')
            text = self.hopn.read()
            self.textans.setText(text)
            self.hopn.close()
        else:
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)
    def returning(self):
        self.close()


class WindowADD(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Determinant Calculator"
        
        self.pushButton = QPushButton("2 X 2", self)
        self.pushButton.move(100, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt ; }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.window2add) 

        self.pushButton = QPushButton("3 X 3", self)
        self.pushButton.move(300, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.window3add)

        self.pushButton = QPushButton("4 X 4", self)
        self.pushButton.move(500, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.window4add)             
        

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight : bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(300,450)
        self.button.clicked.connect(self.back)

        self.main_window()

    def main_window(self):
       
        self.label = QLabel("<h3>Matrix Calculator<h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: white;}')
        
        self.label.resize(500,50)
        self.label.move(210, 50) 
        self.setWindowTitle(self.title)
        self.setGeometry(350, 100, 700, 500)
     
        #background
        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(800,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        self.show()

    def back(self):
        WindowADD.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = MainWindow()
        self.mnwndw.show()
    


    def window2add(self):
        self.w = WindowAdd2x2()
        self.w.show()
        MainWindow.close(self)
    
    def window3add(self):
        self.w = WindowAdd3x3()
        self.w.show()
        MainWindow.close(self)

    def window4add(self):
        self.w = WindowAdd4x4()
        self.w.show()
        MainWindow.close(self)

class WindowSub2x2(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("<h3> Subtraction <h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(500,50)
        self.label.move(430, 10)
       
        self.history = open("HistorySub2.txt", 'w')
        self.history.write("History\n")
        self.history.close()

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(80, 80)
        self.textbox1.resize(100,30)
        

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(180, 80)
        self.textbox2.resize(100,30)

        

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(80, 110)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(180, 110)
        self.textbox4.resize(100,30)

       

       
        self.textbox1a = QLineEdit(self)
        self.textbox1a.move(480, 80)
        self.textbox1a.resize(100,30)
        

        self.textbox2a = QLineEdit(self)
        self.textbox2a.move(580, 80)
        self.textbox2a.resize(100,30)

        self.textbox3a = QLineEdit(self)
        self.textbox3a.move(480, 110)
        self.textbox3a.resize(100,30)

        self.textbox4a = QLineEdit(self)
        self.textbox4a.move(580, 110)
        self.textbox4a.resize(100,30)

        self.det1 = QLineEdit(self)
        self.det1.setText("")
        self.det1.move(700, 200)
        self.det1.resize(100, 30)

        self.det2 = QLineEdit(self)
        self.det2.setText("")
        self.det2.move(800, 200)
        self.det2.resize(100, 30)

        self.det3 = QLineEdit(self)
        self.det3.setText("")
        self.det3.move(700, 230)
        self.det3.resize(100, 30)

        self.det4 = QLineEdit(self)
        self.det4.setText("")
        self.det4.move(800, 230)
        self.det4.resize(100, 30)

        self.text = QLabel("<h3>Answer: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(600, 234)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix A: <h3>", self)
        self.text.setFont(QFont('Times',10 , QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(80, 60)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix B: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(480, 60)
        self.text.resize(150, 30)

        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Submit input")
        self.button.move(50,350)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Clear all ")
        self.button.move(450,350)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(850,350)
        self.button.clicked.connect(self.back) 

        self.button = QPushButton('History', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Show History")
        self.button.move(450,390)
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.button.clicked.connect(self.historycc)
        else:
            QMessageBox.warning(self, "Does not exist", "No existing history", QMessageBox.Ok, QMessageBox.Ok)

        

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(800,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()
    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
       
        self.textbox1a.setText("")
        self.textbox2a.setText("")
        self.textbox3a.setText("")
        self.textbox4a.setText("")
        self.det1.setText("")
        self.det2.setText("")
        self.det3.setText("")
        self.det4.setText("")
        

        

    def data(self):
        if self.textbox1.text() != "" and self.textbox2.text() != "" and self.textbox3.text() != "" and self.textbox4.text() != "" and self.textbox1a.text() != "" and self.textbox2a.text() != "" and self.textbox3a.text() != "" and self.textbox4a.text() != "":
            a = int(self.textbox1.text())
            b = int(self.textbox2.text())
            c = int(self.textbox3.text())
            d = int(self.textbox4.text())
            e = int(self.textbox1a.text())
            f = int(self.textbox2a.text())
            g = int(self.textbox3a.text())
            h = int(self.textbox4a.text())
            self.matrix_computation(a, b, c, d, e, f, g, h)
        elif self.textbox1.text() == "" and self.textbox2.text() == "" and self.textbox3.text() == "" and self.textbox4.text() == "" and self.textbox1a.text() == "" and self.textbox2a.text() == "" and self.textbox3a.text() == "" and self.textbox4a.text() == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)
        elif self.textbox1.text() == "" or self.textbox2.text() == "" or self.textbox3.text() == "" or self.textbox4.text() == "" or self.textbox1a.text() == "" or self.textbox2a.text() == "" or self.textbox3a.text() == "" or self.textbox4a.text() == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)
    
    def back(self):
        WindowSub2x2.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = WindowSUB()
        self.mnwndw.show()
    
    def historycc(self):
        self.open = HisS2()
        self.open.show()

    def matrix_computation(self,a, b, c, d, e, f, g, h):
        A = (a-e)
        B = (b-f)
        C = (c-g)
        D = (d-h)
        

        Determinate1 = A
        Determinate2 = B
        Determinate3 = C
        Determinate4 = D
       
        

        self.det1.setText(f"{Determinate1}")
        self.det2.setText(f"{Determinate2}")
        self.det3.setText(f"{Determinate3}")
        self.det4.setText(f"{Determinate4}")
        submitting = QMessageBox.information(self, "Processing", "Response being submitted. Do you wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if submitting == QMessageBox.Yes and a != "" and b != "" and c != "" and d != "" and e != "" and f != "" and g != "" and h != "":
            self.historia = open("HistorySub2.txt", 'a')
            self.historia.write("Inputs\n" + str(a)+"\n")
            self.historia.write(str(b)+"\n")
            self.historia.write(str(c)+"\n")
            self.historia.write(str(d)+"\n")
            self.historia.write(str(e)+"\n")
            self.historia.write(str(f)+"\n")
            self.historia.write(str(g)+"\n")
            self.historia.write(str(h)+"\n")
            self.historia.write("(1,1) is " + str(Determinate1)+"\n")
            self.historia.write("(1,2) is " + str(Determinate2) + "\n")
            self.historia.write("(2,1) is " + str(Determinate3)+"\n")
            self.historia.write("(2,2) is " + str(Determinate4)+"\n")
            self.historia.close()
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and a == "" and b == "" and c == "" and d == "" and e == "" and f == "" and g == "" and h == "":
            pass
        elif submitting == QMessageBox.No and a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)

class HisS2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "2x2 Substraction History"
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.history = open("HistorySub2.txt", 'r')
            self.history.read()
            self.history.close()
        else:
            QMessageBox.warning(self, "Error", "History does not exists!", QMessageBox.Ok, QMessageBox.Ok)

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
        self.setWindowIcon(QIcon('custom.ico'))
        self.textans = QTextEdit(self)
        self.textans.setText("")
        self.textans.resize(800, 450)

        self.pushButton = QPushButton("Clear", self)
        self.pushButton.move(150, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Clear History")

        self.pushButton.clicked.connect(self.del_rec)

        self.pushButton = QPushButton("Show", self)
        self.pushButton.move(350, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Show History")

        self.pushButton.clicked.connect(self.show_his)

        self.pushButton = QPushButton("Exit", self)
        self.pushButton.move(550, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Close Window")

        self.pushButton.clicked.connect(self.returning)

    def del_rec(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            os.remove('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt')
            self.textans.clear()
        else:    
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)

    def show_his(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.hopn = open("HistorySub2.txt",'r')
            text = self.hopn.read()
            self.textans.setText(text)
            self.hopn.close()
        else:
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)
    def returning(self):
        self.close()



class WindowSub3x3(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("<h3> Subtraction <h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(430,50)
        self.label.move(430, 10)
       
        self.history = open("HistorySub3.txt", 'w')
        self.history.write("History\n")
        self.history.close()

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1050, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(80, 80)
        self.textbox1.resize(100,30)
        

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(180, 80)
        self.textbox2.resize(100,30)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(280,80)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(80, 110)
        self.textbox4.resize(100,30)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(180, 110)
        self.textbox5.resize(100,30)

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(280, 110)
        self.textbox6.resize(100,30)

        self.textbox7 = QLineEdit(self)
        self.textbox7.move(80, 140)
        self.textbox7.resize(100,30)

        self.textbox8 = QLineEdit(self)
        self.textbox8.move(180, 140)
        self.textbox8.resize(100,30)

        self.textbox9 = QLineEdit(self)
        self.textbox9.move(280, 140)
        self.textbox9.resize(100,30)

        self.textbox1a = QLineEdit(self)
        self.textbox1a.move(480, 80)
        self.textbox1a.resize(100,30)
        

        self.textbox2a = QLineEdit(self)
        self.textbox2a.move(580, 80)
        self.textbox2a.resize(100,30)

        self.textbox3a = QLineEdit(self)
        self.textbox3a.move(680,80)
        self.textbox3a.resize(100,30)

        self.textbox4a = QLineEdit(self)
        self.textbox4a.move(480, 110)
        self.textbox4a.resize(100,30)

        self.textbox5a = QLineEdit(self)
        self.textbox5a.move(580, 110)
        self.textbox5a.resize(100,30)

        self.textbox6a = QLineEdit(self)
        self.textbox6a.move(680, 110)
        self.textbox6a.resize(100,30)

        self.textbox7a = QLineEdit(self)
        self.textbox7a.move(480, 140)
        self.textbox7a.resize(100,30)

        self.textbox8a = QLineEdit(self)
        self.textbox8a.move(580, 140)
        self.textbox8a.resize(100,30)

        self.textbox9a = QLineEdit(self)
        self.textbox9a.move(680, 140)
        self.textbox9a.resize(100,30)

        self.det1 = QLineEdit(self)
        self.det1.setText("")
        self.det1.move(700, 200)
        self.det1.resize(100, 30)

        self.det2 = QLineEdit(self)
        self.det2.setText("")
        self.det2.move(800, 200)
        self.det2.resize(100, 30)

        self.det3 = QLineEdit(self)
        self.det3.setText("")
        self.det3.move(900, 200)
        self.det3.resize(100, 30)

        self.det4 = QLineEdit(self)
        self.det4.setText("")
        self.det4.move(700, 230)
        self.det4.resize(100, 30)

        self.det5 = QLineEdit(self)
        self.det5.setText("")
        self.det5.move(800, 230)
        self.det5.resize(100, 30)

        self.det6 = QLineEdit(self)
        self.det6.setText("")
        self.det6.move(900, 230)
        self.det6.resize(100, 30)

        self.det7 = QLineEdit(self)
        self.det7.setText("")
        self.det7.move(700, 260)
        self.det7.resize(100, 30)

        self.det8 = QLineEdit(self)
        self.det8.setText("")
        self.det8.move(800, 260)
        self.det8.resize(100, 30)

        self.det9 = QLineEdit(self)
        self.det9.setText("")
        self.det9.move(900, 260)
        self.det9.resize(100, 30)

        self.text = QLabel("<h3>Answer: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(600, 234)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix A: <h3>", self)
        self.text.setFont(QFont('Times',10 , QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(80, 60)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix B: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(480, 60)
        self.text.resize(150, 30)

        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Submit input")
        self.button.move(50,350)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Clear all ")
        self.button.move(450,350)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(850,350)
        self.button.clicked.connect(self.back) 

        self.button = QPushButton('History', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Show History")
        self.button.move(450,390)
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.button.clicked.connect(self.historycc)
        else:
            QMessageBox.warning(self, "Does not exist", "No existing history", QMessageBox.Ok, QMessageBox.Ok)

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(800,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()
    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
        self.textbox6.setText("")
        self.textbox7.setText("")
        self.textbox8.setText("")
        self.textbox9.setText("")
        self.textbox1a.setText("")
        self.textbox2a.setText("")
        self.textbox3a.setText("")
        self.textbox4a.setText("")
        self.textbox5a.setText("")
        self.textbox6a.setText("")
        self.textbox7a.setText("")
        self.textbox8a.setText("")
        self.textbox9a.setText("")

        self.det1.setText("")
        self.det2.setText("")
        self.det3.setText("")
        self.det4.setText("")
        self.det5.setText("")
        self.det6.setText("")
        self.det7.setText("")
        self.det8.setText("")
        self.det9.setText("")

        

    def data(self):
        if self.textbox1.text() != "" and self.textbox2.text() != "" and self.textbox3.text() != "" and self.textbox4.text() != "" and self.textbox5.text() != "" and self.textbox6.text() != "" and self.textbox7.text() != "" and self.textbox8.text() != ""and self.textbox9.text() != ""and self.textbox1a.text() != ""and self.textbox2a.text() != ""and self.textbox3a.text() != ""and self.textbox4a.text() != ""and self.textbox5a.text() != ""and self.textbox6a.text() != ""and self.textbox7a.text() != ""and self.textbox8a.text() != ""and self.textbox9a.text() != "":
            a = int(self.textbox1.text())
            b = int(self.textbox2.text())
            c = int(self.textbox3.text())
            d = int(self.textbox4.text())
            e = int(self.textbox5.text())
            f = int(self.textbox6.text())
            g = int(self.textbox7.text())
            h = int(self.textbox8.text())
            i = int(self.textbox9.text())
            j = int(self.textbox1a.text())
            k = int(self.textbox2a.text())
            l = int(self.textbox3a.text())
            m = int(self.textbox4a.text())
            n = int(self.textbox5a.text())
            o = int(self.textbox6a.text())
            p = int(self.textbox7a.text())
            q = int(self.textbox8a.text())
            r = int(self.textbox9a.text())
            self.matrix_computation(a, b, c, d, e, f, g, h, i, j,k,l,m,n,o,p,q,r,)
    
    def back(self):
        WindowSub3x3.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = WindowSUB()
        self.mnwndw.show()
    
    def historycc(self):
        self.open = HisS3()
        self.open.show()

    def matrix_computation(self,a, b, c, d, e, f, g, h, i, j,k,l,m,n,o,p,q,r,):
        A = (a-j)
       
        B = (b-k)
        C = (c-l)
        D = (d-m)
        E = (e-n)
        F = (f-o)
        G = (g-p)
        H = (h-q)
        I = (i-r)

        Determinate1 = A
        Determinate2 = B
        Determinate3 = C
        Determinate4 = D
        Determinate5 = E
        Determinate6 = F
        Determinate7 = G
        Determinate8 = H
        Determinate9 = I
        

        self.det1.setText(f"{Determinate1}")
        self.det2.setText(f"{Determinate2}")
        self.det3.setText(f"{Determinate3}")
        self.det4.setText(f"{Determinate4}")
        self.det5.setText(f"{Determinate5}")
        self.det6.setText(f"{Determinate6}")
        self.det7.setText(f"{Determinate7}")
        self.det8.setText(f"{Determinate8}")
        self.det9.setText(f"{Determinate9}")
        submitting = QMessageBox.information(self, "Processing", "Response being submitted. Do you wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if submitting == QMessageBox.Yes and a != "" and b != "" and c != "" and d != "" and e != "" and f != "" and g != "" and h != ""and i != ""and j != ""and k != ""and l != ""and m != ""and n != ""and o != ""and p != ""and q != ""and r != "":

            self.historia = open("HistorySub3.txt", 'a')
            self.historia.write("Inputs\n" + str(a)+"\n")
            self.historia.write(str(b)+"\n")
            self.historia.write(str(c)+"\n")
            self.historia.write(str(d)+"\n")
            self.historia.write(str(e)+"\n")
            self.historia.write(str(f)+"\n")
            self.historia.write(str(g)+"\n")
            self.historia.write(str(h)+"\n")
            self.historia.write(str(i)+"\n")
            self.historia.write(str(j)+"\n")
            self.historia.write(str(k)+"\n")
            self.historia.write(str(l)+"\n")
            self.historia.write(str(m)+"\n")
            self.historia.write(str(n)+"\n")
            self.historia.write(str(o)+"\n")
            self.historia.write(str(p)+"\n")
            self.historia.write(str(q)+"\n")
            self.historia.write(str(r)+"\n")
            self.historia.write("(1,1) is " + str(Determinate1)+"\n")
            self.historia.write("(1,2) is " + str(Determinate2) + "\n")
            self.historia.write("(1,3) is " + str(Determinate3)+"\n")
            self.historia.write("(2,1) is " + str(Determinate4)+"\n")
            self.historia.write("(2,2) is " + str(Determinate5)+"\n")
            self.historia.write("(2,3) is " + str(Determinate6)+"\n")
            self.historia.write("(3,1) is " + str(Determinate7)+"\n")
            self.historia.write("(3,2) is " + str(Determinate8)+"\n")
            self.historia.write("(3,3) is " + str(Determinate9)+"\n")
            
            self.historia.close()
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and a == "" and b == "" and c == "" and d == "" and e == "" and f == "" and g == "" and h == ""and i == ""and j == ""and k ==""and l == ""and m == ""and n == ""and o == ""and p == ""and q == ""and r == "":
            pass
        elif submitting == QMessageBox.No and a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == ""or i == ""or j == ""or k == ""or l == ""or m == ""or n == ""or o == ""or p == ""or q == ""or r == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)

class HisS3(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "3x3 Substraction History"
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.history = open("HistorySub3.txt", 'r')
            self.history.read()
            self.history.close()
        else:
            QMessageBox.warning(self, "Error", "History does not exists!", QMessageBox.Ok, QMessageBox.Ok)

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
        self.setWindowIcon(QIcon('custom.ico'))
        self.textans = QTextEdit(self)
        self.textans.setText("")
        self.textans.resize(800, 450)

        self.pushButton = QPushButton("Clear", self)
        self.pushButton.move(150, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Clear History")

        self.pushButton.clicked.connect(self.del_rec)

        self.pushButton = QPushButton("Show", self)
        self.pushButton.move(350, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Show History")

        self.pushButton.clicked.connect(self.show_his)

        self.pushButton = QPushButton("Exit", self)
        self.pushButton.move(550, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Close Window")

        self.pushButton.clicked.connect(self.returning)

    def del_rec(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            os.remove('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt')
            self.textans.clear()
        else:    
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)

    def show_his(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.hopn = open("HistorySub3.txt",'r')
            text = self.hopn.read()
            self.textans.setText(text)
            self.hopn.close()
        else:
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)
    def returning(self):
        self.close()


class WindowSub4x4(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("<h3> Subtraction <h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(500,50)
        self.label.move(430, 10)
       
        self.history = open("HistorySub4.txt", 'w')
        self.history.write("History\n")
        self.history.close()

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(50, 80)
        self.textbox1.resize(100,30)
    
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(150, 80)
        self.textbox2.resize(100,30)
        

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(250, 80)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(350,80)
        self.textbox4.resize(100,30)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(50, 110)
        self.textbox5.resize(100,30)

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(150, 110)
        self.textbox6.resize(100,30)

        self.textbox7 = QLineEdit(self)
        self.textbox7.move(250, 110)
        self.textbox7.resize(100,30)

        self.textbox8 = QLineEdit(self)
        self.textbox8.move(350, 110)
        self.textbox8.resize(100,30)

        self.textbox9 = QLineEdit(self)
        self.textbox9.move(50, 140)
        self.textbox9.resize(100,30)

        self.textbox10 = QLineEdit(self)
        self.textbox10.move(150, 140)
        self.textbox10.resize(100,30)

        self.textbox11 = QLineEdit(self)
        self.textbox11.move(250, 140)
        self.textbox11.resize(100,30)

        self.textbox12 = QLineEdit(self)
        self.textbox12.move(350, 140)
        self.textbox12.resize(100,30)

        self.textbox13 = QLineEdit(self)
        self.textbox13.move(50, 170)
        self.textbox13.resize(100,30)

        self.textbox14 = QLineEdit(self)
        self.textbox14.move(150, 170)
        self.textbox14.resize(100,30)

        self.textbox15 = QLineEdit(self)
        self.textbox15.move(250, 170)
        self.textbox15.resize(100,30)

        self.textbox16 = QLineEdit(self)
        self.textbox16.move(350, 170)
        self.textbox16.resize(100,30)

        self.textbox1a = QLineEdit(self)
        self.textbox1a.move(580, 80)
        self.textbox1a.resize(100,30)
    
        self.textbox2a = QLineEdit(self)
        self.textbox2a.move(680, 80)
        self.textbox2a.resize(100,30)
        

        self.textbox3a = QLineEdit(self)
        self.textbox3a.move(780, 80)
        self.textbox3a.resize(100,30)

        self.textbox4a = QLineEdit(self)
        self.textbox4a.move(880,80)
        self.textbox4a.resize(100,30)

        self.textbox5a = QLineEdit(self)
        self.textbox5a.move(580, 110)
        self.textbox5a.resize(100,30)

        self.textbox6a = QLineEdit(self)
        self.textbox6a.move(680, 110)
        self.textbox6a.resize(100,30)

        self.textbox7a = QLineEdit(self)
        self.textbox7a.move(780, 110)
        self.textbox7a.resize(100,30)

        self.textbox8a = QLineEdit(self)
        self.textbox8a.move(880, 110)
        self.textbox8a.resize(100,30)

        self.textbox9a = QLineEdit(self)
        self.textbox9a.move(580, 140)
        self.textbox9a.resize(100,30)

        self.textbox10a = QLineEdit(self)
        self.textbox10a.move(680, 140)
        self.textbox10a.resize(100,30)

        self.textbox11a = QLineEdit(self)
        self.textbox11a.move(780, 140)
        self.textbox11a.resize(100,30)

        self.textbox12a = QLineEdit(self)
        self.textbox12a.move(880, 140)
        self.textbox12a.resize(100,30)

        self.textbox13a = QLineEdit(self)
        self.textbox13a.move(580, 170)
        self.textbox13a.resize(100,30)

        self.textbox14a = QLineEdit(self)
        self.textbox14a.move(680, 170)
        self.textbox14a.resize(100,30)

        self.textbox15a = QLineEdit(self)
        self.textbox15a.move(780, 170)
        self.textbox15a.resize(100,30)

        self.textbox16a = QLineEdit(self)
        self.textbox16a.move(880, 170)
        self.textbox16a.resize(100,30)

        self.det1 = QLineEdit(self)
        self.det1.setText("")
        self.det1.move(580, 300)
        self.det1.resize(100, 30)

        self.det2 = QLineEdit(self)
        self.det2.setText("")
        self.det2.move(680, 300)
        self.det2.resize(100, 30)

        self.det3 = QLineEdit(self)
        self.det3.setText("")
        self.det3.move(780, 300)
        self.det3.resize(100, 30)

        self.det4 = QLineEdit(self)
        self.det4.setText("")
        self.det4.move(880, 300)
        self.det4.resize(100, 30)

        self.det5 = QLineEdit(self)
        self.det5.setText("")
        self.det5.move(580, 330)
        self.det5.resize(100, 30)

        self.det6 = QLineEdit(self)
        self.det6.setText("")
        self.det6.move(680, 330)
        self.det6.resize(100, 30)

        self.det7 = QLineEdit(self)
        self.det7.setText("")
        self.det7.move(780, 330)
        self.det7.resize(100, 30)

        self.det8 = QLineEdit(self)
        self.det8.setText("")
        self.det8.move(880, 330)
        self.det8.resize(100, 30)

        self.det9 = QLineEdit(self)
        self.det9.setText("")
        self.det9.move(580, 360)
        self.det9.resize(100, 30)

        self.det10 = QLineEdit(self)
        self.det10.setText("")
        self.det10.move(680, 360)
        self.det10.resize(100, 30)

        self.det11 = QLineEdit(self)
        self.det11.setText("")
        self.det11.move(780, 360)
        self.det11.resize(100, 30)

        self.det12 = QLineEdit(self)
        self.det12.setText("")
        self.det12.move(880, 360)
        self.det12.resize(100, 30)

        self.det13 = QLineEdit(self)
        self.det13.setText("")
        self.det13.move(580, 390)
        self.det13.resize(100, 30)

        self.det14 = QLineEdit(self)
        self.det14.setText("")
        self.det14.move(680, 390)
        self.det14.resize(100, 30)

        self.det15 = QLineEdit(self)
        self.det15.setText("")
        self.det15.move(780, 390)
        self.det15.resize(100, 30)

        self.det16 = QLineEdit(self)
        self.det16.setText("")
        self.det16.move(880, 390)
        self.det16.resize(100, 30)

        self.text = QLabel("<h3>Answer: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(580, 275)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix A: <h3>", self)
        self.text.setFont(QFont('Times',10 , QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(50, 55)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix B: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(580, 55)
        self.text.resize(150, 30)

        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Submit input")
        self.button.move(50,360)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Clear all ")
        self.button.move(200,360)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(350,360)
        self.button.clicked.connect(self.back) 
        
        self.button = QPushButton('History', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Show History")
        self.button.move(200,390)
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.button.clicked.connect(self.historycc)
        else:
            QMessageBox.warning(self, "Does not exist", "No existing history", QMessageBox.Ok, QMessageBox.Ok)

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(800,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()
    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
        self.textbox6.setText("")
        self.textbox7.setText("")
        self.textbox8.setText("")
        self.textbox9.setText("")
        self.textbox10.setText("")
        self.textbox11.setText("")
        self.textbox12.setText("")
        self.textbox13.setText("")
        self.textbox14.setText("")
        self.textbox15.setText("")
        self.textbox16.setText("")
    
        self.textbox1a.setText("")
        self.textbox2a.setText("")
        self.textbox3a.setText("")
        self.textbox4a.setText("")
        self.textbox5a.setText("")
        self.textbox6a.setText("")
        self.textbox7a.setText("")
        self.textbox8a.setText("")
        self.textbox9a.setText("")
        self.textbox10a.setText("")
        self.textbox11a.setText("")
        self.textbox12a.setText("")
        self.textbox13a.setText("")
        self.textbox14a.setText("")
        self.textbox15a.setText("")
        self.textbox16a.setText("")

        self.det1.setText("")
        self.det2.setText("")
        self.det3.setText("")
        self.det4.setText("")
        self.det5.setText("")
        self.det6.setText("")
        self.det7.setText("")
        self.det8.setText("")
        self.det9.setText("")
        self.det10.setText("")
        self.det11.setText("")
        self.det12.setText("")
        self.det13.setText("")
        self.det14.setText("")
        self.det15.setText("")
        self.det16.setText("")


        

    def data(self):
        if self.textbox1.text() != "" and self.textbox2.text() !=  "" and self.textbox3.text() != "" and self.textbox4.text() != "" and self.textbox5.text() != "" and self.textbox6.text() != ""and self.textbox7.text() != "" and self.textbox8.text() != ""and  self.textbox9.text() != "" and self.textbox10.text() != "" and self.textbox11.text() != "" and self.textbox12.text() != "" and self.textbox13.text() != "" and self.textbox14.text() != "" and self.textbox15.text() != "" and self.textbox16.text() != "":
            a = int(self.textbox1.text())
            b = int(self.textbox2.text())
            c = int(self.textbox3.text())
            d = int(self.textbox4.text())
            e = int(self.textbox5.text())
            f = int(self.textbox6.text())
            g = int(self.textbox7.text())
            h = int(self.textbox8.text())
            i = int(self.textbox9.text())
            j = int(self.textbox10.text())
            k = int(self.textbox11.text())
            l = int(self.textbox12.text())
            m = int(self.textbox13.text())
            n = int(self.textbox14.text())
            o = int(self.textbox15.text())
            p = int(self.textbox16.text())
            

            aa = int(self.textbox1a.text())
            bb = int(self.textbox2a.text())
            cc = int(self.textbox3a.text())
            dd = int(self.textbox4a.text())
            ee = int(self.textbox5a.text())
            ff = int(self.textbox6a.text())
            gg = int(self.textbox7a.text())
            hh = int(self.textbox8a.text())
            ii = int(self.textbox9a.text())
            jj = int(self.textbox10a.text())
            kk = int(self.textbox11a.text())
            ll = int(self.textbox12a.text())
            mm = int(self.textbox13a.text())
            nn = int(self.textbox14a.text())
            oo = int(self.textbox15a.text())
            pp = int(self.textbox16a.text())
            self.matrix_computation(a, b, c, d, e, f, g, h, i, j,k,l,m,n,o,p,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp)
    
    def back(self):
        WindowSub4x4.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = WindowSUB()
        self.mnwndw.show()
    
    def historycc(self):
        self.open = HisS4()
        self.open.show()

    def matrix_computation(self,a, b, c, d, e, f, g, h, i, j,k,l,m,n,o,p,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp):
        A = (a-aa)
        B = (b-bb)
        C = (c-cc)
        D = (d-dd)
        E = (e-ee)
        F = (f-ff)
        G = (g-gg)
        H = (h-hh)
        I = (i-ii)
        J = (j-jj)
        K = (k-kk)
        L = (l-ll)
        M = (m-mm)
        N = (n-nn)
        O = (o-oo)
        P = (p-pp)

        Determinate1 = A
        Determinate2 = B
        Determinate3 = C
        Determinate4 = D
        Determinate5 = E
        Determinate6 = F
        Determinate7 = G
        Determinate8 = H
        Determinate9 = I
        Determinate10 = J
        Determinate11 = K
        Determinate12 = L
        Determinate13 = M
        Determinate14 = N
        Determinate15 = O
        Determinate16 = P
        

        self.det1.setText(f"{Determinate1}")
        self.det2.setText(f"{Determinate2}")
        self.det3.setText(f"{Determinate3}")
        self.det4.setText(f"{Determinate4}")
        self.det5.setText(f"{Determinate5}")
        self.det6.setText(f"{Determinate6}")
        self.det7.setText(f"{Determinate7}")
        self.det8.setText(f"{Determinate8}")
        self.det9.setText(f"{Determinate9}")
        self.det10.setText(f"{Determinate10}")
        self.det11.setText(f"{Determinate11}")
        self.det12.setText(f"{Determinate12}")
        self.det13.setText(f"{Determinate13}")
        self.det14.setText(f"{Determinate14}")
        self.det15.setText(f"{Determinate15}")
        self.det16.setText(f"{Determinate16}")
        submitting = QMessageBox.information(self, "Processing", "Response being submitted. Do you wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if submitting == QMessageBox.Yes and a != "" and b != "" and c != "" and d != "" and e != "" and f != "" and g != "" and h != ""and i != ""and j != ""and k != ""and l != ""and m != ""and n != ""and o != ""and p != ""and aa != ""and bb != "" and cc != "" and dd != "" and ee != ""and  ff != "" and gg != ""and hh != ""and ii != ""and jj != ""and kk != ""and ll != ""and mm != ""and nn != "" and oo != "" and pp != "":

            self.historia = open("HistorySub4.txt", 'a')
            self.historia.write("Inputs\n" + str(a)+"\n")
            self.historia.write(str(b)+"\n")
            self.historia.write(str(c)+"\n")
            self.historia.write(str(d)+"\n")
            self.historia.write(str(e)+"\n")
            self.historia.write(str(f)+"\n")
            self.historia.write(str(g)+"\n")
            self.historia.write(str(h)+"\n")
            self.historia.write(str(i)+"\n")
            self.historia.write(str(j)+"\n")
            self.historia.write(str(k)+"\n")
            self.historia.write(str(l)+"\n")
            self.historia.write(str(m)+"\n")
            self.historia.write(str(n)+"\n")
            self.historia.write(str(o)+"\n")
            self.historia.write(str(p)+"\n")
        
            self.historia.write(str(aa)+"\n")
            self.historia.write(str(bb)+"\n")
            self.historia.write(str(cc)+"\n")
            self.historia.write(str(dd)+"\n")
            self.historia.write(str(ee)+"\n")
            self.historia.write(str(ff)+"\n")
            self.historia.write(str(gg)+"\n")
            self.historia.write(str(hh)+"\n")
            self.historia.write(str(ii)+"\n")
            self.historia.write(str(jj)+"\n")
            self.historia.write(str(kk)+"\n")
            self.historia.write(str(ll)+"\n")
            self.historia.write(str(mm)+"\n")
            self.historia.write(str(nn)+"\n")
            self.historia.write(str(oo)+"\n")
            self.historia.write(str(pp)+"\n")
            
            self.historia.write("(1,1) is " + str(Determinate1)+"\n")
            self.historia.write("(1,2) is " + str(Determinate2) + "\n")
            self.historia.write("(1,3) is " + str(Determinate3)+"\n")
            self.historia.write("(1,4) is " + str(Determinate4)+"\n")
            self.historia.write("(2,1) is " + str(Determinate5)+"\n")
            self.historia.write("(2,2) is " + str(Determinate6)+"\n")
            self.historia.write("(2,3) is " + str(Determinate7)+"\n")
            self.historia.write("(2,4) is " + str(Determinate8)+"\n")
            self.historia.write("(3,1) is " + str(Determinate9)+"\n")
            self.historia.write("(3,2) is " + str(Determinate10)+"\n")
            self.historia.write("(3,3) is " + str(Determinate11) + "\n")
            self.historia.write("(3,4) is " + str(Determinate12)+"\n")
            self.historia.write("(4,1) is " + str(Determinate13)+"\n")
            self.historia.write("(4,2) is " + str(Determinate14)+"\n")
            self.historia.write("(4,3) is " + str(Determinate15)+"\n")
            self.historia.write("(4,4) is " + str(Determinate16)+"\n")
            self.historia.close()
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and a == "" and b == "" and c == "" and d == "" and e == "" and f == "" and g == "" and h == ""and i == ""and j == ""and k ==""and l == ""and m == ""and n == ""and o == ""and p == "" and aa == "" and bb == "" and cc == "" and dd == "" and ee == "" and ff == "" and gg == "" and hh == ""and ii == ""and jj == ""and kk ==""and ll == ""and mm == ""and nn == ""and oo == ""and pp == "":
            pass
        elif submitting == QMessageBox.No and a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == ""or i == ""or j == ""or k =="" or l == ""or m == ""or n == "" or o == ""or p == "" or aa == "" or bb == "" or cc == ""or dd == "" or ee == "" or ff == ""or gg == "" or hh == ""or ii == ""or jj == ""or kk ==""or ll == ""or mm == ""or nn == ""or oo == ""or pp == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)

class HisS4(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "4x4 Subtraction History"
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.history = open("HistorySub4.txt", 'r')
            self.history.read()
            self.history.close()
        else:
            QMessageBox.warning(self, "Error", "History does not exists!", QMessageBox.Ok, QMessageBox.Ok)

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
        self.setWindowIcon(QIcon('custom.ico'))
        self.textans = QTextEdit(self)
        self.textans.setText("")
        self.textans.resize(800, 450)

        self.pushButton = QPushButton("Clear", self)
        self.pushButton.move(150, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Clear History")

        self.pushButton.clicked.connect(self.del_rec)

        self.pushButton = QPushButton("Show", self)
        self.pushButton.move(350, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Show History")

        self.pushButton.clicked.connect(self.show_his)

        self.pushButton = QPushButton("Exit", self)
        self.pushButton.move(550, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Close Window")

        self.pushButton.clicked.connect(self.returning)

    def del_rec(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            os.remove('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt')
            self.textans.clear()
        else:    
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)

    def show_his(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.hopn = open("HistorySub4.txt",'r')
            text = self.hopn.read()
            self.textans.setText(text)
            self.hopn.close()
        else:
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)
    def returning(self):
        self.close()

class WindowSUB(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Determinant Calculator"
        
        self.pushButton = QPushButton("2 X 2", self)
        self.pushButton.move(100, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt ; }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.window2sub) 

        self.pushButton = QPushButton("3 X 3", self)
        self.pushButton.move(300, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.window3sub)

        self.pushButton = QPushButton("4 X 4", self)
        self.pushButton.move(500, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.window4sub)             
        

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight : bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(300,450)
        self.button.clicked.connect(self.back)
        
        self.main_window()

    def main_window(self):
       
        self.label = QLabel("<h3>Matrix Calculator<h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: white;}')
        
        self.label.resize(500,50)
        self.label.move(210, 50) 
        self.setWindowTitle(self.title)
        self.setGeometry(350, 100, 700, 500)
     
        #background
        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(680,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        self.show()

    def back(self):
        WindowSUB.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = MainWindow()
        self.mnwndw.show()
    


    def window2sub(self):
        self.w = WindowSub2x2()
        self.w.show()
        MainWindow.close(self)
    
    def window3sub(self):
        self.w = WindowSub3x3()
        self.w.show()
        MainWindow.close(self)

    def window4sub(self):
        self.w = WindowSub4x4()
        self.w.show()
        MainWindow.close(self)
    
    
   
    def history(self):
        pass

class WindowMultiply2x2(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("Multiplication", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(500,50)
        self.label.move(430, 10)
       
        self.history = open("HistoryMultiply2.txt", 'w')
        self.history.write("History\n")
        self.history.close()

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(80, 80)
        self.textbox1.resize(100,30)
        

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(180, 80)
        self.textbox2.resize(100,30)

        

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(80, 110)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(180, 110)
        self.textbox4.resize(100,30)

       

       
        self.textbox1a = QLineEdit(self)
        self.textbox1a.move(480, 80)
        self.textbox1a.resize(100,30)
        

        self.textbox2a = QLineEdit(self)
        self.textbox2a.move(580, 80)
        self.textbox2a.resize(100,30)

        self.textbox3a = QLineEdit(self)
        self.textbox3a.move(480, 110)
        self.textbox3a.resize(100,30)

        self.textbox4a = QLineEdit(self)
        self.textbox4a.move(580, 110)
        self.textbox4a.resize(100,30)

        self.det1 = QLineEdit(self)
        self.det1.setText("")
        self.det1.move(700, 200)
        self.det1.resize(100, 30)

        self.det2 = QLineEdit(self)
        self.det2.setText("")
        self.det2.move(800, 200)
        self.det2.resize(100, 30)

        self.det3 = QLineEdit(self)
        self.det3.setText("")
        self.det3.move(700, 230)
        self.det3.resize(100, 30)

        self.det4 = QLineEdit(self)
        self.det4.setText("")
        self.det4.move(800, 230)
        self.det4.resize(100, 30)

        self.text = QLabel("<h3>Answer: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(600, 234)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix A: <h3>", self)
        self.text.setFont(QFont('Times',10 , QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(80, 60)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix B: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(480, 60)
        self.text.resize(150, 30)

        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Submit input")
        self.button.move(50,350)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Clear all ")
        self.button.move(450,350)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(850,350)
        self.button.clicked.connect(self.back) 

        self.button = QPushButton('History', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Show History")
        self.button.move(450,390)
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.button.clicked.connect(self.historycc)
        else:
            QMessageBox.warning(self, "Does not exist", "No existing history", QMessageBox.Ok, QMessageBox.Ok)

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(800,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()
    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
       
        self.textbox1a.setText("")
        self.textbox2a.setText("")
        self.textbox3a.setText("")
        self.textbox4a.setText("")
        self.det1.setText("")
        self.det2.setText("")
        self.det3.setText("")
        self.det4.setText("")
        

        

    def data(self):
        if self.textbox1.text() != "" and self.textbox2.text() != "" and self.textbox3.text() != "" and self.textbox4.text() != "" and self.textbox1a.text() != "" and self.textbox2a.text() != "" and self.textbox3a.text() != "" and self.textbox4a.text() != "":
            a = int(self.textbox1.text())
            b = int(self.textbox2.text())
            c = int(self.textbox3.text())
            d = int(self.textbox4.text())
            e = int(self.textbox1a.text())
            f = int(self.textbox2a.text())
            g = int(self.textbox3a.text())
            h = int(self.textbox4a.text())
            self.matrix_computation(a, b, c, d, e, f, g, h)
        elif self.textbox1.text() == "" and self.textbox2.text() == "" and self.textbox3.text() == "" and self.textbox4.text() == "" and self.textbox1a.text() == "" and self.textbox2a.text() == "" and self.textbox3a.text() == "" and self.textbox4a.text() == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)
        elif self.textbox1.text() == "" or self.textbox2.text() == "" or self.textbox3.text() == "" or self.textbox4.text() == "" or self.textbox1a.text() == "" or self.textbox2a.text() == "" or self.textbox3a.text() == "" or self.textbox4a.text() == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)


    def back(self):
        WindowMultiply2x2.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = windowMULTIPLY()
        self.mnwndw.show()
    
    def historycc(self):
        self.open = HisM2()
        self.open.show()

    def matrix_computation(self,a, b, c, d, e, f, g, h):
        A = ((a*e)+(b*g))
        B = ((a*f)+(b*h))
        C = ((c*e)+(d*g))
        D = ((c*e)+(d*g))
        

        Determinate1 = A
        Determinate2 = B
        Determinate3 = C
        Determinate4 = D
       
        

        self.det1.setText(f"{Determinate1}")
        self.det2.setText(f"{Determinate2}")
        self.det3.setText(f"{Determinate3}")
        self.det4.setText(f"{Determinate4}")
        submitting = QMessageBox.information(self, "Processing", "Response being submitted. Do you wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if submitting == QMessageBox.Yes and a != "" and b != "" and c != "" and d != "" and e != "" and f != "" and g != "" and h != "":
            self.historia = open("HistoryMultiply2.txt", 'a')
            self.historia.write("Inputs\n" + str(a)+"\n")
            self.historia.write(str(b)+"\n")
            self.historia.write(str(c)+"\n")
            self.historia.write(str(d)+"\n")
            self.historia.write(str(e)+"\n")
            self.historia.write(str(f)+"\n")
            self.historia.write(str(g)+"\n")
            self.historia.write(str(h)+"\n")
            self.historia.write("(1,1) is " + str(Determinate1)+"\n")
            self.historia.write("(1,2) is " + str(Determinate2) + "\n")
            self.historia.write("(2,1) is " + str(Determinate3)+"\n")
            self.historia.write("(2,2) is " + str(Determinate4)+"\n")
            self.historia.close()
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and a == "" and b == "" and c == "" and d == "" and e == "" and f == "" and g == "" and h == "":
            pass
        elif submitting == QMessageBox.No and a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)
class HisM2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "2x2 Multiplication History"
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.history = open("HistoryMultiply2.txt", 'r')
            self.history.read()
            self.history.close()
        else:
            QMessageBox.warning(self, "Error", "History does not exists!", QMessageBox.Ok, QMessageBox.Ok)

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
        self.setWindowIcon(QIcon('custom.ico'))
        self.textans = QTextEdit(self)
        self.textans.setText("")
        self.textans.resize(800, 450)

        self.pushButton = QPushButton("Clear", self)
        self.pushButton.move(150, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Clear History")

        self.pushButton.clicked.connect(self.del_rec)

        self.pushButton = QPushButton("Show", self)
        self.pushButton.move(350, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Show History")

        self.pushButton.clicked.connect(self.show_his)

        self.pushButton = QPushButton("Exit", self)
        self.pushButton.move(550, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Close Window")

        self.pushButton.clicked.connect(self.returning)

    def del_rec(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            os.remove('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt')
            self.textans.clear()
        else:    
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)

    def show_his(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.hopn = open("HistoryMultiply2.txt",'r')
            text = self.hopn.read()
            self.textans.setText(text)
            self.hopn.close()
        else:
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)
    def returning(self):
        self.close()        


class WindowMultiply3x3(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("<h3> Multiplication  <h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(430,50)
        self.label.move(430, 10)
       
        self.history = open("HistoryMultiply3.txt", 'w')
        self.history.write("History\n")
        self.history.close()

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1050, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(80, 80)
        self.textbox1.resize(100,30)
        

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(180, 80)
        self.textbox2.resize(100,30)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(280,80)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(80, 110)
        self.textbox4.resize(100,30)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(180, 110)
        self.textbox5.resize(100,30)

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(280, 110)
        self.textbox6.resize(100,30)

        self.textbox7 = QLineEdit(self)
        self.textbox7.move(80, 140)
        self.textbox7.resize(100,30)

        self.textbox8 = QLineEdit(self)
        self.textbox8.move(180, 140)
        self.textbox8.resize(100,30)

        self.textbox9 = QLineEdit(self)
        self.textbox9.move(280, 140)
        self.textbox9.resize(100,30)

        self.textbox1a = QLineEdit(self)
        self.textbox1a.move(480, 80)
        self.textbox1a.resize(100,30)
        

        self.textbox2a = QLineEdit(self)
        self.textbox2a.move(580, 80)
        self.textbox2a.resize(100,30)

        self.textbox3a = QLineEdit(self)
        self.textbox3a.move(680,80)
        self.textbox3a.resize(100,30)

        self.textbox4a = QLineEdit(self)
        self.textbox4a.move(480, 110)
        self.textbox4a.resize(100,30)

        self.textbox5a = QLineEdit(self)
        self.textbox5a.move(580, 110)
        self.textbox5a.resize(100,30)

        self.textbox6a = QLineEdit(self)
        self.textbox6a.move(680, 110)
        self.textbox6a.resize(100,30)

        self.textbox7a = QLineEdit(self)
        self.textbox7a.move(480, 140)
        self.textbox7a.resize(100,30)

        self.textbox8a = QLineEdit(self)
        self.textbox8a.move(580, 140)
        self.textbox8a.resize(100,30)

        self.textbox9a = QLineEdit(self)
        self.textbox9a.move(680, 140)
        self.textbox9a.resize(100,30)

        self.det1 = QLineEdit(self)
        self.det1.setText("")
        self.det1.move(700, 200)
        self.det1.resize(100, 30)

        self.det2 = QLineEdit(self)
        self.det2.setText("")
        self.det2.move(800, 200)
        self.det2.resize(100, 30)

        self.det3 = QLineEdit(self)
        self.det3.setText("")
        self.det3.move(900, 200)
        self.det3.resize(100, 30)

        self.det4 = QLineEdit(self)
        self.det4.setText("")
        self.det4.move(700, 230)
        self.det4.resize(100, 30)

        self.det5 = QLineEdit(self)
        self.det5.setText("")
        self.det5.move(800, 230)
        self.det5.resize(100, 30)

        self.det6 = QLineEdit(self)
        self.det6.setText("")
        self.det6.move(900, 230)
        self.det6.resize(100, 30)

        self.det7 = QLineEdit(self)
        self.det7.setText("")
        self.det7.move(700, 260)
        self.det7.resize(100, 30)

        self.det8 = QLineEdit(self)
        self.det8.setText("")
        self.det8.move(800, 260)
        self.det8.resize(100, 30)

        self.det9 = QLineEdit(self)
        self.det9.setText("")
        self.det9.move(900, 260)
        self.det9.resize(100, 30)

        self.text = QLabel("<h3>Answer: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(600, 234)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix A: <h3>", self)
        self.text.setFont(QFont('Times',10 , QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(80, 60)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix B: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(480, 60)
        self.text.resize(150, 30)

        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Submit input")
        self.button.move(50,350)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Clear all ")
        self.button.move(450,350)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(850,350)
        self.button.clicked.connect(self.back) 

        self.button = QPushButton('History', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Show History")
        self.button.move(450,390)
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.button.clicked.connect(self.historycc)
        else:
            QMessageBox.warning(self, "Does not exist", "No existing history", QMessageBox.Ok, QMessageBox.Ok)
        

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(800,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()
    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
        self.textbox6.setText("")
        self.textbox7.setText("")
        self.textbox8.setText("")
        self.textbox9.setText("")
        self.textbox1a.setText("")
        self.textbox2a.setText("")
        self.textbox3a.setText("")
        self.textbox4a.setText("")
        self.textbox5a.setText("")
        self.textbox6a.setText("")
        self.textbox7a.setText("")
        self.textbox8a.setText("")
        self.textbox9a.setText("")

        self.det1.setText("")
        self.det2.setText("")
        self.det3.setText("")
        self.det4.setText("")
        self.det5.setText("")
        self.det6.setText("")
        self.det7.setText("")
        self.det8.setText("")
        self.det9.setText("")

        

    def data(self):
        if self.textbox1.text() != "" and self.textbox2.text() != "" and self.textbox3.text() != "" and self.textbox4.text() != "" and self.textbox5.text() != "" and self.textbox6.text() != "" and self.textbox7.text() != "" and self.textbox8.text() != ""and self.textbox9.text() != ""and self.textbox1a.text() != ""and self.textbox2a.text() != ""and self.textbox3a.text() != ""and self.textbox4a.text() != ""and self.textbox5a.text() != ""and self.textbox6a.text() != ""and self.textbox7a.text() != ""and self.textbox8a.text() != ""and self.textbox9a.text() != "":
            a = int(self.textbox1.text())
            b = int(self.textbox2.text())
            c = int(self.textbox3.text())
            d = int(self.textbox4.text())
            e = int(self.textbox5.text())
            f = int(self.textbox6.text())
            g = int(self.textbox7.text())
            h = int(self.textbox8.text())
            i = int(self.textbox9.text())
            j = int(self.textbox1a.text())
            k = int(self.textbox2a.text())
            l = int(self.textbox3a.text())
            m = int(self.textbox4a.text())
            n = int(self.textbox5a.text())
            o = int(self.textbox6a.text())
            p = int(self.textbox7a.text())
            q = int(self.textbox8a.text())
            r = int(self.textbox9a.text())
            self.matrix_computation(a, b, c, d, e, f, g, h, i, j,k,l,m,n,o,p,q,r,)
    
    def back(self):
        WindowMultiply3x3.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = windowMULTIPLY()
        self.mnwndw.show()
    def historycc(self):
        self.open = HisM3()
        self.open.show()

    def matrix_computation(self,a, b, c, d, e, f, g, h, i, j,k,l,m,n,o,p,q,r,):
        A = ((a*j)+(b*m)+(c*p))
        B = ((a*k)+(b*n)+(c*q))
        C = ((a*l)+(b*o)+(c*r))
        D = ((d*j)+(e*m)+(f*p))
        E = ((d*k)+(e*n)+(f*q))
        F = ((d*l)+(e*o)+(f*r))
        G = ((g*j)+(h*m)+(i*p))
        H = ((g*k)+(h*n)+(i*q))
        I = ((g*l)+(h*o)+(i*r))

        Determinate1 = A
        Determinate2 = B
        Determinate3 = C
        Determinate4 = D
        Determinate5 = E
        Determinate6 = F
        Determinate7 = G
        Determinate8 = H
        Determinate9 = I
        

        self.det1.setText(f"{Determinate1}")
        self.det2.setText(f"{Determinate2}")
        self.det3.setText(f"{Determinate3}")
        self.det4.setText(f"{Determinate4}")
        self.det5.setText(f"{Determinate5}")
        self.det6.setText(f"{Determinate6}")
        self.det7.setText(f"{Determinate7}")
        self.det8.setText(f"{Determinate8}")
        self.det9.setText(f"{Determinate9}")
        submitting = QMessageBox.information(self, "Processing", "Response being submitted. Do you wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if submitting == QMessageBox.Yes and a != "" and b != "" and c != "" and d != "" and e != "" and f != "" and g != "" and h != ""and i != ""and j != ""and k != ""and l != ""and m != ""and n != ""and o != ""and p != ""and q != ""and r != "":

            self.historia = open("HistoryAdd3.txt", 'a')
            self.historia.write("Inputs\n" + str(a)+"\n")
            self.historia.write(str(b)+"\n")
            self.historia.write(str(c)+"\n")
            self.historia.write(str(d)+"\n")
            self.historia.write(str(e)+"\n")
            self.historia.write(str(f)+"\n")
            self.historia.write(str(g)+"\n")
            self.historia.write(str(h)+"\n")
            self.historia.write(str(i)+"\n")
            self.historia.write(str(j)+"\n")
            self.historia.write(str(k)+"\n")
            self.historia.write(str(l)+"\n")
            self.historia.write(str(m)+"\n")
            self.historia.write(str(n)+"\n")
            self.historia.write(str(o)+"\n")
            self.historia.write(str(p)+"\n")
            self.historia.write(str(q)+"\n")
            self.historia.write(str(r)+"\n")
            self.historia.write("(1,1) is " + str(Determinate1)+"\n")
            self.historia.write("(1,2) is " + str(Determinate2) + "\n")
            self.historia.write("(1,3) is " + str(Determinate3)+"\n")
            self.historia.write("(2,1) is " + str(Determinate4)+"\n")
            self.historia.write("(2,2) is " + str(Determinate5)+"\n")
            self.historia.write("(2,3) is " + str(Determinate6)+"\n")
            self.historia.write("(3,1) is " + str(Determinate7)+"\n")
            self.historia.write("(3,2) is " + str(Determinate8)+"\n")
            self.historia.write("(3,3) is " + str(Determinate9)+"\n")
            
            self.historia.close()
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and a == "" and b == "" and c == "" and d == "" and e == "" and f == "" and g == "" and h == ""and i == ""and j == ""and k ==""and l == ""and m == ""and n == ""and o == ""and p == ""and q == ""and r == "":
            pass
        elif submitting == QMessageBox.No and a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == ""or i == ""or j == ""or k == ""or l == ""or m == ""or n == ""or o == ""or p == ""or q == ""or r == "":
            QMessageBox.warning(self, "Invalid", "Don't leave any blank spaces", QMessageBox.Ok, QMessageBox.Ok)

class HisM3(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "3x3 Multiplication History"
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.history = open("HistoryMultiply3.txt", 'r')
            self.history.read()
            self.history.close()
        else:
            QMessageBox.warning(self, "Error", "History does not exists!", QMessageBox.Ok, QMessageBox.Ok)

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
        self.setWindowIcon(QIcon('custom.ico'))
        self.textans = QTextEdit(self)
        self.textans.setText("")
        self.textans.resize(800, 450)

        self.pushButton = QPushButton("Clear", self)
        self.pushButton.move(150, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Clear History")

        self.pushButton.clicked.connect(self.del_rec)

        self.pushButton = QPushButton("Show", self)
        self.pushButton.move(350, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Show History")

        self.pushButton.clicked.connect(self.show_his)

        self.pushButton = QPushButton("Exit", self)
        self.pushButton.move(550, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Close Window")

        self.pushButton.clicked.connect(self.returning)

    def del_rec(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            os.remove('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt')
            self.textans.clear()
        else:    
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)

    def show_his(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.hopn = open("HistoryMultiply3.txt",'r')
            text = self.hopn.read()
            self.textans.setText(text)
            self.hopn.close()
        else:
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)
    def returning(self):
        self.close()

class WindowMultiply4x4(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("Multiplication", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(500,50)
        self.label.move(430, 10)
       
        self.history = open("HistoryMultiply4.txt", 'w')
        self.history.write("History\n")
        self.history.close()

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(50, 80)
        self.textbox1.resize(100,30)
    
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(150, 80)
        self.textbox2.resize(100,30)
        

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(250, 80)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(350,80)
        self.textbox4.resize(100,30)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(50, 110)
        self.textbox5.resize(100,30)

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(150, 110)
        self.textbox6.resize(100,30)

        self.textbox7 = QLineEdit(self)
        self.textbox7.move(250, 110)
        self.textbox7.resize(100,30)

        self.textbox8 = QLineEdit(self)
        self.textbox8.move(350, 110)
        self.textbox8.resize(100,30)

        self.textbox9 = QLineEdit(self)
        self.textbox9.move(50, 140)
        self.textbox9.resize(100,30)

        self.textbox10 = QLineEdit(self)
        self.textbox10.move(150, 140)
        self.textbox10.resize(100,30)

        self.textbox11 = QLineEdit(self)
        self.textbox11.move(250, 140)
        self.textbox11.resize(100,30)

        self.textbox12 = QLineEdit(self)
        self.textbox12.move(350, 140)
        self.textbox12.resize(100,30)

        self.textbox13 = QLineEdit(self)
        self.textbox13.move(50, 170)
        self.textbox13.resize(100,30)

        self.textbox14 = QLineEdit(self)
        self.textbox14.move(150, 170)
        self.textbox14.resize(100,30)

        self.textbox15 = QLineEdit(self)
        self.textbox15.move(250, 170)
        self.textbox15.resize(100,30)

        self.textbox16 = QLineEdit(self)
        self.textbox16.move(350, 170)
        self.textbox16.resize(100,30)

        self.textbox1a = QLineEdit(self)
        self.textbox1a.move(580, 80)
        self.textbox1a.resize(100,30)
    
        self.textbox2a = QLineEdit(self)
        self.textbox2a.move(680, 80)
        self.textbox2a.resize(100,30)
        

        self.textbox3a = QLineEdit(self)
        self.textbox3a.move(780, 80)
        self.textbox3a.resize(100,30)

        self.textbox4a = QLineEdit(self)
        self.textbox4a.move(880,80)
        self.textbox4a.resize(100,30)

        self.textbox5a = QLineEdit(self)
        self.textbox5a.move(580, 110)
        self.textbox5a.resize(100,30)

        self.textbox6a = QLineEdit(self)
        self.textbox6a.move(680, 110)
        self.textbox6a.resize(100,30)

        self.textbox7a = QLineEdit(self)
        self.textbox7a.move(780, 110)
        self.textbox7a.resize(100,30)

        self.textbox8a = QLineEdit(self)
        self.textbox8a.move(880, 110)
        self.textbox8a.resize(100,30)

        self.textbox9a = QLineEdit(self)
        self.textbox9a.move(580, 140)
        self.textbox9a.resize(100,30)

        self.textbox10a = QLineEdit(self)
        self.textbox10a.move(680, 140)
        self.textbox10a.resize(100,30)

        self.textbox11a = QLineEdit(self)
        self.textbox11a.move(780, 140)
        self.textbox11a.resize(100,30)

        self.textbox12a = QLineEdit(self)
        self.textbox12a.move(880, 140)
        self.textbox12a.resize(100,30)

        self.textbox13a = QLineEdit(self)
        self.textbox13a.move(580, 170)
        self.textbox13a.resize(100,30)

        self.textbox14a = QLineEdit(self)
        self.textbox14a.move(680, 170)
        self.textbox14a.resize(100,30)

        self.textbox15a = QLineEdit(self)
        self.textbox15a.move(780, 170)
        self.textbox15a.resize(100,30)

        self.textbox16a = QLineEdit(self)
        self.textbox16a.move(880, 170)
        self.textbox16a.resize(100,30)

        self.det1 = QLineEdit(self)
        self.det1.setText("")
        self.det1.move(580, 300)
        self.det1.resize(100, 30)

        self.det2 = QLineEdit(self)
        self.det2.setText("")
        self.det2.move(680, 300)
        self.det2.resize(100, 30)

        self.det3 = QLineEdit(self)
        self.det3.setText("")
        self.det3.move(780, 300)
        self.det3.resize(100, 30)

        self.det4 = QLineEdit(self)
        self.det4.setText("")
        self.det4.move(880, 300)
        self.det4.resize(100, 30)

        self.det5 = QLineEdit(self)
        self.det5.setText("")
        self.det5.move(580, 330)
        self.det5.resize(100, 30)

        self.det6 = QLineEdit(self)
        self.det6.setText("")
        self.det6.move(680, 330)
        self.det6.resize(100, 30)

        self.det7 = QLineEdit(self)
        self.det7.setText("")
        self.det7.move(780, 330)
        self.det7.resize(100, 30)

        self.det8 = QLineEdit(self)
        self.det8.setText("")
        self.det8.move(880, 330)
        self.det8.resize(100, 30)

        self.det9 = QLineEdit(self)
        self.det9.setText("")
        self.det9.move(580, 360)
        self.det9.resize(100, 30)

        self.det10 = QLineEdit(self)
        self.det10.setText("")
        self.det10.move(680, 360)
        self.det10.resize(100, 30)

        self.det11 = QLineEdit(self)
        self.det11.setText("")
        self.det11.move(780, 360)
        self.det11.resize(100, 30)

        self.det12 = QLineEdit(self)
        self.det12.setText("")
        self.det12.move(880, 360)
        self.det12.resize(100, 30)

        self.det13 = QLineEdit(self)
        self.det13.setText("")
        self.det13.move(580, 390)
        self.det13.resize(100, 30)

        self.det14 = QLineEdit(self)
        self.det14.setText("")
        self.det14.move(680, 390)
        self.det14.resize(100, 30)

        self.det15 = QLineEdit(self)
        self.det15.setText("")
        self.det15.move(780, 390)
        self.det15.resize(100, 30)

        self.det16 = QLineEdit(self)
        self.det16.setText("")
        self.det16.move(880, 390)
        self.det16.resize(100, 30)

        self.text = QLabel("<h3>Answer: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(580, 275)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix A: <h3>", self)
        self.text.setFont(QFont('Times',10 , QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(50, 55)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Matrix B: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(580, 55)
        self.text.resize(150, 30)

        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Submit input")
        self.button.move(50,360)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Clear all ")
        self.button.move(200,360)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(350,360)
        self.button.clicked.connect(self.back) 

        self.button = QPushButton('History', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Show History")
        self.button.move(200,390)
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.button.clicked.connect(self.historycc)
        else:
            QMessageBox.warning(self, "Does not exist", "No existing history", QMessageBox.Ok, QMessageBox.Ok)


        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(800,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()
    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
        self.textbox6.setText("")
        self.textbox7.setText("")
        self.textbox8.setText("")
        self.textbox9.setText("")
        self.textbox10.setText("")
        self.textbox11.setText("")
        self.textbox12.setText("")
        self.textbox13.setText("")
        self.textbox14.setText("")
        self.textbox15.setText("")
        self.textbox16.setText("")
    
        self.textbox1a.setText("")
        self.textbox2a.setText("")
        self.textbox3a.setText("")
        self.textbox4a.setText("")
        self.textbox5a.setText("")
        self.textbox6a.setText("")
        self.textbox7a.setText("")
        self.textbox8a.setText("")
        self.textbox9a.setText("")
        self.textbox10a.setText("")
        self.textbox11a.setText("")
        self.textbox12a.setText("")
        self.textbox13a.setText("")
        self.textbox14a.setText("")
        self.textbox15a.setText("")
        self.textbox16a.setText("")

        self.det1.setText("")
        self.det2.setText("")
        self.det3.setText("")
        self.det4.setText("")
        self.det5.setText("")
        self.det6.setText("")
        self.det7.setText("")
        self.det8.setText("")
        self.det9.setText("")
        self.det10.setText("")
        self.det11.setText("")
        self.det12.setText("")
        self.det13.setText("")
        self.det14.setText("")
        self.det15.setText("")
        self.det16.setText("")


        

    def data(self):
       if self.textbox1.text() != "" and self.textbox2.text() !=  "" and self.textbox3.text() != "" and self.textbox4.text() != "" and self.textbox5.text() != "" and self.textbox6.text() != ""and self.textbox7.text() != "" and self.textbox8.text() != ""and  self.textbox9.text() != "" and self.textbox10.text() != "" and self.textbox11.text() != "" and self.textbox12.text() != "" and self.textbox13.text() != "" and self.textbox14.text() != "" and self.textbox15.text() != "" and self.textbox16.text() != "":
            a = int(self.textbox1.text())
            b = int(self.textbox2.text())
            c = int(self.textbox3.text())
            d = int(self.textbox4.text())
            e = int(self.textbox5.text())
            f = int(self.textbox6.text())
            g = int(self.textbox7.text())
            h = int(self.textbox8.text())
            i = int(self.textbox9.text())
            j = int(self.textbox10.text())
            k = int(self.textbox11.text())
            l = int(self.textbox12.text())
            m = int(self.textbox13.text())
            n = int(self.textbox14.text())
            o = int(self.textbox15.text())
            p = int(self.textbox16.text())
            

            aa = int(self.textbox1a.text())
            bb = int(self.textbox2a.text())
            cc = int(self.textbox3a.text())
            dd = int(self.textbox4a.text())
            ee = int(self.textbox5a.text())
            ff = int(self.textbox6a.text())
            gg = int(self.textbox7a.text())
            hh = int(self.textbox8a.text())
            ii = int(self.textbox9a.text())
            jj = int(self.textbox10a.text())
            kk = int(self.textbox11a.text())
            ll = int(self.textbox12a.text())
            mm = int(self.textbox13a.text())
            nn = int(self.textbox14a.text())
            oo = int(self.textbox15a.text())
            pp = int(self.textbox16a.text())
            self.matrix_computation(a, b, c, d, e, f, g, h, i, j,k,l,m,n,o,p,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp)
    
    def back(self):
        WindowMultiply4x4.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = windowMULTIPLY()
        self.mnwndw.show()
    
    def historycc(self):
        self.open = HisM4()
        self.open.show()

    def matrix_computation(self,a, b, c, d, e, f, g, h, i, j,k,l,m,n,o,p,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp):
        A = ((a*aa)+(b*ee)+(c*ii)+(d*mm))
        B = ((a*bb)+(b*ff)+(c*jj)+(d*nn))
        C = ((a*cc)+(b*gg)+(c*kk)+(d*oo))
        D = ((a*dd)+(b*hh)+(c*ll)+(d*pp))
        E = ((e*aa)+(f*ee)+(g*ii)+(h*mm))
        F = ((e*bb)+(f*ff)+(g*jj)+(h*nn))
        G = ((e*cc)+(f*gg)+(g*kk)+(h*oo))
        H = ((e*dd)+(f*hh)+(g*ll)+(h*pp))
        I = ((i*aa)+(j*ee)+(k*ii)+(l*mm))
        J = ((i*bb)+(j*ff)+(k*jj)+(l*nn))
        K = ((i*cc)+(j*gg)+(k*kk)+(l*oo))
        L = ((i*dd)+(j*hh)+(k*ll)+(l*pp))
        M = ((m*aa)+(n*ee)+(o*ii)+(p*mm))
        N = ((m*bb)+(n*ff)+(o*jj)+(p*nn))
        O = ((m*cc)+(n*gg)+(o*kk)+(p*oo))
        P = ((m*dd)+(n*hh)+(o*ll)+(p*pp))

        Determinate1 = A
        Determinate2 = B
        Determinate3 = C
        Determinate4 = D
        Determinate5 = E
        Determinate6 = F
        Determinate7 = G
        Determinate8 = H
        Determinate9 = I
        Determinate10 = J
        Determinate11 = K
        Determinate12 = L
        Determinate13 = M
        Determinate14 = N
        Determinate15 = O
        Determinate16 = P
        

        self.det1.setText(f"{Determinate1}")
        self.det2.setText(f"{Determinate2}")
        self.det3.setText(f"{Determinate3}")
        self.det4.setText(f"{Determinate4}")
        self.det5.setText(f"{Determinate5}")
        self.det6.setText(f"{Determinate6}")
        self.det7.setText(f"{Determinate7}")
        self.det8.setText(f"{Determinate8}")
        self.det9.setText(f"{Determinate9}")
        self.det10.setText(f"{Determinate10}")
        self.det11.setText(f"{Determinate11}")
        self.det12.setText(f"{Determinate12}")
        self.det13.setText(f"{Determinate13}")
        self.det14.setText(f"{Determinate14}")
        self.det15.setText(f"{Determinate15}")
        self.det16.setText(f"{Determinate16}")
        self.historia = open("HistoryMultiply4.txt", 'a')
        self.historia.write("Inputs\n" + str(a)+"\n")
        self.historia.write(str(b)+"\n")
        self.historia.write(str(c)+"\n")
        self.historia.write(str(d)+"\n")
        self.historia.write(str(e)+"\n")
        self.historia.write(str(f)+"\n")
        self.historia.write(str(g)+"\n")
        self.historia.write(str(h)+"\n")
        self.historia.write(str(i)+"\n")
        self.historia.write(str(j)+"\n")
        self.historia.write(str(k)+"\n")
        self.historia.write(str(l)+"\n")
        self.historia.write(str(m)+"\n")
        self.historia.write(str(n)+"\n")
        self.historia.write(str(o)+"\n")
        self.historia.write(str(p)+"\n")
            
        self.historia.write(str(aa)+"\n")
        self.historia.write(str(bb)+"\n")
        self.historia.write(str(cc)+"\n")
        self.historia.write(str(dd)+"\n")
        self.historia.write(str(ee)+"\n")
        self.historia.write(str(ff)+"\n")
        self.historia.write(str(gg)+"\n")
        self.historia.write(str(hh)+"\n")
        self.historia.write(str(ii)+"\n")
        self.historia.write(str(jj)+"\n")
        self.historia.write(str(kk)+"\n")
        self.historia.write(str(ll)+"\n")
        self.historia.write(str(mm)+"\n")
        self.historia.write(str(nn)+"\n")
        self.historia.write(str(oo)+"\n")
        self.historia.write(str(pp)+"\n")
        self.historia.write("(1,1) is " + str(Determinate1)+"\n")
        self.historia.write("(1,2) is " + str(Determinate2) + "\n")
        self.historia.write("(1,3) is " + str(Determinate3)+"\n")
        self.historia.write("(1,4) is " + str(Determinate4)+"\n")
        self.historia.write("(2,1) is " + str(Determinate5)+"\n")
        self.historia.write("(2,2) is " + str(Determinate6)+"\n")
        self.historia.write("(2,3) is " + str(Determinate7)+"\n")
        self.historia.write("(2,4) is " + str(Determinate8)+"\n")
        self.historia.write("(3,1) is " + str(Determinate9)+"\n")
        self.historia.write("(3,2) is " + str(Determinate10)+"\n")
        self.historia.write("(3,3) is " + str(Determinate11) + "\n")
        self.historia.write("(3,4) is " + str(Determinate12)+"\n")
        self.historia.write("(4,1) is " + str(Determinate13)+"\n")
        self.historia.write("(4,2) is " + str(Determinate14)+"\n")
        self.historia.write("(4,3) is " + str(Determinate15)+"\n")
        self.historia.write("(4,4) is " + str(Determinate16)+"\n")
        self.historia.close()

class HisM4(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "4x4 Multiplication History"
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.history = open("HistoryMultiply4.txt", 'r')
            self.history.read()
            self.history.close()
        else:
            QMessageBox.warning(self, "Error", "History does not exists!", QMessageBox.Ok, QMessageBox.Ok)

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
        self.setWindowIcon(QIcon('custom.ico'))
        self.textans = QTextEdit(self)
        self.textans.setText("")
        self.textans.resize(800, 450)

        self.pushButton = QPushButton("Clear", self)
        self.pushButton.move(150, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Clear History")

        self.pushButton.clicked.connect(self.del_rec)

        self.pushButton = QPushButton("Show", self)
        self.pushButton.move(350, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Show History")

        self.pushButton.clicked.connect(self.show_his)

        self.pushButton = QPushButton("Exit", self)
        self.pushButton.move(550, 470)
        self.pushButton.setStyleSheet("background-color: #d67d00 ; color : white  ")
        self.pushButton.setFont(QFont('Times', 13, QFont.Bold ))
        self.pushButton.setToolTip("Close Window")

        self.pushButton.clicked.connect(self.returning)

    def del_rec(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            os.remove('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt')
            self.textans.clear()
        else:    
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)

    def show_his(self):
        if os.path.exists('C:/Users/RODAS/Desktop/finalproject/Determinant History.txt'):
            self.hopn = open("HistoryMultiplyp4.txt",'r')
            text = self.hopn.read()
            self.textans.setText(text)
            self.hopn.close()
        else:
            QMessageBox.warning(self, "No File", "History does not exist", QMessageBox.Ok, QMessageBox.Ok)
    def returning(self):
        self.close()

class windowMULTIPLY(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Determinant Calculator"
        
        self.pushButton = QPushButton("2 X 2", self)
        self.pushButton.move(100, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt ; }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.window2multiply) 

        self.pushButton = QPushButton("3 X 3", self)
        self.pushButton.move(300, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.window3multiply)

        self.pushButton = QPushButton("4 X 4", self)
        self.pushButton.move(500, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.window4multiply)             
        

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight : bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(300,450)
        self.button.clicked.connect(self.back)
        

       

        self.main_window()

    def main_window(self):
       
        self.label = QLabel("<h3>Matrix Calculator<h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: white;}')
        
        self.label.resize(500,50)
        self.label.move(210, 50) 
        self.setWindowTitle(self.title)
        self.setGeometry(350, 100, 700, 500)
     
        #background
        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(800,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        self.show()

    def back(self):
        windowMULTIPLY.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = MainWindow()
        self.mnwndw.show()
    


    def window2multiply(self):
        self.w = WindowMultiply2x2()
        self.w.show()
        MainWindow.close(self)
    
    def window3multiply(self):
        self.w = WindowMultiply3x3()
        self.w.show()
        MainWindow.close(self)

    def window4multiply(self):
        self.w = WindowMultiply4x4()
        self.w.show()
        MainWindow.close(self)
    
    
   


class WindowInv2x2(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("Inverse", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(350,50)
        self.label.move(330, 10)
       

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 800, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(80, 80)
        self.textbox1.resize(100,30)
        

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(180, 80)
        self.textbox2.resize(100,30)

        

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(80, 110)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(180, 110)
        self.textbox4.resize(100,30)

       

       
        self.textbox1a = QLineEdit(self)
        self.textbox1a.move(480, 80)
        self.textbox1a.resize(100,30)
        

        self.textbox2a = QLineEdit(self)
        self.textbox2a.move(580, 80)
        self.textbox2a.resize(100,30)

        self.textbox3a = QLineEdit(self)
        self.textbox3a.move(480, 110)
        self.textbox3a.resize(100,30)

        self.textbox4a = QLineEdit(self)
        self.textbox4a.move(580, 110)
        self.textbox4a.resize(100,30)

       

        self.text = QLabel("<h3>Matrix A: <h3>", self)
        self.text.setFont(QFont('Times',10 , QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(80, 60)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Inverse Matrix : <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(480, 60)
        self.text.resize(150, 30)



        
        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Submit input")
        self.button.move(50,350)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Clear all ")
        self.button.move(350,350)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(650,350)
        self.button.clicked.connect(self.back) 

        

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(800,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()
    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
       
        self.textbox1a.setText("")
        self.textbox2a.setText("")
        self.textbox3a.setText("")
        self.textbox4a.setText("")
        
        

        

    def data(self):
        Submitted = QMessageBox.information(self, "Input Submitted", "Your Input Has Been Verified", QMessageBox.Ok, QMessageBox.Ok)
        x = np.array([[self.textbox1.text(),self.textbox2.text()],
                        [self.textbox3.text(),self.textbox4.text()]]),
                       
        z = x.astype(int)
        Answer = np.linalg.inv(z)
        Answer = np.around(Answer,decimals=2)
        print(Answer)

        self.textbox1a.setText(f"{Answer[0][0]}")
        self.textbox2a.setText(f"{Answer[0][1]}")
        self.textbox3a.setText(f"{Answer[1][0]}")
        self.textbox4a.setText(f"{Answer[1][1]}")
        

    def back(self):
        WindowInv2x2.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = WindowINV()
        self.mnwndw.show()

    
        


class WindowInv3x3(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("<h3> Inverse  <h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(430,50)
        self.label.move(360, 10)
       

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 800, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(80, 80)
        self.textbox1.resize(100,30)
        

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(180, 80)
        self.textbox2.resize(100,30)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(280,80)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(80, 110)
        self.textbox4.resize(100,30)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(180, 110)
        self.textbox5.resize(100,30)

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(280, 110)
        self.textbox6.resize(100,30)

        self.textbox7 = QLineEdit(self)
        self.textbox7.move(80, 140)
        self.textbox7.resize(100,30)

        self.textbox8 = QLineEdit(self)
        self.textbox8.move(180, 140)
        self.textbox8.resize(100,30)

        self.textbox9 = QLineEdit(self)
        self.textbox9.move(280, 140)
        self.textbox9.resize(100,30)

        self.textbox1a = QLineEdit(self)
        self.textbox1a.move(480, 80)
        self.textbox1a.resize(100,30)
        

        self.textbox2a = QLineEdit(self)
        self.textbox2a.move(580, 80)
        self.textbox2a.resize(100,30)

        self.textbox3a = QLineEdit(self)
        self.textbox3a.move(680,80)
        self.textbox3a.resize(100,30)

        self.textbox4a = QLineEdit(self)
        self.textbox4a.move(480, 110)
        self.textbox4a.resize(100,30)

        self.textbox5a = QLineEdit(self)
        self.textbox5a.move(580, 110)
        self.textbox5a.resize(100,30)

        self.textbox6a = QLineEdit(self)
        self.textbox6a.move(680, 110)
        self.textbox6a.resize(100,30)

        self.textbox7a = QLineEdit(self)
        self.textbox7a.move(480, 140)
        self.textbox7a.resize(100,30)

        self.textbox8a = QLineEdit(self)
        self.textbox8a.move(580, 140)
        self.textbox8a.resize(100,30)

        self.textbox9a = QLineEdit(self)
        self.textbox9a.move(680, 140)
        self.textbox9a.resize(100,30)

        

        
        self.text = QLabel("<h3>Matrix A: <h3>", self)
        self.text.setFont(QFont('Times',10 , QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(80, 60)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Inverse Matrix: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(480, 60)
        self.text.resize(150, 30)





      
        
        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Submit input")
        self.button.move(50,350)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Clear all ")
        self.button.move(350,350)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(650,350)
        self.button.clicked.connect(self.back) 

        

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(800,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()
    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
        self.textbox6.setText("")
        self.textbox7.setText("")
        self.textbox8.setText("")
        self.textbox9.setText("")
        self.textbox1a.setText("")
        self.textbox2a.setText("")
        self.textbox3a.setText("")
        self.textbox4a.setText("")
        self.textbox5a.setText("")
        self.textbox6a.setText("")
        self.textbox7a.setText("")
        self.textbox8a.setText("")
        self.textbox9a.setText("")

      

        

    def data(self):
        Submitted = QMessageBox.information(self, "Input Submitted", "Your Input Has Been Verified", QMessageBox.Ok, QMessageBox.Ok)
        x = np.array([[self.textbox1.text(),self.textbox2.text(),self.textbox3.text()],
                        [self.textbox4.text(),self.textbox5.text(),self.textbox6.text()],
                        [self.textbox7.text(),self.textbox8.text(),self.textbox9.text()]])
        
        z = x.astype(int)
        Answer = np.linalg.inv(z)
        Answer = np.around(Answer,decimals=2)
        print(Answer)

       
        self.textbox1a.setText(f"{Answer[0][0]}")
        self.textbox2a.setText(f"{Answer[0][1]}")
        self.textbox3a.setText(f"{Answer[0][2]}")
        self.textbox4a.setText(f"{Answer[1][0]}")
        self.textbox5a.setText(f"{Answer[1][1]}")
        self.textbox6a.setText(f"{Answer[1][2]}")
        self.textbox7a.setText(f"{Answer[2][0]}")
        self.textbox8a.setText(f"{Answer[2][1]}")
        self.textbox9a.setText(f"{Answer[2][2]}")

    
    def back(self):
        WindowInv3x3.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = WindowINV()
        self.mnwndw.show()

    

class WindowInv4x4(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.label = QLabel("Inverse", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: #dedede;}')
        self.label.resize(500,50)
        self.label.move(430, 10)
       

        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(100, 50, 1000, 500)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(50, 80)
        self.textbox1.resize(100,30)
    
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(150, 80)
        self.textbox2.resize(100,30)
        

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(250, 80)
        self.textbox3.resize(100,30)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(350,80)
        self.textbox4.resize(100,30)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(50, 110)
        self.textbox5.resize(100,30)

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(150, 110)
        self.textbox6.resize(100,30)

        self.textbox7 = QLineEdit(self)
        self.textbox7.move(250, 110)
        self.textbox7.resize(100,30)

        self.textbox8 = QLineEdit(self)
        self.textbox8.move(350, 110)
        self.textbox8.resize(100,30)

        self.textbox9 = QLineEdit(self)
        self.textbox9.move(50, 140)
        self.textbox9.resize(100,30)

        self.textbox10 = QLineEdit(self)
        self.textbox10.move(150, 140)
        self.textbox10.resize(100,30)

        self.textbox11 = QLineEdit(self)
        self.textbox11.move(250, 140)
        self.textbox11.resize(100,30)

        self.textbox12 = QLineEdit(self)
        self.textbox12.move(350, 140)
        self.textbox12.resize(100,30)

        self.textbox13 = QLineEdit(self)
        self.textbox13.move(50, 170)
        self.textbox13.resize(100,30)

        self.textbox14 = QLineEdit(self)
        self.textbox14.move(150, 170)
        self.textbox14.resize(100,30)

        self.textbox15 = QLineEdit(self)
        self.textbox15.move(250, 170)
        self.textbox15.resize(100,30)

        self.textbox16 = QLineEdit(self)
        self.textbox16.move(350, 170)
        self.textbox16.resize(100,30)

        self.textbox1a = QLineEdit(self)
        self.textbox1a.move(580, 80)
        self.textbox1a.resize(100,30)
    
        self.textbox2a = QLineEdit(self)
        self.textbox2a.move(680, 80)
        self.textbox2a.resize(100,30)
        

        self.textbox3a = QLineEdit(self)
        self.textbox3a.move(780, 80)
        self.textbox3a.resize(100,30)

        self.textbox4a = QLineEdit(self)
        self.textbox4a.move(880,80)
        self.textbox4a.resize(100,30)

        self.textbox5a = QLineEdit(self)
        self.textbox5a.move(580, 110)
        self.textbox5a.resize(100,30)

        self.textbox6a = QLineEdit(self)
        self.textbox6a.move(680, 110)
        self.textbox6a.resize(100,30)

        self.textbox7a = QLineEdit(self)
        self.textbox7a.move(780, 110)
        self.textbox7a.resize(100,30)

        self.textbox8a = QLineEdit(self)
        self.textbox8a.move(880, 110)
        self.textbox8a.resize(100,30)

        self.textbox9a = QLineEdit(self)
        self.textbox9a.move(580, 140)
        self.textbox9a.resize(100,30)

        self.textbox10a = QLineEdit(self)
        self.textbox10a.move(680, 140)
        self.textbox10a.resize(100,30)

        self.textbox11a = QLineEdit(self)
        self.textbox11a.move(780, 140)
        self.textbox11a.resize(100,30)

        self.textbox12a = QLineEdit(self)
        self.textbox12a.move(880, 140)
        self.textbox12a.resize(100,30)

        self.textbox13a = QLineEdit(self)
        self.textbox13a.move(580, 170)
        self.textbox13a.resize(100,30)

        self.textbox14a = QLineEdit(self)
        self.textbox14a.move(680, 170)
        self.textbox14a.resize(100,30)

        self.textbox15a = QLineEdit(self)
        self.textbox15a.move(780, 170)
        self.textbox15a.resize(100,30)

        self.textbox16a = QLineEdit(self)
        self.textbox16a.move(880, 170)
        self.textbox16a.resize(100,30)

       

        

        self.text = QLabel("<h3>Matrix A: <h3>", self)
        self.text.setFont(QFont('Times',10 , QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(50, 55)
        self.text.resize(150, 30)

        self.text = QLabel("<h3>Inverse Matrix: <h3>", self)
        self.text.setFont(QFont('Times', 10, QFont.Bold ))
        self.text.setStyleSheet('QLabel {color:#dedede;}')
        self.text.move(580, 55)
        self.text.resize(150, 30)





      
        
        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Submit input")
        self.button.move(50,360)
        self.button.clicked.connect(self.data)

        self.button = QPushButton('Clear', self)
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")
        self.button.setToolTip("Clear all ")
        self.button.move(450,360)
        self.button.clicked.connect(self.clear)

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold}")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(850,360)
        self.button.clicked.connect(self.back) 

        

        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(680,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.show()
    @pyqtSlot()
    
    def clear(self):
        buttonReply = QMessageBox.information(self, "Input Cleared", "Your Input Has Been Cleared", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
        self.textbox6.setText("")
        self.textbox7.setText("")
        self.textbox8.setText("")
        self.textbox9.setText("")
        self.textbox10.setText("")
        self.textbox11.setText("")
        self.textbox12.setText("")
        self.textbox13.setText("")
        self.textbox14.setText("")
        self.textbox15.setText("")
        self.textbox16.setText("")
    
        self.textbox1a.setText("")
        self.textbox2a.setText("")
        self.textbox3a.setText("")
        self.textbox4a.setText("")
        self.textbox5a.setText("")
        self.textbox6a.setText("")
        self.textbox7a.setText("")
        self.textbox8a.setText("")
        self.textbox9a.setText("")
        self.textbox10a.setText("")
        self.textbox11a.setText("")
        self.textbox12a.setText("")
        self.textbox13a.setText("")
        self.textbox14a.setText("")
        self.textbox15a.setText("")
        self.textbox16a.setText("")

        

    def data(self):
        Submitted = QMessageBox.information(self, "Input Submitted", "Your Input Has Been Verified", QMessageBox.Ok, QMessageBox.Ok)
        x = np.array([[self.textbox1.text(),self.textbox2.text(),self.textbox3.text(),self.textbox4.text()],
                        [self.textbox5.text(),self.textbox6.text(),self.textbox7.text(),self.textbox8.text()],
                        [self.textbox9.text(),self.textbox10.setText(),self.textbox11.setText(),self.textbox12.setText()],
                        [self.textbox13.setText(),self.textbox14.setText(),self.textbox15.setText(),self.textbox16.setText() ]])
        
        z = x.astype(int)
        Answer = np.linalg.inv(z)
        Answer = np.around(Answer,decimals=2)
        print(Answer)

        self.textbox1a.setText(f"{Answer[0][0]}")
        self.textbox2a.setText(f"{Answer[0][1]}")
        self.textbox3a.setText(f"{Answer[0][2]}")
        self.textbox4a.setText(f"{Answer[0][3]}")
        self.textbox5a.setText(f"{Answer[1][0]}")
        self.textbox6a.setText(f"{Answer[1][1]}")
        self.textbox7a.setText(f"{Answer[1][2]}")
        self.textbox8a.setText(f"{Answer[1][3]}")
        self.textbox9a.setText(f"{Answer[2][0]}")
        self.textbox10.setText(f"{Answer[2][1]}")
        self.textbox11.setText(f"{Answer[2][2]}")
        self.textbox12.setText(f"{Answer[2][3]}")
        self.textbox13.setText(f"{Answer[3][0]}")
        self.textbox14.setText(f"{Answer[3][1]}")
        self.textbox15.setText(f"{Answer[3][2]}")
        self.textbox16.setText(f"{Answer[3][3]}")
       

    
    def back(self):
        WindowInv4x4.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = WindowINV()
        self.mnwndw.show()

    

class WindowINV(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Determinant Calculator"
        
        self.pushButton = QPushButton("2 X 2", self)
        self.pushButton.move(100, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt ; }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.window2inv) 

        self.pushButton = QPushButton("3 X 3", self)
        self.pushButton.move(300, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.window3inv)

        self.pushButton = QPushButton("4 X 4", self)
        self.pushButton.move(500, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.window4inv)             
        

        self.button = QPushButton('Back', self)  
        self.button.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight : bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt}")   
        self.button.setToolTip("Go Back")
        self.button.move(300,450)
        self.button.clicked.connect(self.back)
        

       

        self.main_window()

    def main_window(self):
       
        self.label = QLabel("<h3>Matrix Calculator<h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: white;}')
        
        self.label.resize(500,50)
        self.label.move(210, 50) 
        self.setWindowTitle(self.title)
        self.setGeometry(350, 100, 700, 500)
     
        #background
        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(680,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        self.show()

    def back(self):
        WindowINV.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = MainWindow()
        self.mnwndw.show()

    def window2inv(self):
        self.w = WindowInv2x2()
        self.w.show()
        MainWindow.close(self)
    
    def window3inv(self):
        self.w = WindowInv3x3()
        self.w.show()
        MainWindow.close(self)

    def window4inv(self):
        self.w = WindowInv4x4()
        self.w.show()
        MainWindow.close(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Matrix Calculator"
        self.setGeometry(420, 100, 500, 500)

        self.pushButton = QPushButton("Multiplication", self)
        self.pushButton.move(50, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 10pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt ; }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.windowmultiply)
        
        self.pushButton = QPushButton("Addition", self)
        self.pushButton.move(550, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 10pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.windowadd)
        
        self.pushButton = QPushButton("Determinant", self)
        self.pushButton.move(175, 250)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 10pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.windowdet) 

        self.pushButton = QPushButton("Subtraction", self)
        self.pushButton.move(300, 200)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 10pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.windowsub)

        self.pushButton = QPushButton("Inverse", self)
        self.pushButton.move(425,250)
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 10pt; font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt }")
        self.pushButton.setToolTip("Start")
        self.pushButton.clicked.connect(self.windowinv)

        self.pushButton = QPushButton('Exit', self)
        self.pushButton.move(300,450)
        self.pushButton.setToolTip("Exit to the System")
        self.pushButton.setStyleSheet("QPushButton{background-color : #d67d00 ; color :white ; font: 13pt;font-weight: bold }")
        self.setStyleSheet(" QToolTip{ border: 1px solid black; background-color:white ; font: 8pt;}")
        self.pushButton.clicked.connect(QApplication.instance().quit)
        

        
        self.main_window()

    


    def main_window(self):
       
        self.label = QLabel("<h3>Matrix Calculator<h3>", self)
        self.label.setFont(QFont('Times', 20, QFont.Bold ))
        self.label.setStyleSheet('QLabel {color: white;}')
        
        self.label.resize(500,50)
        self.label.move(210, 50) 
        self.setWindowTitle(self.title)
        self.setGeometry(350, 100, 700, 500)
     
        #background
        oImage = QImage("technological-circuit-background_115579-1077.jpg")
        sImage = oImage.scaled(QSize(680,500))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        self.show()
    

    def window2(self):
        self.w = Window2()
        self.w.show()
        MainWindow.close(self)


    def window3(self):
        self.w = Window3()
        self.w.show()
        MainWindow.close(self)

    def window4(self):
        self.w = Window4()
        self.w.show()
        MainWindow.close(self)
    
    def windowmultiply(self):
        self.w = windowMULTIPLY()
        self.w.show()
        MainWindow.close(self)
    
    def windowdet(self):
        self.w = Window()
        self.w.show()
        MainWindow.close(self)

    def windowadd(self):
        self.w = WindowADD()
        self.w.show()
        MainWindow.close(self)
    
    def windowinv(self):
        self.w = WindowINV()
        self.w.show()
        MainWindow.close(self)

    def windowsub(self):
        self.w = WindowSUB()
        self.w.show()
        MainWindow.close(self)

    def windo6(self):
        self.w = Window6(self)
        self.w.show()
        MainWindow.close(self)


   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())