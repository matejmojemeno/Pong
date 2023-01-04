from paddle import Paddle
from ball import Ball

class Opponent:
    def __init__(self, difficulty, win):
        self.paddle = Paddle(False, difficulty * 5, difficulty * 5, win)


    def move(self, ball, win):
        if self.paddle.pos_y + self.paddle.height/2 - self.paddle.velocity > ball.pos_y:
            self.paddle.move(True, win)
        if self.paddle.pos_y + self.paddle.height/2 + self.paddle.velocity < ball.pos_y:
            self.paddle.move(False, win)


    def draw(self, win):
        self.paddle.draw(win)