from paddle import Paddle
from ball import Ball

class Opponent:
    def __init__(self, win, difficulty):
        self.paddle = Paddle(False, difficulty * 5, difficulty, win)
        self.difficulty = difficulty


    def move(self, win, ball):
        if abs(self.paddle.pos_x - ball.pos_x - ball.x_velocity) > abs(self.paddle.pos_x - ball.pos_x):
            self.center(win)
        else:
            if self.difficulty < 2:
                self.follow_ball(ball, win)
            else:
                self.follow_ball2(ball, win)


    def follow_ball(self, ball, win):
        if self.paddle.pos_y > ball.pos_y:
            self.paddle.move(True, win)
        if self.paddle.pos_y + self.paddle.height < ball.pos_y:
            self.paddle.move(False, win)


    def follow_ball2(self, ball, win):
        if self.paddle.pos_y + self.paddle.height/2 - self.paddle.velocity > ball.pos_y:
            self.paddle.move(True, win)
        if self.paddle.pos_y + self.paddle.height/2 + self.paddle.velocity < ball.pos_y:
            self.paddle.move(False, win)


    def center(self, win):
        if self.paddle.pos_y + self.paddle.height/2 < win.get_height()/2:
            self.paddle.move(False, win)
        elif self.paddle.pos_y + self.paddle.height/2 > win.get_height()/2:
            self.paddle.move(True, win)


    def draw(self, win):
        self.paddle.draw(win)