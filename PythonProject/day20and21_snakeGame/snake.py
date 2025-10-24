from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self, color, shape):
        self.segments = []
        self.snake_color = color
        self.snake_shape = shape
        for x in STARTING_POSITION:

            xander = Turtle()
            # xander.degrees(360.0)
            xander.shape(self.snake_shape)
            xander.color(self.snake_color)
            xander.penup()
            xander.goto(x)
            self.segments.append(xander)

    def add_segment(self):
        xander = Turtle()
        xander.shape(self.snake_shape)
        xander.color(self.snake_color)
        xander.penup()
        xander.goto(self.segments[-1].position())
        self.segments.append(xander)


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
        else:
            print("ok")

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
