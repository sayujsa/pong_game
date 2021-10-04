import turtle
l_score = 0
r_score = 0


class ScoreBoard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"{l_score} : {r_score}", align="center", font=("arial", 20, "bold"))

    @staticmethod
    def increase_point(left=0, right=0):
        global l_score, r_score
        l_score += left
        r_score += right

    def refresh_screen(self):
        self.clear()

    def wins(self, side):
        self.color("white")
        self.goto(0, 0)
        self.write(f"{side} WINS", align="center", font=("arial", 20, "bold"))
