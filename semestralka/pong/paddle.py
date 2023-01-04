"""numpy clip for restraining the paddle from moving out of screen"""
from numpy import clip
import pygame

class Paddle:
    """a paddle object"""
    BASE_HEIGHT = 80
    BASE_WIDTH = 20
    VELOCITY = 10

    def __init__(self, left, size, speed, win):
        """creates a paddle object"""
        
        self.width = self.BASE_WIDTH + size
        self.height = self.BASE_HEIGHT + size*5

        self.set_x(left, win)
        self.set_y(win)

        #TODO dat tomu nejaku normalnu rychlost
        self.velocity = self.VELOCITY + speed
        self.sprinting_velocity = 0


    def set_x(self, left, win):
        if left:
            self.pos_x = 20
        else:
            self.pos_x = win.get_width() - 20 - self.width


    def set_y(self, win):
        self.pos_y = win.get_height()/2 - self.height/2


    def draw(self, win):
        """draws the paddle"""
        pygame.draw.rect(win, (255, 255, 255), (self.pos_x, self.pos_y, self.width, self.height))


    def adjust_paddle(self, win):
        """stops the paddle from going out of the screen"""
        self.pos_y = clip(a_min=0, a_max=win.get_height() - self.height, a=self.pos_y)


    def move(self, up, win):
        """moves the paddle up and down"""
        if up:
            self.pos_y -= max(self.velocity, self.sprinting_velocity)
        else:
            self.pos_y += max(self.velocity, self.sprinting_velocity)
        self.adjust_paddle(win)


    def sprint(self, is_sprinting):
        """make the paddle 50% faster"""
        if is_sprinting:
            self.sprinting_velocity = self.velocity*1.5
        else:
            self.sprinting_velocity = 0