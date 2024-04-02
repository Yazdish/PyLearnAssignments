import turtle
import time
start_time = time.time()

pen = turtle.Turtle(shape="turtle")
num_sides = 3
side_length = 10    
for j in range(10):
    angle = 360.0 / num_sides
    pen.lt(angle/2)
   
    for i in range(num_sides):
        pen.forward(side_length)
        pen.left(angle)
    
    num_sides = num_sides + 1
    side_length = side_length + 10
    

    pen.penup()
    pen.fd(side_length)
    pen.pendown()
    
turtle.done()

end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time)