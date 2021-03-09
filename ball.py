from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 1.5
        self.y_move = 1.5
        self.ball_speed = 0.01

    def ball_move(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto((x_new, y_new))

    def bounce_y(self):
        self.y_move *= -1
        self.ball_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.home()
        self.ball_speed = 0.01
        self.bounce_x()