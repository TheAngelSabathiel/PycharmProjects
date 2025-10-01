from turtle import Turtle, Screen
import random
import colorgram


# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return r,g,b
#
# screen = Screen()
# xander = Turtle()
# xander.shape("turtle")
# xander.color("blue")
# xander.shapesize(1.5,1.5,3)
# xander.fillcolor("skyblue")
# xander.speed("fastest")
# screen.colormode(255)

#Challenge 1 - Drawing a square
# for x in range(4):
#     xander.forward(100)
#     xander.left(90)

# joms = Turtle()
#
# joms.forward(10)
# joms.color("white")
# joms.forward(10)
# joms.pensize(1)

# Random drawing
# t = Turtle()
# for i in range(100):
#     steps = int(random.random()*100)
#     angle = int(random.random()*360)
#     t.right(angle)
#     t.forward(steps)

#Challenge 2 - Drawing a broken line 10 px
# for i in range(100):
#     xander.forward(10)
#     xander.penup()
#     xander.forward(10)
#     xander.pendown()


#Challenge 3 - Drawing color changing polygons

# for n in range(3,11):
#     xander.color(random_color())
#     internal_angle = ((n - 2) * 180) / n
#     for x in range(n):
#         xander.forward(100)
#         xander.right(180 - internal_angle)

#Challenge 4 - Drawing random walk
# xander.pensize(10)
# for x in range(10000):
#     xander.color(random_color())
#     xander.right(random.randint(1,4)*90)
#     xander.forward(20)

#Challenge 5 - Drawing a spirograph

# size_of_gap = int(input("Size of gap in degrees: "))
# for x in range(int(360/size_of_gap)):
#     xander.circle(100)
#     xander.setheading(xander.heading() + size_of_gap)
#     xander.color(random_color())

# Main Challenge: Damien Hirst Painting

colors = colorgram.extract("image.jpg", 10)
print(colors)

color = colorgram.Color()

print(color)













screen.exitonclick()