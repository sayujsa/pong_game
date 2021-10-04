import ball
import pad_file
import time
import turtle
import score
from turtle import Screen

screen = Screen()
screen.title("PONG")
screen.bgcolor("black")
screen.setup(800, 600)

turtle.tracer(1, 0)

r_pad = pad_file.Pad(375, 0)
l_pad = pad_file.Pad(-375, 0)

screen.listen()
screen.onkeypress(r_pad.move_up, "Up")
screen.onkeypress(r_pad.move_down, "Down")
screen.onkeypress(l_pad.move_up, "w")
screen.onkeypress(l_pad.move_down, "s")

ball = ball.Ball()

while True:
    points = score.ScoreBoard()
    time.sleep(1)
    ball.ball_speed = 0.07

    while ball.is_inside_bounds():
        time.sleep(ball.ball_speed)
        ball.move(ball.direction)
        if ball.is_at_top_or_bottom():
            ball.bounce("y")
        if ball.is_on_pad(r_pad, l_pad):
            ball.bounce("x")
        ball.gradually_increase_speed()

    if ball.xcor() >= 380:
        points.increase_point(left=1)
    else:
        points.increase_point(right=1)

    if score.l_score == 5:
        points.wins("LEFT SIDE")
        break
    elif score.r_score == 5:
        points.wins("RIGHT SIDE")
        break

    points.refresh_screen()
    ball.home()


screen.exitonclick()
