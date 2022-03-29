from turtle import Turtle, Screen

cursor = Turtle()
screen = Screen()


def move_forwards():
    cursor.forward(10)

def move_backwards():
    cursor.backward(10)

def turn_left():
    new_heading = cursor.heading() + 10
    cursor.setheading(new_heading)

def turn_right():
    new_heading = cursor.heading() - 10
    cursor.setheading(new_heading)

def clear():
    cursor.clear()
    cursor.penup()
    cursor.home()
    cursor.pendown()

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()