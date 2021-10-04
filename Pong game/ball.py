import turtle


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.direction = [10, 10]
        self.ball_speed = 0.07

    def move(self, direction):
        self.goto(self.xcor() + direction[0], self.ycor() + direction[1])

    def bounce(self, x_or_y):
        if x_or_y == "x":
            self.direction[0] *= -1
        else:
            self.direction[1] *= -1

    def gradually_increase_speed(self):
        self.ball_speed -= 0.00005

    def is_inside_bounds(self):
        if 380 > self.xcor() > -380:
            return True
        else:
            return False
        
    def is_at_top_or_bottom(self):
        if 280 < self.ycor() or -280 > self.ycor():
            return True
        else:
            return False
    
    def is_on_pad(self, r_pad, l_pad):
        if self.xcor() > 340 and self.distance(r_pad) < 50 or self.xcor() < -340 and self.distance(l_pad) < 50:
            return True
        else:
            return False
