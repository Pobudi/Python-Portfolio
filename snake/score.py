from turtle import Turtle
import time


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.score = -1
        self.penup()
        self.hideturtle()

    def add_write(self):
        self.goto(x=0, y=250)
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align="center", font=("Courier", 14, "normal"))

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as file:
                file.write(str(self.score))

            self.high_score = self.score
        self.score = -1
        self.add_write()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 18, "normal"))
        time.sleep(1)
        self.clear()
        #self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align="center", font=("Courier", 14, "normal"))