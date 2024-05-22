from turtle import *


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.color('white')
        self.goto(x=350, y=0)
        self.goto(x_cor, y_cor)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


