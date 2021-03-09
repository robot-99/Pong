from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player1 = Paddle((350, 0))
player2 = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkeypress(player1.up, "Up")
screen.onkeypress(player1.down, "Down")
screen.onkeypress(player2.up, "w")
screen.onkeypress(player2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.ball_move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    if ball.distance(player1) < 50 and ball.xcor() > 330 or ball.distance(player2) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        score.player2_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score.player1_point()

screen.exitonclick()
