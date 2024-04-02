
import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def num (x):
    global number
    old_number = window.textbox.text()
    number = old_number + x
    window.textbox.setText(number)

def point () :
    global number
    number = number + "."
    window.textbox.setText (number)

def minus () :
    global number
    number = "-" + number
    window.textbox.setText (number)

def ac () :
    global number 
    number = ""
    window.textbox.setText (number)

def sum () :
    global number
    global operation
    global first
    first = float (number)
    operation = "+"
    number = ""
    window.textbox.setText (number)

def sub () :
    global number
    global operation
    global first
    first = float (number)
    operation = "-"
    number = ""
    window.textbox.setText (number)

def multi () :
    global number 
    global operation
    global first
    first = float (number)
    operation = "*"
    number = ""
    window.textbox.setText (number)

def divid () : 
    global number
    global operation
    global first
    first = float (number)
    operation = "/"
    number = ""
    window.textbox.setText (number)

def sqrt () : 
    global number
    global operation
    global first
    first = float (number)
    operation = "sqrt"
    text = f"sqrt ({first})"
    window.textbox.setText (text)

def percent () :
    global number
    first = float (number)
    result = first / 100
    window.textbox.setText (str(result))
    number = ""

def log () : 
    global number
    global operation
    global first
    first = float (number)
    operation = "log"
    text = f"log({number})"
    window.textbox.setText (text)

def sin () :
    global number
    global operation
    global first
    first = float (number)
    operation = "sin"
    text = f"sin({number})"
    window.textbox.setText (text)

def cos () : 
    global number
    global operation
    global first
    first = float (number)
    operation = "cos"
    text = f"cos({number})"
    window.textbox.setText (text)

def tan () : 
    global number
    global operation
    global first
    first = float (number)
    operation = "tan"
    text = f"tan({number})"
    window.textbox.setText (text)

def cot () : 
    global number
    global operation
    global first
    first = float (number)
    operation = "cot"
    text = f"cot({number})"
    window.textbox.setText (text)

def equal () :
    global number
    global first
    global operation

    if operation == "+" or operation == "-" or operation == "*" or operation == "/" :
        second = float ( number )

        if operation == "+" :
            result = first + second

        elif operation == "-" :
            result = first - second
        
        elif operation == "*" :
            result = first * second

        elif operation == "/" :
            if second == 0 :
                result = " Error!! "

            else :
                result = first / second
    
    else :
        if operation == "sqrt" :
            if first >= 0 :
                result = math.sqrt (first)
            
            else :
                result = " Error!! "

        elif operation == "log" :
            result = math.log10 (first)

        elif operation == "sin" : 
            rad = first * ( math.pi / 180 )
            result = math.sin (rad)      

        elif operation == "cos" :
            rad = first * ( math.pi / 180 )
            result = math.cos (rad)

        elif operation == "tan" : 
            rad = first * ( math.pi / 180 )
            result = math.tan (rad)

        elif operation == "cot" : 
            rad = first * ( math.pi / 180 )
            result = 1 / ( math.tan (rad) )
    
    window.textbox.setText (str(result))
    number = ""
    operation = ""
    first = ""

app = QApplication ([])
loader = QUiLoader ()
window = loader.load ("calculator.ui")
number = ""
operation = ""

window.btn_num_0.clicked.connect (partial(num,"0"))
window.btn_num_1.clicked.connect (partial(num,"1"))
window.btn_num_2.clicked.connect (partial(num,"2"))
window.btn_num_3.clicked.connect (partial(num,"3"))
window.btn_num_4.clicked.connect (partial(num,"4"))
window.btn_num_5.clicked.connect (partial(num,"5"))
window.btn_num_6.clicked.connect (partial(num,"6"))
window.btn_num_7.clicked.connect (partial(num,"7"))
window.btn_num_8.clicked.connect (partial(num,"8"))
window.btn_num_9.clicked.connect (partial(num,"9"))
window.point.clicked.connect (partial(num,"."))
window.minus.clicked.connect (minus)
window.equal.clicked.connect (equal)
window.sum.clicked.connect (sum)
window.sub.clicked.connect (sub)
window.multi.clicked.connect (multi)
window.divide.clicked.connect (divid)
window.sqrt.clicked.connect (sqrt)
window.percent.clicked.connect (percent)
window.log.clicked.connect (log)
window.sin.clicked.connect (sin)
window.cos.clicked.connect (cos)
window.tan.clicked.connect (tan)
window.cot.clicked.connect (cot)
window.ac.clicked.connect (ac)

window.show ()
app.exec ()