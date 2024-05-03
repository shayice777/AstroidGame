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
points_list = []
POINTS_NUM = 12
for i in range(POINTS_NUM):
    new_turtle_point = turtle.Turtle()
    new_turtle_point.name = 'point'+str(i)
    points_list.append(new_turtle_point)

# אסטרואידים
asteroid_list = []
ASTEROID_NUM = 5
for i in range(ASTEROID_NUM):
    new_turtle = turtle.Turtle()
    new_turtle.name = 'asteroid'+str(i)
    asteroid_list.append(new_turtle)

# הגדרת המסך-משתנים קבועים
X_SCREEN_SIZE = 1200
Y_SCREEN_SIZE = 720

#הגדרת מסך
screen.bgcolor("black")
screen.setup(X_SCREEN_SIZE, Y_SCREEN_SIZE)

# ציור גבולות-משתנים קבועים
BORDERS_PAINTER_SPEED = 100
BORDERS_PAINTER_PENSIZE = 10
BORDERS_PAINTER_STARTING_POINT_X = -595
BORDERS_PAINTER_STARTING_POINT_Y = 355
BORDERS_PAINTER_FD_WIDTH = 1185
BORDERS_PAINTER_FD_LENGTH = 705
BORDERS_PAINTER_TURN = 90

# ציור גבולות
borders.speed(BORDERS_PAINTER_SPEED)
borders.hideturtle()
borders.color("#ff0f05")
borders.pensize(BORDERS_PAINTER_PENSIZE)
borders.penup()
borders.goto(BORDERS_PAINTER_STARTING_POINT_X, BORDERS_PAINTER_STARTING_POINT_Y)
borders.pendown()
borders.fd(BORDERS_PAINTER_FD_WIDTH)
borders.rt(BORDERS_PAINTER_TURN)
borders.fd(BORDERS_PAINTER_FD_LENGTH)
borders.rt(BORDERS_PAINTER_TURN)
borders.fd(BORDERS_PAINTER_FD_WIDTH)
borders.rt(BORDERS_PAINTER_TURN)
borders.fd(BORDERS_PAINTER_FD_LENGTH)

# כתיבת השם של הסופר זמן-משתנים קבועים
WRITER_SPEED = 55
TIMER_WRITER_X = -580
TIMER_WRITER_Y = 325
FONT_SIZE = 15

#כתיבת השם של הסופר זמן
writer.penup()
writer.speed(WRITER_SPEED)
writer.goto(TIMER_WRITER_X, TIMER_WRITER_Y)
writer.pendown()
writer.color("white")
writer.write("time counter:", font=("OCR A Extended", FONT_SIZE, "normal"))

#כתיבת השם של הסופר נקודות-משתנים קבועים
POINTS_WRITER_X = 415
POINTS_WRITER_Y = 325

writer.penup()
writer.goto(POINTS_WRITER_X,POINTS_WRITER_Y)
writer.pendown()
writer.write("point counter:", font=("OCR A Extended", FONT_SIZE, "normal"))
writer.hideturtle()

# הגדרת נקודות-משתנים קבועים
POINTS_AND_ASTEROID_SPEED = 150
X_POINTS = 580
Y_POINTS = 340

# הגדרת נקודות
for i in range(len(points_list)):
    points_list[i].speed(POINTS_AND_ASTEROID_SPEED)
    points_list[i].penup()
    x_points = random.randint(-X_POINTS, X_POINTS)
    y_points = random.randint(-Y_POINTS, Y_POINTS)
    points_list[i].goto(x_points, y_points)

# הגדרת אסטרואידיפ-משתנים קבועים


# הגדרת אסטרואידים
for i in range(len(asteroid_list)):
    asteroid_list[i].speed(1)
    asteroid_list[i].penup()
    asteroid_list[i].pencolor("purple")
    asteroid_list[i].circle(500)




# הגדרת סופר נקודות-משתנים קבועים
X_WRITE_POINTS = 485
Y_WRITE_POINTS = 300

