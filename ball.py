from turtle import Turtle
import time
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.starts = 1
        self.direction = "up"
        self.penup()
        self.color("white")
        self.setpos(0,0)
        self.shape("square")
        self.generate_beginning()

    def generate_beginning(self):
        self.x_move = 3
        self.y_move = random.randint(0,2)
        self.x_move *= self.starts
        self.starts *= -1

    def move(self):
        x = self.xcor()+self.x_move
        y = self.ycor()+self.y_move
        self.goto(x, y)
        self.speed(10)

    def bounce(self):
        self.y_move *= -1

    def reset_ball(self):
        self.direction = "up"
        self.color("white")
        self.setpos(0, 0)
        self.shape("square")
        self.generate_beginning()

    def bounce_paddle(self):
        self.x_move *= -1