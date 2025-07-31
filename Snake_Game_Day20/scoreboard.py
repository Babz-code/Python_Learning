from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

with open("data.txt", "r") as file:
    content = int(file.read())

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_number = 0
        self.high_score = content
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score_counter()

    def score_counter(self):
        self.clear()
        self.write(f"Score = {self.score_number} Highscore: {self.high_score}", False, ALIGNMENT, FONT)

    def add_to_score(self):
        self.score_number += 1
        self.score_counter()

    def reset(self):
        if self.score_number > self.high_score:
            self.high_score = self.score_number
            with open("data.txt", "w") as file_2:
                file_2.write(f"{self.high_score}")
        self.score_number = 0
        self.score_counter()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, ALIGNMENT, FONT)