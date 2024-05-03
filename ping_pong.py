import turtle
import random
import math
import threading
screen = turtle.Screen()
board = turtle.Turtle()
ball =  turtle.Turtle()
board.speed(100)
board.penup()
board.shape("square")
board.turtlesize(3,16)
board.goto(0,-400)
board.color("green")
# ball
ball.turtlesize(3)
ball.shape("circle")
ball.color("maroon")

ball.setheading(90)

ball.goto(0,482)
def fd_ball():
       while True:
           ball.fd(10)
           screen.update()

fd_ball_fun = threading.Thread(target=fd_ball)
fd_ball_fun.start()


def left_ball_top():
    ball.left(-200)
    screen.update()


def right_ball_top():
    ball.right(-200)
    screen.update()





def ball_loc_up():
    choice_random_list =[1,2]
    rand_value = random.choice(choice_random_list)
    x =  ball.position()
    if x[1] ==  482:
       if rand_value == 1:
           left_ball_top()
       elif rand_value == 2:
            right_ball_top()

ball_loc_up()

#
def left_board():
      board.setheading(180)
      board.fd(100)

def right_board():
      board.setheading(0)
      board.fd(100)


def left_ball_floor():
    ball.left(200)
    screen.update()
    fd_ball()
    print("hii")

def right_ball_floor():
    ball.right(200)
    screen.update()
    fd_ball()
    print("hii")


def contact_ball_board():
    while True:
            distance = math.sqrt((ball.xcor() - board.xcor()) ** 2 + (ball.ycor() - board.ycor()) ** 2)
            if distance < 30:
                ball.setheading(0)

pointipounti = threading.Thread(target=contact_ball_board)
pointipounti.start()

screen.listen()
screen.onkey(left_board,"Left")
screen.onkey(right_board,"Right")

print(ball.position())
print(board.position())
screen.mainloop()