import screen
import pygame
from numpy import clip

class Paddle:
    def __init__(self, x, y, width, height):
        self.paddle_x = x
        self.paddle_y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(screen.screen, (255, 255, 255), (self.paddle_x, self.paddle_y, self.width, self.height))

    def adjust_paddle(self):
        clip(0, screen.HEIGHT - self.height, self.paddle_y)
    
    def move(self, velocity, up):    
        if up:
            self.paddle_y -= velocity
        else:
            self.paddle_y += velocity
        self.adjust_paddle()

    


def handle_paddle(keys, paddle, up):
    if keys[pygame.K_w]:
        paddle.move(5, up=True)
    if keys[pygame.K_s]:
        paddle.move(5, up=False)