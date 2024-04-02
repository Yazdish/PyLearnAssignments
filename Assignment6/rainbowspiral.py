import turtle
import time

turtle.bgcolor("black")

colors = ["red","purple","blue","green","yellow","orange"]
t = turtle.Pen(shape="turtle")
t.speed = 100
i=0
while i<360:
    for j in range(len(colors)):
        t.width(i/100 + 1)
        t.pencolor(colors[j])
        t.forward(i)
        t.left(59)
        i +=1


turtle.done()

#time.sleep(10)

