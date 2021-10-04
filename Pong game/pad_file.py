import turtle


class Pad(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(x, y)

    def move_up(self):
        if self.ycor() <= 240:
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def move_down(self):
        if self.ycor() >= -220:
            y = self.ycor() - 20
            self.goto(self.xcor(), y)
