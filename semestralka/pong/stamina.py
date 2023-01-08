"""stamina"""

import pygame


class Stamina:
    """stamina class"""

    # stamina with 0 upgrades is set to 500
    BASE_STAMINA = 500
    # stamina is increased 25 points with every level
    LEVEL_INCREASE = 25
    # stamina is decreased 5 points every tick
    DECREASE = 5
    # stamina is increased 1 point every tick
    INCREASE = 1

    def __init__(self, level, left):
        """creates a stamina object"""

        self.level = level
        self.max_stamina = self.BASE_STAMINA + level * self.LEVEL_INCREASE
        self.stamina = self.max_stamina
        # boolean whether it belongs to a left paddle
        self.left = left

    def decrease(self):
        """checks stamina and decreases it every tick when it is used"""

        # checks if there is any stamina to use
        if self.stamina > self.DECREASE:
            self.stamina -= self.DECREASE
            # return true because stamina was decreased
            return True
        # no stamina to decrease
        return False

    def increase(self):
        """increases stamina every tick"""

        if self.stamina < self.max_stamina:
            # stamina increases a little faster with higher level
            self.stamina += self.INCREASE + self.level / 10

    def green(self, ratio):
        """return colors from green to yellow as ratio goes from 1 to 0.3"""

        # increases the ratio of red color as ratio goes to 0.3
        r = 255 * (1 - ratio)
        # green is always 255 so the color is more green
        return (r, 255, 0)

    def red(self, ratio):
        """returns colors from yellow to red as ratio goes from 0.3 to 0"""

        # decreses the ratio of green in the color as ratio goes to 0
        g = ratio * 255 / 0.3
        # red is always 255
        return (255, g, 0)

    def color(self):
        """gets the color of the stamina to display it"""

        # stamina ratio
        stamina_ratio = self.stamina / self.max_stamina

        if stamina_ratio > 0.3:
            return self.green(stamina_ratio)
        # the stamina turns red when hits ratio lower than 0.3
        return self.red(stamina_ratio)

    def draw(self, win):
        """draws the stamina on set coordinates"""

        # white rectangle to outline the stamina
        pygame.draw.rect(win, (255, 255, 255),
                         (500 + 180 * (not self.left), 690, 100, 20))
        # black rectangle to be background for the stamina
        pygame.draw.rect(win, (0, 0, 0), (502 + 180 *
                         (not self.left), 692, 96, 16))
        # draw colored stamina, boolean left functions as 0 or 1 to move the
        # stamina
        pygame.draw.rect(win,
                         self.color(),
                         (502 + 180 * (not self.left),
                          692,
                          96 * self.stamina / self.max_stamina,
                          16))
