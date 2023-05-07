"""two player game"""

from .game import Game
from .player import Player

class Two_players_game(Game):
    """class for a two player game
        derived from single player game"""

    def __init__(self, win):
        """creates a two player game object"""

        super().__init__(win, 0)

        self.left_player = Player(self.win, left=True, is_default=True)
        self.right_player = Player(self.win, left=False, is_default=True)


    def end_game(self):
        """decides who won, calss draw winner based on it"""

        self.draw_winner(self.left_player.score == 10)
        self.wait_for_space()
