import math
def answer(a,b,c):
    p=(b-((a**2)/3))
    q=((2*(a**3))/27-((a*b)/3)+c)
    Δ=(((q**2)/4)+((p**3)/27))
    if Δ>0:
        x=((((-q/2)+(math.sqrt(Δ)))**(1/3))+(((-q/2)-(math.sqrt(Δ)))**(1/3))-a/3)
        print("x=",x)
    elif Δ==0:
        x1=round(-2*((q/2)**(1/3))-a/3)
        x2=round(((q/2)**(1/3))-a/3)
        print("x1=",x1)
        print("x2=x3=",x2)
    elif Δ<0:
        x1=round((2/(math.sqrt(3)))*(math.sqrt(-p))*math.sin((1/3)*math.asin((3*q*math.sqrt(3))/(2*((math.sqrt(-p))**3))))-a/3)
        x2=round((-2/(math.sqrt(3)))*(math.sqrt(-p))*math.sin(((1/3)*math.asin((3*q*math.sqrt(3))/(2*((math.sqrt(-p))**3))))+(math.pi)/3)-a/3)  
        x3=round((2/(math.sqrt(3)))*(math.sqrt(-p))*math.cos(((1/3)*math.asin((3*q*math.sqrt(3))/(2*((math.sqrt(-p))**3))))+(math.pi)/6)-a/3)
        print("x1=",x1)
        print("x2=",x2) 
        print("x3=",x3)  

A=float(input("please enter a: "))
B=float(input("please enter b: "))
C=float(input("please enter c: "))

answer(A,B,C)