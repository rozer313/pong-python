from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
import math
import random
import scoreboard

screen = Screen()

screen.title("game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

line = scoreboard.Line()
scoreboard = scoreboard.Scoreboard()

l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))
ball = Ball()

print(l_paddle.xcor())
print(r_paddle.xcor())


def calculate_degree(ball_center, paddle_center):
    distance = ball_center - paddle_center
    if distance < 0:
        distance *= -1

    x_sign = 1
    y_sign = 1
    if ball.x_move < 0:
        x_sign = -1
    if ball.y_move < 0:
        y_sign = -1

    speed_1 = 7
    speed_2 = 8
    speed_3 = 9
    speed_4 = 10

    if 0 <= distance < 5:
        ball.x_move = speed_1
        ball.y_move = speed_1 * math.tan(random.randint(0, 9) * math.pi / 180)
    elif 5 <= distance < 20:
        ball.x_move = speed_2
        ball.y_move = speed_2 * math.tan(random.randint(10, 25) * math.pi / 180)

    elif 20 <= distance < 40:
        ball.x_move = speed_3
        ball.y_move = speed_3 * math.tan(random.randint(26, 40) * math.pi / 180)
    else:
        ball.x_move = speed_4
        ball.y_move = speed_4 * math.tan(random.randint(40, 45) * math.pi / 180)

    ball.x_move *= x_sign
    ball.y_move *= y_sign

    ball.bounce_paddle()

def l_bot():
    if ball.xcor() <= 0:
        y = ball.ycor() - (ball.ycor() % 20)
        if y > l_paddle.ycor():
            l_paddle.move_up()
        elif y < l_paddle.ycor():
            l_paddle.move_down()


def r_bot():
    if ball.xcor() >= 0:
        if ball.ycor() > r_paddle.begin_cor:
            r_paddle.move_up()
        elif ball.ycor() < r_paddle.end_cor:
            r_paddle.move_down()


screen.listen()
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

is_game_on = True
print(r_paddle.xcor())
while is_game_on:
    screen.update()
    ball.move()
    l_bot()
    r_bot()
    if (ball.distance(r_paddle) <= 50) and ball.xcor() >= r_paddle.xcor():
        calculate_degree(r_paddle.ycor(), ball.ycor())

    if (ball.distance(l_paddle) <= 50) and ball.xcor() <= l_paddle.xcor():
        calculate_degree(l_paddle.ycor(), ball.ycor())

    if ball.xcor() > 390 or ball.xcor() < -390:
        if ball.xcor() > 390:
            scoreboard.change_l_score()
        elif ball.xcor() < -390:
            scoreboard.change_r_score()

        time.sleep(0.1)

        ball.reset_ball()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    time.sleep(0.01)

screen.exitonclick()
