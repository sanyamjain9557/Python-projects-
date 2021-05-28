import turtle

while(True):
    pen=turtle.Turtle()
    turtle.bgcolor('black')

    pen.turtlesize(2)
    pen.speed(0)

    color=['white','green','blue','yellow','red','pink']


    for i in range(6):
        for j in color:
            pen.color(j)
            pen.circle(100)
            pen.left(10)

    pen.hideturtle()