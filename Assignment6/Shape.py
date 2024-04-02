import turtle
p=turtle.Pen(shape="turtle")

j=20
h=10

for n in range(3,10):
    angle = ((n-2)*180)/n
    p.left(180-(angle/2))
 
    j=j+10
    h+=2
    for i in range(n):
        p.forward(j)
        p.left(180-angle)
    p.right(180-(angle/2))
    p.penup()
    p.forward(h)
    p.down()

turtle.done()