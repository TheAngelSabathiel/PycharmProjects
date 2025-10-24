from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_pos = 20 * random.randint(-14,14)
        y_pos = 20 * random.randint(-14,14)
        self.goto(x_pos,y_pos)