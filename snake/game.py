from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("DarkOliveGreen4")
screen.title("Snake game")
screen.tracer(0)

diego = Turtle()
diego.hideturtle()
diego.penup()
diego.goto(-80, -30)

snake = Snake()
food = Food()
score = Score()
score.add_write()

screen.listen()
screen.onkeyrelease(snake.up, "Up")
screen.onkeyrelease(snake.down, "Down")
screen.onkeyrelease(snake.right, "Right")
screen.onkeyrelease(snake.left, "Left")

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 18:
        food.new()
        score.add_write()
        snake.add_segment()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            score.reset()
            snake.reset()

screen.exitonclick()
