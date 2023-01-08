"""numpy clip for restraining the paddle from moving out of screen"""
from numpy import clip
import pygame


class Paddle:
    """a paddle object"""

    # paddle with 0 attributes will be 100 pixels tall
    BASE_HEIGHT = 100
    # 20 pixels wide
    BASE_WIDTH = 20
    # moves 7 pixels a tick
    VELOCITY = 7

    def __init__(self, left, size, speed, win):
        """creates a paddle object"""

        self.set_stats(size, speed)
        self.set_x(left, win)

        #in the middle of the screen
        self.pos_y = win.get_height() / 2 - self.height / 2

        self.sprinting_velocity = 0

    def set_stats(self, size, speed):
        """sets stats of paddle based on input"""

        # gets 0.5 pixels wider every level
        self.width = self.BASE_WIDTH + size / 2
        # gets 2.5 pixels taller every level
        self.height = self.BASE_HEIGHT + size * 5 / 2

        # moves 0.2 pixels more a tick every level
        self.velocity = self.VELOCITY + speed / 5

    def set_x(self, left, win):
        """sets the x corrdinate of paddle when created"""

        if left:
            self.pos_x = 20
        else:
            # right side of paddle 20 pixels from the right edge of the screen
            self.pos_x = win.get_width() - 20 - self.width

    def draw(self, skin, win):
        """draws the paddle"""

        # load the image and scale it to paddle size
        skin = pygame.transform.scale(pygame.image.load(
            'resources/skins/' + skin), (self.width, self.height))
        rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

        # draw the image over the rectangle
        win.blit(skin, rect)

    def adjust_paddle(self, win):
        """stops the paddle from going out of the screen"""
        self.pos_y = clip(
            a_min=0,
            a_max=win.get_height() -
            self.height,
            a=self.pos_y)

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
            self.sprinting_velocity = self.velocity * 1.5
        else:
            # the paddle is not moving so 0
            self.sprinting_velocity = 0
