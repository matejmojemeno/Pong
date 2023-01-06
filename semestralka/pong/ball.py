"""counterclockwise angle between a point and the x axis"""
import numpy as np
import pygame

class Ball:
    """ball object"""
    RADIUS = 20
    BASE_VELOCITY = 10


    def __init__(self, win):
        """creates a ball object"""
        self.reset(win, going_left=True)
        

    def move(self):
        """moves the ball depending on its velocity"""
        self.pos_x += self.x_velocity
        self.pos_y += self.y_velocity


    def draw(self, win):
        """draws the ball on the screen"""
        pygame.draw.circle(win, (255, 255, 255), (self.pos_x, self.pos_y), self.RADIUS)


    def angle(self):
        """returns angle of the ball and the x axis in radians"""
        x_axis_angle = np.arccos(self.x_velocity / np.sqrt(self.x_velocity**2 + self.y_velocity**2))

        # print(x_axis_angle*180/np.pi, self.x_velocity, self.y_velocity)

        return np.sign(-self.y_velocity) * min(x_axis_angle, np.pi - x_axis_angle)


    def total_velocity(self):
        return np.sqrt(self.x_velocity**2 + self.y_velocity**2)
    

    def starting_velocity(self, going_left):
        angle = np.random.uniform(0, 1/2)
        if going_left:
            return - self.BASE_VELOCITY * np.cos(angle), np.random.choice([-1, 1]) * self.BASE_VELOCITY * np.sin(angle)
        return self.BASE_VELOCITY * np.cos(angle), np.random.choice([-1, 1]) * self.BASE_VELOCITY * np.sin(angle)


    def reset(self, win, going_left):
        self.pos_x = win.get_width()/2
        self.pos_y = win.get_height()/2

        self.x_velocity, self.y_velocity = self.starting_velocity(going_left)


    def won(self, win):
        if self.pos_x + self.RADIUS < 0:
            self.reset(win, going_left=True)
            return 1
        if self.pos_x - self.RADIUS > win.get_width():
            self.reset(win, going_left=False)
            return -1
        return 0