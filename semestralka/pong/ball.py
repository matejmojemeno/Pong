"""counterclockwise angle between a point and the x axis"""
from math import atan2
import pygame

class Ball:
    """ball object"""

    def __init__(self, radius, x_velocity, y_velocity, win):
        """creates a ball object"""
        self.pos_x = win.get_width()/2 #ball will be in the center at the beginning
        self.pos_y = win.get_height()/2

        self.radius = radius

        self.x_velocity = x_velocity
        self.y_velocity = y_velocity


    def move(self):
        """moves the ball depending on its velocity"""
        self.pos_x += self.x_velocity
        self.pos_y += self.y_velocity


    def draw(self, win):
        """draws the ball on the screen"""
        pygame.draw.circle(win, (255, 255, 255), self.pos_x, self.pos_y, self.radius)


    def angle(self):
        """returns angle of the ball and the x axis in radians"""
        return atan2(self.y_velocity, self.x_velocity)
