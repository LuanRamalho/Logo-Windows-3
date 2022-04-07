import turtle
logo = turtle.Turtle()
logo.begin_fill()
logo.color("#00a4ef")
logo.penup()
logo.goto(-100, 100)
logo.pendown()

for i in range(4):
    logo.forward(200)
    logo.right(90)
logo.end_fill()

logo.color("white")
logo.penup()
logo.forward(100)
logo.pendown()

logo.right(90)
logo.width(10)
logo.forward(200)
logo.penup()
logo.goto(-100,0)
logo.pendown()
logo.right(-90)
logo.forward(200)

logo.color("#00a4ef")
logo.penup()
logo.goto(5,-160)
logo.write("Windows 11", move = False, align="center", font=("Arial", 24, "bold"))

logo.hideturtle()
turtle.done()












