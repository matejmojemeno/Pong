from paddle import Paddle
from stamina import Stamina
import pygame

class Player:
    def __init__(self, win, left, is_default):
        self.paddle = Paddle(left, 0, 0, win)
        self.stamina = Stamina(1000, left)
        self.left = left


    def draw(self, win):
        self.paddle.draw(win)
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
        #playes is trying to move up and down so he stays in the same place
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