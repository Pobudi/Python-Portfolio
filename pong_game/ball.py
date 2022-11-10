from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_vector = 7
        self.y_vector = 7
        self.move_speed = 0.06

    def move(self):
        if self.ycor() == 280 or self.ycor() == -280:
            self.y_vector *= -1

        if self.xcor() < 380 and self.xcor() > -380:
            new_x = self.xcor() + self.x_vector
            new_y = self.ycor() + self.y_vector
            self.setposition(new_x, new_y)

    def bounce(self):
        self.x_vector *= -1
        self.move_speed *= 0.8

    def reset_game(self):
        self.setposition(0, 0)
        time.sleep(1.5)
        self.move_speed = 0.1
        self.bounce()

