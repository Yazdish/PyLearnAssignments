import random
import sys
from functools import partial
from PySide6.QtWidgets import QApplication , QMainWindow , QMessageBox
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)
        self.ui.strong.setChecked (True)
        self.state = "strong"
        self.ui.strong.clicked.connect (partial (self.statement , "strong"))
        self.ui.extra.clicked.connect (partial (self.statement , "extra"))
        self.ui.superstrong.clicked.connect (partial (self.statement , "superstrong"))
        self.ui.about.clicked.connect (self.about)
        self.ui.generate.clicked.connect (self.generate)
        self.charecters = [ "!" , "@" , "#" , "$" , "%" , "^" , "&" , "*" , "?" ]
        self.lower_letters = [ "a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z" ]

    def generate(self):
        n = 0
        text = ""

        if self.state == "strong":
            while n < 8:
                list = []
                i = random.randint(0, 3)
                if i == 0:
                    number = random.randint(0, 9)
                    text += str(number)
                    list.append (0)
                    n += 1
                
                elif i == 1 :
                    index = random.randint (0 , len(self.charecters) - 1 )
                    text += self.charecters [index]
                    list.append (1)
                    n += 1

                elif i == 2  :
                    index = random.randint ( 0 , len(self.lower_letters) - 1 )
                    text += self.lower_letters [index].upper ()
                    list.append (2)
                    n += 1

                elif i == 3 :
                    index = random.randint ( 0 , len(self.lower_letters) - 1 )
                    text += self.lower_letters [index]
                    list.append (2)
                    n += 1

            self.ui.txtbox.setText (text)

            
        elif self.state == "extra" :
            while n < 12 :
                i = random.randint (0 , 3)
                if i == 0 :
                    number = random.randint (0 , 9)
                    text += str (number)
                    n += 1
                
                elif i == 1 :
                    index = random.randint (0 , len(self.charecters) - 1 )
                    text += self.charecters [index]
                    n += 1

                elif i == 2 :
                    index = random.randint ( 0 , len(self.lower_letters) - 1 )
                    text += self.lower_letters [index].upper ()
                    n += 1

                elif i == 3 :
                    index = random.randint ( 0 , len(self.lower_letters) - 1 )
                    text += self.lower_letters [index]
                    n += 1

            self.ui.txtbox.setText (text)

        elif self.state == "superstrong" :
            while n < 20 :
                i = random.randint (0 , 3)
                if i == 0 :
                    number = random.randint (0 , 9)
                    text += str (number)
                    n += 1
                
                elif i == 1 :
                    index = random.randint (0 , len(self.charecters) - 1 )
                    text += self.charecters [index]
                    n += 1

                elif i == 2 :
                    index = random.randint ( 0 , len(self.lower_letters) - 1 )
                    text += self.lower_letters [index].upper ()
                    n += 1

                elif i == 3 :
                    index = random.randint ( 0 , len(self.lower_letters) - 1 )
                    text += self.lower_letters [index]
                    n += 1

            self.ui.txtbox.setText (text)

    def statement ( self , mode) :
        self.state = mode

    def about (self):
        text = f"Strong Password :\n 8 characters long including numbers, special characters and uppercase letters\
\nExtra Strong Password :\n 12 characters long with multiple numbers, special characters and uppercase letters\nSuper Strong Password:\
\n 20 characters long with multiple numbers, special characters and uppercase letters"
        message = QMessageBox (WindowTitle = "about" , text = text)
        message.exec_ ()

app = QApplication ( sys.argv )
window = MainWindow ()
window.show ()
app.exec ()