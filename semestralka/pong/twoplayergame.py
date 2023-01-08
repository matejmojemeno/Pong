from .game import Game

class Two_playess_game(Game):
    def __init__(self, win):
        self.win = win

        self.left_player = Player(self.win, left=True, is_default=True)
        self.right_player = Player(self.win, left=False, is_default=True)

        self.ball = Ball(self.win)
        self.left_player_turn = True

        self.ball_stop = 0