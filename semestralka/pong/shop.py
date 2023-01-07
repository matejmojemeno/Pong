import pygame
import sys

class Shop:
    def __init__(self, win):
        self.title = self.title(win)
        self.item_images, self.item_rects = self.items()


    def scale_image(self, image, height):
        width = image.get_width() / image.get_height() * height
        return pygame.transform.scale(image, (width, height))


    def title(self, win):
        image = self.scale_image(pygame.image.load('resources/shop/shop.png'), 100)
        rect = pygame.Rect(win.get_width()/2 - image.get_width()/2, 10, image.get_width(), image.get_height())

        return (image, rect)


    def items(self):
        items = ['size', 'speed', 'stamina']

        images = [self.scale_image(pygame.image.load('resources/shop/' + item + '.png'), 50) for item in items]
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


    def draw_plus(self, index, win):
        plus = self.scale_image(pygame.image.load('resources/shop/plus.png'), 38)
        gray_plus = self.scale_image(pygame.image.load('resources/shop/gray_plus.png'), 38)
        
        mouse_x, mouse_y = pygame.mouse.get_pos()

        rect = pygame.Rect(520, 150*index + 70, 38, 38)
            
        if rect.collidepoint(mouse_x, mouse_y):
            win.blit(gray_plus, rect)
        else:
            win.blit(plus, rect)
     

    def draw_coin(self, x, y, win):
        coin = self.scale_image(pygame.image.load('resources/shop/coin.png'), 50)
        rect = pygame.Rect(x - coin.get_width(), y, coin.get_width(), 50)
        
        win.blit(coin, rect)
        return coin.get_width() + 20


    def draw_number(self, number, x, y, win):
        image = self.scale_image(pygame.image.load('resources/numbers/' + number + '.png'), 50)
        rect = pygame.Rect(x - image.get_width(), y, image.get_width(), 50)

        win.blit(image, rect)
        return image.get_width() + 5



    def display_coins(self, amount, x, y, win):
        amount = str(amount)[::-1]

        x -= self.draw_coin(x, y, win)

        for number in amount:
            x -= self.draw_number(number, x, y, win)


pygame.init()

win = pygame.display.set_mode((1280, 720))
shop = Shop(win)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

    shop.draw(win)
    shop.draw_bar(1, 20, win)
    shop.draw_bar(2, 15, win)
    shop.draw_bar(3, 0, win)

    # shop.draw_plus(win)

    shop.display_coins(1000, 1250, 30, win)
    
    pygame.display.update()
    pygame.display.flip()
    