# הגדרת סופר הנקודות
write_points.hideturtle()
write_points.penup()
write_points.color("white")
write_points.goto(X_WRITE_POINTS, Y_WRITE_POINTS)
write_points.pendown()

# הגדרת הנקודות והמגע בינם לבין השחקן-משתנים קבועים
RANGE_RANDOMAX_X = 580
RANGE_RANDOMAX_Y = 340
STARTING_POINTS = 0
RADIUS_DISTANCE = 30

# הגדרת הנקודות והמגע בינם לבין השחקן
def point_asteroid():
    points_counter = STARTING_POINTS
    while True:
        for i in range(len(points_list)):
            distance = math.sqrt((turtle_player.xcor() - points_list[i].xcor()) ** 2 + (turtle_player.ycor() - points_list[i].ycor()) ** 2)
            if distance < RADIUS_DISTANCE:
                points_list[i].hideturtle()
                x_point = random.randint(-RANGE_RANDOMAX_X, RANGE_RANDOMAX_X)
                y_point = random.randint(-RANGE_RANDOMAX_Y, RANGE_RANDOMAX_Y)
                points_list[i].goto(x_point, y_point)
                points_list[i].showturtle()
                write_points.clear()
                points_counter += 1
                write_points.write(points_counter, font=("OCR A Extended", FONT_SIZE, "normal"))
                break
            else:
                time.sleep(0.0000000001)

pointipounti = threading.Thread(target=point_asteroid)
pointipounti.start()

# הגדרת הצב
turtle_speed = 50
turtle_player.shape("turtle")
turtle_player.color("#3cb371")
turtle_player.penup()
turtle_player.speed(turtle_speed)

# הערות לשחקן
print("תפסו את הכוכבים")

# סופר הזמן-משתנים קבועים
X_WRITE_TIMER = -520
Y_WRITE_TIMER = 300

# סופר הזמן
def timer():
    gametime = 0
    write_timer.color("white")
    write_timer.hideturtle()
    write_timer.penup()
    write_timer.goto(X_WRITE_TIMER, Y_WRITE_TIMER)
    write_timer.pendown()
    while True:
        time.sleep(1)
        write_timer.clear()
        gametime += 1
        write_timer.write(gametime, font=("OCR A Extended", FONT_SIZE, "normal"))


timerth = threading.Thread(target=timer)
timerth.start()

# הזזת הצב
turtle_movment = 0.8

def right():
    turtle_player.setheading(0)


def left():
    turtle_player.setheading(180)


def up():
    turtle_player.setheading(90)


def down():
    turtle_player.setheading(-90)


turtle.listen()

# הגדרת המפגש של הצב עם הגבולות-משתנים קבועים
X_MAX_SCREEN_LIMITS = 572
X_MIN_SCREEN_LIMITS = -574
Y_MAX_SCREEN_LIMITS = 338
Y_MIN_SCREEN_LIMITS = -332
X_WRITER_GAME_OVER = -450
Y_WRITER_GAME_OVER = -110
WRITER_GAME_OVER_FONT_SIZE = 230

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
        if x_pos_turtle_player > X_MAX_SCREEN_LIMITS or x_pos_turtle_player < X_MIN_SCREEN_LIMITS or y_pos_turtle_player > Y_MAX_SCREEN_LIMITS or y_pos_turtle_player < Y_MIN_SCREEN_LIMITS:
            for i in range(5):
                writer_game_over.hideturtle()
                writer_game_over.penup()
                writer_game_over.goto(X_WRITER_GAME_OVER,Y_WRITER_GAME_OVER)
                writer_game_over.color("red")
                writer_game_over.pendown()
                writer_game_over.write("Game Over", font=("Chiller", WRITER_GAME_OVER_FONT_SIZE, "normal"))
                time.sleep(1)
                writer_game_over.clear()
            turtle.bye()

            break


for_r = threading.Thread(target=forwards)
for_r.start()

screen.mainloop()