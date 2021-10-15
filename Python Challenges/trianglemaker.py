import turtle

def triangle_draw (x,y,sz):
    turtle.speed(-5)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(3):
        turtle.forward(sz)
        turtle.left(120)

for y in range (-300,300,10):
    for x in range (-300,300,10):
        triangle_draw(x,y,10)
