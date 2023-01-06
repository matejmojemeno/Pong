import pygame

class Shop:
    def __init__(self, win):
        self.title = self.title(win)
        self.item_images, self.item_rects = self.items()


    def scale_image(self, image, height):
        width = image.get_width() / image.get_height() * height
        return pygame.transform.scale(image, (width, height))


    def title(self, win):
        image = pygame.image.load('resources/shop/shop.png')

        image = self.scale_image(image, 100)
        rect = pygame.Rect(win.get_width()/2 - image.get_width()/2, 10, image.get_width(), image.get_height())

        return (image, rect)


    def items(self):
        items = ['size', 'speed', 'stamina']
        images = [pygame.image.load('resources/shop/' + item + '.png') for item in items]
        images = [self.scale_image(image, 50) for image in images]

        rects = [pygame.Rect(10, 150*i, image.get_width(), image.get_height()) for i, image in enumerate(images, start=1)]

        return (images, rects)


    def draw(self, win):
        win.blit(self.title[0], self.title[1])
        for image, rect in zip(self.item_images, self.item_rects):
            win.blit(image, rect)


    def draw_bar(self, index, amount, win):
        pygame.draw.rect(win, (255, 255, 255), (10, 150*index + 70, 494, 38))
        pygame.draw.rect(win, (0, 0, 0), (15, 150*index + 75, 484, 28))
        for i in range(amount):
            pygame.draw.rect(win, (255, 255, 255), (19 + 24*i, 150*index + 79, 20, 20))


pygame.init()

win = pygame.display.set_mode((1280, 720))
shop = Shop(win)

while True:
    shop.draw(win)
    pygame.display.update()
    shop.draw_bar(1, 20, win)
    shop.draw_bar(2, 15, win)
    shop.draw_bar(3, 0, win)