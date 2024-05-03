# זימון ספריות
import threading
import time
import turtle
import random
import math

# יצירת הכלים למשחק
screen = turtle.Screen()
turtle_player = turtle.Turtle()
screen.register_shape("C:/Users/shaya/PycharmProjects/pythonProject7/vO04Ex.gif")
turtle_player.shape("C:/Users/shaya/PycharmProjects/pythonProject7/vO04Ex.gif")

writer = turtle.Turtle()
writer_game_over = turtle.Turtle()
write_timer = turtle.Turtle()
write_points = turtle.Turtle()
borders = turtle.Turtle()

# נקודות
points_list = []
for i in range(8):
    new_turtle = turtle.Turtle()
    new_turtle.name = 'point'+str(i)
    points_list.append(new_turtle)

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
for i in range(len(points_list)):
    points_list[i].speed(1500)
    points_list[i].hideturtle()
    points_list[i].color("#7f00ff")
    points_list[i].penup()
    points_list[i].shape("circle")
    x = random.randint(-580, 580)
    y = random.randint(-340, 340)
    points_list[i].goto(x, y)
    points_list[i].showturtle()

# הגדרת סופר הנקודות
write_points.hideturtle()
write_points.penup()
write_points.color("white")
write_points.goto(485, 300)
write_points.pendown()

# הגדרת הנקודות והמגע בינם לבין השחקן
RANGE_RANDOMAX_X = 580
RANGE_RANDOMAX_Y = 340
def point():
    points_counter = 0
    while True:
        for i in range(len(points_list)):
            distance = math.sqrt((turtle_player.xcor() - points_list[i].xcor()) ** 2 + (turtle_player.ycor() - points_list[i].ycor()) ** 2)
            if distance < 30:
                points_list[i].hideturtle()
                x_point = random.randint(-RANGE_RANDOMAX_X, RANGE_RANDOMAX_X)
                y_point = random.randint(-RANGE_RANDOMAX_Y, RANGE_RANDOMAX_Y)
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
class Colors:
    magenta = '\033[35m'

print(Colors.magenta+"תפסו את הכוכבים")

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

# הגדרת המפגש של הצב עם הגבולות
        x_y_pos_turtle_player = turtle_player.pos()
        x_pos_turtle_player = x_y_pos_turtle_player[0]
        y_pos_turtle_player = x_y_pos_turtle_player[1]
        if x_pos_turtle_player > 572 or x_pos_turtle_player < -574 or y_pos_turtle_player > 338 or y_pos_turtle_player < -332:
            for i in range(5):
                writer_game_over.hideturtle()
                writer_game_over.penup()
                writer_game_over.goto(-370,-120)
                writer_game_over.color("red")
                writer_game_over.pendown()
                writer_game_over.write("Game Over", font=("Chiller", 180, "normal"))
                turtle.bye()

            break

turtle_player.shape("C:/Users/shaya/PycharmProjects/pythonProject7/vO04Ex.gif")
for_r = threading.Thread(target=forwards)
for_r.start()

screen.mainloop()