import turtle
pen = turtle.Turtle()
screen = turtle.Screen()
pen.speed(60)
pen.up()
pen.goto(-200,300)
pen.down()

pen.write("python",font=("Arial",100,"normal") )
pen.up()
pen.goto(-600,0)
pen.down()

def line():
    pen.down()
    for i in range(2):
        pen.begin_fill()
        pen.fd(50)
        pen.rt(90)
        pen.fd(20)
        pen.rt(90)
        pen.end_fill()
    pen.up()
    pen.fd(70)

def point():
    pen.up()
    pen.fd(10)
    pen.down()
    pen.begin_fill()
    pen.circle(-12)
    pen.end_fill()
    pen.up()
    pen.fd(30)

def space():
    pen.fd(40)


#line()
#point()
#space()

#p
point()
line()
line()
point()
space()

#y
line()
point()
line()
line()
space()

#t
line()
space()

#h
point()
point()
point()
point()
space()

#o
line()
line()
line()
space()

#n
line()
point()
space()

screen.mainloop()