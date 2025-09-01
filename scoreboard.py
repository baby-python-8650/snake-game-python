from turtle import Turtle
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.count_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update_score_board()


    def update_score_board(self):
        self.write(f"SCORE = {self.count_score}", align="center", font=("Arial", 15, "bold"))


    def update_score(self):
        self.count_score += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write(f"GAMEOVER.. ", align="center", font=("Lucida Console", 30, "bold"))