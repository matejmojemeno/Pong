"""numpy clip for clipping paddle position"""
from numpy import clip
import pygame

class Paddle:
    """paddle class"""

    def __init__(self, x, y, win):
        """creates a paddle object"""
        self.pos_x = x
        self.pos_y = y
        self.width = self.get_width(win)
        self.height = self.get_height(win)


    def get_width(self, win):
        """calculates width of the paddle based on window size"""
        return win.get_width()/100


    def get_height(self, win):
        """calculates height of the paddle based on window size"""
        return win.get_height()/8


    def draw(self, win):
        """draws the paddle"""
        pygame.draw.rect(win, (255, 255, 255), self.pos_x, self.pos_y, self.width, self.height)


    def adjust_paddle(self, win):
        """stops the paddle from going out of the screen"""
        clip(0, win.get_height() - self.height, self.pos_y)


    def move(self, velocity, up, win):
        """moves the paddle up and down"""
        if up:
            self.pos_y -= velocity
        else:
            self.pos_y += velocity
        self.adjust_paddle(win)
