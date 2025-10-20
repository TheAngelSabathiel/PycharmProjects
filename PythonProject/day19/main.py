from turtle import Turtle, Screen
import random

screen = Screen()
screen.screensize(500,500)
# xander = Turtle()
# xander.speed("fastest")
# xander.shape("turtle")

is_race_on = False
all_turtles = []
xander = Turtle()
xander.shape("turtle")
xander.penup()
xander.goto(300,-150)
xander.setheading(90)
xander.pendown()
xander.forward(300)
xander.penup()
xander.home()
xander.hideturtle()

input = screen.textinput("The Great Xander the Turtle Race", "Type the color of the turtle who will win the race?").lower()
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i in range(7):
    xander = Turtle()
    xander.shape("turtle")
    xander.penup()
    xander.color(colors[i])
    xander.goto(-300,i*40-120)
    all_turtles.append(xander)

if input:
    is_race_on = True

print(all_turtles)

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 300:
            winning_turtle = turtle.pencolor()
            is_race_on = False
if winning_turtle == input:
    print(f"The {winning_turtle} turtle wins. You got it right.")
else:
    print(f"The {winning_turtle} turtle wins. You lose.")



# Etch-a-sketch
# def move_forward():
#     xander.forward(10)
#
# def turn_right():
#     new_heading = xander.heading() - 15
#     xander.setheading(new_heading)
#
# def turn_left():
#     new_heading = xander.heading() + 15
#     xander.setheading(new_heading)
#
# def move_backward():
#     xander.backward(10)
#
# def clearscreen():
#     xander.clear()
#     xander.penup()
#     xander.home()
#     xander.pendown()
#
# screen.listen()
# screen.onkey(fun=move_forward, key="w")
# screen.onkey(fun=turn_right, key="d")
# screen.onkey(fun=turn_left, key="a")
# screen.onkey(fun=move_backward, key="s")
# screen.onkey(fun=clearscreen, key="c")


screen.exitonclick()