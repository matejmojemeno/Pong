"""player played by a human"""

import pygame
from .paddle import Paddle
from .stamina import Stamina
from .parse_config_file import read_stats, read_skins


class Player:
    """player class"""

    def __init__(self, win, left, is_default):
        """creates a player object"""

        self.left = left
        self.score = 0
        self.set_stats(win, left, is_default)

    def set_stats(self, win, left, is_default):
        """sets stats of players"""

        # default when playing 2 player mode
        if is_default:
            self.skin = 'default'
            stats = [10, 10, 10]
        else:
            curr_skin, skins = read_skins()
            # first object of tuple is name of skin
            self.skin = skins[curr_skin][0]
            stats = read_stats()

        self.paddle = Paddle(left, stats[0], stats[1], win)
        self.skin = pygame.transform.scale(pygame.image.load('resources/skins/' + self.skin), (self.paddle.width, self.paddle.height))
        self.stamina = Stamina(stats[2], left)

    def draw(self, win):
        """draw paddle and stamina of player"""

        self.paddle.draw(self.skin, win)
        self.stamina.draw(win)

    def handle_sprinting(self, shift, up, down):
        """make player sprint if keys are pressed and stamina is available"""
        if shift and up or shift and down:
            if self.stamina.decrease():
                self.paddle.sprint(is_sprinting=True)
            else:
                # not enough stamina
                self.paddle.sprint(is_sprinting=False)
        else:
            self.paddle.sprint(is_sprinting=False)
            self.stamina.increase()

    def handle_movement(self, up, down, win):
        """move player up and down based"""
        if up:
            self.paddle.move(up, win)
        if down:
            self.paddle.move(not down, win)

    def handle_keys(self, shift, up, down, win):
        """handle keys for movement"""

        # player is trying to move up and down so he stays in the same place
        if up and down:
            return

        self.handle_sprinting(shift, up, down)
        self.handle_movement(up, down, win)

    def move(self, win):
        """move player"""
        keys = pygame.key.get_pressed()
        if self.left:
            # use left shift, w, s to move left player
            self.handle_keys(keys[pygame.K_LSHIFT],
                             keys[pygame.K_w], keys[pygame.K_s], win)
        else:
            # use right shift, up, down arrow keys to move right player
            self.handle_keys(keys[pygame.K_RSHIFT],
                             keys[pygame.K_UP], keys[pygame.K_DOWN], win)
