from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 310)
        self.pensize(6)
        self.pencolor("white")
        self.hideturtle()
        while self.ycor() >= -310:
            self.pendown()
            self.sety(self.ycor() - 20)
            self.penup()
            self.sety(self.ycor() - 20)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.rewrite()

    def rewrite(self):
        self.clear()
        self.goto(-190, 220)
        self.write(f"{self.l_score}", align="center", font=("courier", 50, "bold"))
        self.goto(190, 220)
        self.write(f"{self.r_score}", align="center", font=("courier", 50, "bold"))

    def change_l_score(self):
        self.l_score += 1
        self.rewrite()

    def change_r_score(self):
        self.r_score += 1
        self.rewrite()
