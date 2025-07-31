from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.l_score_card()
        self.r_score_card()


    def l_score_card(self):
        self.goto(-100, 260)
        self.write(self.l_score, False, "center", ("Arial", 30, "normal"))

    def r_score_card(self):
        self.goto(100, 260)
        self.write(self.r_score, False, "center", ("Arial", 30, "normal"))

    def add_to_l_score(self):
        self.l_score += 1
        self.clear()
        self.r_score_card()
        self.l_score_card()

    def add_to_r_score(self):
        self.r_score += 1
        self.clear()
        self.r_score_card()
        self.l_score_card()