import turtle
screen = turtle.Screen()
screen.getcanvas().winfo_toplevel().iconbitmap(r"C:\Users\shaya\Downloads\mars_97169.ico")
screen.title("terrforoming")
screen.bgcolor("black")

mars = turtle.Turtle()
mars.color("tomato")
mars.shape("circle")
mars.shapesize(10, 10)
mars.stamp()
mars.hideturtle()
mars.speed(10000)
mars.rt(180)
mars.fd(100)
mars.pensize(5)
mars.color("moccasin")
mars.setheading(-90)
mars.circle(100)
mars.stamp()
mars.shape("")
mars.shapesize(5, 50)
mars.penup()











screen.mainloop()