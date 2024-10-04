from turtle import Turtle
import time

class Paddle(Turtle):

    def __init__(self, position=(0,0)):
        super().__init__()
        self.penup()
        self.position = position
        self.setpos(position)
        self.speed(10)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.begin_cor = self.ycor()+50
        self.end_cor = self.ycor()-50

    def move_up(self):
        y = self.ycor()
        if y < 240:
            self.sety(y + 20)
            self.begin_cor = self.ycor() + 50
            self.end_cor = self.ycor() - 50

    def move_down(self):
        y = self.ycor()
        if y > -240:
            self.sety(y - 20)
            self.speed(10)
            self.begin_cor = self.ycor() - 50
            self.end_cor = self.ycor() + 50

    def paddle_reset(self):
        self.setpos(self.position)
