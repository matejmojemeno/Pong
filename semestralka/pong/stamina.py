import pygame

class Stamina:
    BASE_STAMINA = 500
    LEVEL_INCREASE = 25
    DECREASE = 5
    INCREASE = 1

    def __init__(self, level, left):
        self.level = level
        self.max_stamina = self.BASE_STAMINA + level*self.LEVEL_INCREASE
        self.stamina = self.max_stamina
        self.left = left


    def decrease(self):
        if self.stamina > self.DECREASE:
            self.stamina -= self.DECREASE
            return True
        return False


    def increase(self):
        if self.stamina < self.max_stamina:
            self.stamina += self.INCREASE + self.level/10


    def green(self, ratio):
        r = 100 + 155*(1 - ratio)
        return (r, 255, 0)


    def red(self, ratio):
        g = ratio * 255 / 0.3
        return (255, g, 0)


    def color(self):
        stamina_ratio = self.stamina / self.max_stamina

        if stamina_ratio > 0.3:
            return self.green(stamina_ratio)
        return self.red(stamina_ratio)


    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), (500 + 180*(not self.left), 690, 100, 20))
        pygame.draw.rect(win, (0, 0, 0), (502 + 180*(not self.left), 692, 96, 16))
        pygame.draw.rect(win, self.color(), (502 + 180*(not self.left), 692, 96 * self.stamina / self.max_stamina, 16))
