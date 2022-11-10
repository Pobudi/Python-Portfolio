from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.new()

    def new(self):
        self.color("cyan")
        self.speed("fastest")
        self.goto(randint(-290, 290), randint(-290, 290))
