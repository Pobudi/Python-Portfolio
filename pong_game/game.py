from turtle import Screen, Turtle
import paddle
import ball
import time
import scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

r_paddle = paddle.Paddle(350)
l_paddle = paddle.Paddle(-350)
ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()
scoreboard.update()


screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce()

    if ball.xcor() > 380:
        ball.reset_game()
        scoreboard.l_score += 1
        scoreboard.update()

    elif ball.xcor() < -380:
        ball.reset_game()
        scoreboard.r_score += 1
        scoreboard.update()


screen.exitonclick()
