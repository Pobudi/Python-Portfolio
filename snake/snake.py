from turtle import Turtle

INDEX = -1
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def color_choice(self):
        global INDEX, COLORS
        INDEX += 1
        if INDEX == 7:
            INDEX = 0
        return COLORS[INDEX]

    def create_snake(self):
        for i in range(3):
            global INDEX, COLORS
            diego = Turtle(shape="square")
            diego.color(f"{self.color_choice()}")
            diego.penup()
            diego.goto(x=0 - (20 * i), y=0)

            self.segments.append(diego)

    def move(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if x == 300:
            self.head.goto(x - 600, y)
        elif x == -300:
            self.head.goto(x + 600, y)
        elif y == 300:
            self.head.goto(x, y - 600)
        elif y == -300:
            self.head.goto(x, y + 600)

        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def add_segment(self):
        position = self.segments[-1].position()
        diego = Turtle(shape="square")
        diego.color(self.color_choice())
        diego.penup()
        diego.goto(position)

        self.segments.append(diego)

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

