# זימון ספריות
import threading
import time
import turtle
import random
import math

# יצירת הכלים למשחק
screen = turtle.Screen()
turtle_player = turtle.Turtle()
writer = turtle.Turtle()
writer_game_over = turtle.Turtle()
write_timer = turtle.Turtle()
write_points = turtle.Turtle()
borders = turtle.Turtle()

# נקודות
point1 = turtle.Turtle()
point2 = turtle.Turtle()
point3 = turtle.Turtle()
point4 = turtle.Turtle()
point5 = turtle.Turtle()
point6 = turtle.Turtle()
point7 = turtle.Turtle()
point8 = turtle.Turtle()

# הגדרת המסך
screen.bgcolor("black")
screen.setup(1200, 720)

# ציור גבולות
borders.speed(100)
borders.hideturtle()
borders.color("#ff0f05")
borders.pensize(10)
borders.penup()
borders.goto(-595, 355)
borders.pendown()
borders.fd(1185)
borders.rt(90)
borders.fd(705)
borders.rt(90)
borders.fd(1185)
borders.rt(90)
borders.fd(705)

# כתיבת השם של הסופר זמן
writer.penup()
writer.speed(55)
writer.goto(-580, 325)
writer.pendown()
writer.color("white")
writer.write("time counter:", font=("OCR A Extended", 15, "normal"))

#כתיבת השם של הסופר נקודות
writer.penup()
writer.goto(415,325)
writer.pendown()
writer.write("point counter:", font=("OCR A Extended", 15, "normal"))
writer.hideturtle()

# הגדרת נקודות
points_list = [point1, point2, point3, point4, point5, point6, point7, point8]
for i in range(len(points_list)):
    points_list[i].speed(150)
for i in range(len(points_list)):
    points_list[i].color("#7f00ff")
for i in range(len(points_list)):
    points_list[i].penup()
for i in range(len(points_list)):
    points_list[i].shape("circle")
for i in range(len(points_list)):
    x = random.randint(-580, 580)
    y = random.randint(-340, 340)
    points_list[i].goto(x, y)
# הגדרת סופר הנקודות
write_points.hideturtle()
write_points.penup()
write_points.color("white")
write_points.goto(485, 300)
write_points.pendown()

# הגדרת הנקודות והמגע בינם לבין השחקן
def point():
    points_counter = 0
    while True:
        for i in range(len(points_list)):
            distance = math.sqrt((turtle_player.xcor() - points_list[i].xcor()) * 2 + (turtle_player.ycor() - points_list[i].ycor()) * 2)
            if distance < 30:
                points_list[i].hideturtle()
                x_point = random.randint(-580, 580)
                y_point = random.randint(-340, 340)
                points_list[i].goto(x_point, y_point)
                points_list[i].showturtle()
                write_points.clear()
                points_counter += 1
                write_points.write(points_counter, font=("OCR A Extended", 15, "normal"))
                break
            else:
                time.sleep(0.0000000001)

pointipounti = threading.Thread(target=point)
pointipounti.start()



# הגדרת הצב
turtle_size = 1
turtle_speed = 2
turtle_player.shape("turtle")
turtle_player.shapesize(turtle_size)
turtle_player.color("#3cb371")
turtle_player.penup()
turtle_player.speed(turtle_speed)

# הערות לשחקן
print("תפסו את הכוכבים")

# סופר הזמן
def timer():
    gametime = 0
    write_timer.color("white")
    write_timer.hideturtle()
    write_timer.penup()
    write_timer.goto(-520, 300)
    write_timer.pendown()
    while True:
        time.sleep(1)
        write_timer.clear()
        gametime += 1
        write_timer.write(gametime, font=("OCR A Extended", 15, "normal"))


timerth = threading.Thread(target=timer)
timerth.start()

# הזזת הצב
turtle_movment = 1


def right():
    turtle_player.setheading(0)


def left():
    turtle_player.setheading(180)


def up():
    turtle_player.setheading(90)


def down():
    turtle_player.setheading(-90)


turtle.listen()


def forwards():
    time.sleep(2)
    while True:
        turtle.onkey(right, "Right")
        turtle.onkey(left, "Left")
        turtle.onkey(up, "Up")
        turtle.onkey(down, "Down")
        turtle_player.fd(turtle_movment)