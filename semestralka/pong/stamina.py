import pygame

class Stamina:
    DECREASE = 5
    INCREASE = 1

    def __init__(self, max_stamina):
        self.max_stamina = max_stamina
        self.stamina = max_stamina


    def decrease(self):
        if self.stamina > self.DECREASE:
            self.stamina -= self.DECREASE


    def increase(self):
        if self.stamina < self.max_stamina:
            self.stamina += self.INCREASE


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
        pygame.draw.rect(win, (255, 255, 255), (0, 0, 400, 50))
        pygame.draw.rect(win, self.color(), (10, 10, 380 * self.stamina / self.max_stamina, 30))


pygame.init()

win = pygame.display.set_mode((400, 400))
stamina = Stamina(1000)

clock = pygame.time.Clock()

while True:
    clock.tick(60)

    stamina.draw(win)
    stamina.decrease()

    pygame.display.update()