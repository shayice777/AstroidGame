import turtle
import random

# פונקציה ליצירת טרטל
def create_turtle(color):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    t.speed(0)
    return t

# פונקציה להזזת הטרטל למעלה
def move_up(t):
    t.setheading(90)
    t.forward(10)

# פונקציה ליצירת שבטרטל עם טרטלים
def main():
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    turtles = []
    for i in range(5):
        t = create_turtle("blue")
        t.penup()
        t.goto(random.randint(-300, 300), random.randint(-200, 200))
        turtles.append(t)

    while True:
        wn.update()

        # הזז את הטרטלים למעלה
        for t in turtles:
            move_up(t)

        # בדוק אם טרטל יצא מהמסך ואם כן - החזר אותו לצד השני
        for t in turtles:
            if t.ycor() > 300:
                t.goto(random.randint(-300, 300), -300)

if __name__ == "__main__":
    main()