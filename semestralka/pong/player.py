from .paddle import Paddle
from .stamina import Stamina
from .readplayer import read_stats, read_skins
import pygame

class Player:
    def __init__(self, win, left, is_default):
        self.left = left
        self.score = 0
        self.set_stats(win, left, is_default)


    def set_stats(self, win, left, is_default):
        if is_default:
            self.skin = 'default.png'
            stats = [10, 10, 10]
        else:
            curr_skin, skins = read_skins()
            self.skin = skins[curr_skin][0]
            stats = read_stats()

        self.paddle = Paddle(left, stats[0], stats[1], win)
        self.stamina = Stamina(stats[2], left)


    def draw(self, win):
        self.paddle.draw(self.skin, win)
        self.stamina.draw(win)


    def handle_sprinting(self, shift, up, down):
        if shift and up or shift and down:
            if self.stamina.decrease():
                self.paddle.sprint(is_sprinting=True)
            else:
                self.paddle.sprint(is_sprinting=False)
        else:
            self.paddle.sprint(is_sprinting=False)
            self.stamina.increase()


    def handle_movement(self, up, down, win):
        if up:
            self.paddle.move(up, win)
        if down:
            self.paddle.move(not down, win)


    def handle_keys(self, shift, up, down, win):
        #player is trying to move up and down so he stays in the same place
        if up and down:
            return
        
        self.handle_sprinting(shift, up, down)
        self.handle_movement(up, down, win)


    def move(self, win, ball):
        keys = pygame.key.get_pressed()
        if self.left:
            self.handle_keys(keys[pygame.K_LSHIFT], keys[pygame.K_w], keys[pygame.K_s], win)
        else:
            self.handle_keys(keys[pygame.K_RSHIFT], keys[pygame.K_UP], keys[pygame.K_DOWN], win)