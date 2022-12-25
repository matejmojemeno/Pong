import screen
import pygame
import numpy as np

class Ball:
    ball_x = screen.WIDTH/2
    ball_y = screen.HEIGHT/2

    def __init__(self, radius, x_velocity, y_velocity):
        self.radius = radius
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def move(self):
        self.ball_x += self.x_velocity
        self.ball_y += self.y_velocity

    def draw(self):
        pygame.draw.circle(screen.screen, screen.WHITE, (self.ball_x, self.ball_y), self.radius)
    
    def angle(self):
        return np.arccos(np.abs(self.x_velocity)/(np.sqrt(self.x_velocity**2 + self.y_velocity**2)))