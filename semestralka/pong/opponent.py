"""AI playing the right paddle"""

from .paddle import Paddle


class Opponent:
    """opponent class"""

    def __init__(self, win, difficulty):
        """create opponent object"""

        # every difficulty adds 5 to stats so hard is 15, 15, 15
        self.paddle = Paddle(False, difficulty * 5, difficulty * 5, win)
        self.difficulty = difficulty
        self.score = 0

    def move(self, win, ball):
        """move the paddle"""

        # decide the paddle movement based on x velocity of ball
        if abs(
            self.paddle.pos_x -
            ball.pos_x -
            ball.x_velocity) > abs(
            self.paddle.pos_x -
                ball.pos_x):
            self.center(win)
        else:
            if self.difficulty < 2:
                # for easy and medium
                self.follow_by_edges(ball, win)
            else:
                # got better results in testing so we use this for hard
                self.follow_by_center(ball, win)

    def follow_by_edges(self, ball, win):
        """move to the ball when it goes outside paddle y"""

        if self.paddle.pos_y > ball.pos_y:
            self.paddle.move(True, win)
        if self.paddle.pos_y + self.paddle.height < ball.pos_y:
            self.paddle.move(False, win)

    def follow_by_center(self, ball, win):
        """follow the ball to always match center of paddle and center of ball"""

        if self.paddle.pos_y + self.paddle.height / \
                2 - self.paddle.velocity > ball.pos_y:
            self.paddle.move(True, win)
        if self.paddle.pos_y + self.paddle.height / \
                2 + self.paddle.velocity < ball.pos_y:
            self.paddle.move(False, win)

    def center(self, win):
        """move the paddle to the center when ball is going to the opposite direction"""

        if self.paddle.pos_y + self.paddle.height / 2 < win.get_height() / 2:
            self.paddle.move(False, win)
        elif self.paddle.pos_y + self.paddle.height / 2 > win.get_height() / 2:
            self.paddle.move(True, win)

    def draw(self, win):
        """draw the paddle with default skin"""

        self.paddle.draw('default.png', win)
