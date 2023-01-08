"""numpy for mathematical operations"""
import numpy as np
import pygame


class Ball:
    """ball object"""

    # ball radius set to 20
    RADIUS = 20
    # velocity of the ball starts at 10
    BASE_VELOCITY = 10

    def __init__(self, win):
        """creates a ball object"""

        # reset does the same and i want left to begin every time
        self.reset(win, going_left=True)

    def move(self):
        """moves the ball depending on its velocity"""
        self.pos_x += self.x_velocity
        self.pos_y += self.y_velocity

    def draw(self, win):
        """draws the ball on the screen"""
        pygame.draw.circle(
            win, (255, 255, 255), (self.pos_x, self.pos_y), self.RADIUS)

    def angle(self):
        """returns angle of the ball and the x axis in radians"""

        # angle with the ball and the x axis
        x_axis_angle = np.arccos(
            self.x_velocity /
            np.sqrt(
                self.x_velocity**2 +
                self.y_velocity**2))

        # i want the smaller angle, and sign determines whether it goes up or
        # down
        return np.sign(-self.y_velocity) * \
            min(x_axis_angle, np.pi - x_axis_angle)

    def total_velocity(self):
        """total velocity of the ball calculated as the euclidian distance of the directional vector"""
        return np.sqrt(self.x_velocity**2 + self.y_velocity**2)

    def starting_velocity(self, going_left):
        """gives the ball its velocity when reset"""

        # random angle, the ball won't bounce before reaching the edge
        angle = np.random.uniform(0, 1 / 2)

        # calculate direction and velocities based on the angle and base
        # velocity
        if going_left:
            return - self.BASE_VELOCITY * \
                np.cos(angle), np.random.choice([-1, 1]) * self.BASE_VELOCITY * np.sin(angle)
        return self.BASE_VELOCITY * \
            np.cos(angle), np.random.choice([-1, 1]) * self.BASE_VELOCITY * np.sin(angle)

    def reset(self, win, going_left):
        """resets the ball after coming off the screen"""

        # ball is put in the middle of the screen
        self.pos_x = win.get_width() / 2
        self.pos_y = win.get_height() / 2

        self.x_velocity, self.y_velocity = self.starting_velocity(going_left)

    def scored_point(self, win):
        """checks if someone scored a point and resets the ball if they did"""

        # check if ball is outside of the screen
        if self.pos_x + self.RADIUS < 0:
            self.reset(win, going_left=True)
            # 1 means the right player scored
            return 1
        if self.pos_x - self.RADIUS > win.get_width():
            self.reset(win, going_left=False)
            # -1 means the left player scored
            return -1

        # 0 means no one scored
        return 0
