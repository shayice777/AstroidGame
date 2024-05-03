import threading
# זימון הספריות
import threading
import time
import turtle
#יצירת הכלים למשחק
pen = turtle.Turtle()
pen2 = turtle.Turtle()
snake = turtle.Turtle()
screen = turtle.Screen()
# הגדרת המסך
screen.bgcolor("black")
# הגדרת הנחש
snake.shape("circle")
snake.color("#3cb371")
snake.penup()
snake.speed(1000)

print("תפתחו את המסך בשביל לשחק")
# כותב הסופרים של הזמן+הנקודות
pen.penup()
pen.goto(-730,360)
pen.pendown()
pen.color("white")
pen.write( "time counter:", font=("OCR A Extended", 18, "normal"))
pen.hideturtle()
# סופר הזמן
def timer():
    gametime = 0
    pen2.color("white")
    pen2.penup()
    pen2.goto(-660,335)
    pen2.pendown()
    while True:
        time.sleep(1)
        pen2.clear()
        gametime += 1
        pen2.write(gametime, font=("OCR A Extended", 18, "normal"))
timerth = threading.Thread(target=timer)
timerth.start()

x = 0
y = 1

def right():
    snake.setheading(0)

def left():
    snake.setheading(180)

def up():
    snake.setheading(90)

def down():
    snake.setheading(-90)

turtle.listen()
def forwards():
    while 0 == x:
        turtle.onkey(right, "Right")
        turtle.onkey(left, "Left")
        turtle.onkey(up, "Up")
        turtle.onkey(down,"Down")
        snake.fd(y)

for_r = threading.Thread(target=forwards)
for_r.start()

screen.mainloop()