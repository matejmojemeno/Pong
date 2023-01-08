"""shop"""

import sys
import pygame
from .parse_config_file import read_coins, read_stats, read_skins, save


class Shop:
    """shop class"""

    def __init__(self):
        """creates a shop object"""
        self.item_images, self.item_rects = self.items()

        self.stats = read_stats()
        self.coins = read_coins()
        self.curr_skin, self.skins = read_skins()
        self.displayed_skin = self.curr_skin

    def scale_image(self, image, height):
        """scales image to a desired size"""
        width = image.get_width() / image.get_height() * height
        return pygame.transform.scale(image, (width, height))

    def items(self):
        """returns list of stat items and their rectangles"""

        items = ['size', 'speed', 'stamina']

        # all scaled to be 50 pixels tall
        images = [
            self.scale_image(
                pygame.image.load(
                    'resources/shop/' +
                    item +
                    '.png'),
                50) for item in items]
        rects = [
            pygame.Rect(
                10,
                150 * i,
                image.get_width(),
                image.get_height()) for i,
            image in enumerate(
                images,
                start=1)]

        return (images, rects)

    def draw_title(self, win):
        """draws Shop title on the top of the screen"""

        image = self.scale_image(
            pygame.image.load('resources/shop/shop.png'), 100)
        rect = pygame.Rect(
            win.get_width() /
            2 -
            image.get_width() /
            2,
            10,
            image.get_width(),
            image.get_height())

        win.blit(image, rect)

    def draw_stats_names(self, win):
        """draws names of the stats"""

        for image, rect in zip(self.item_images, self.item_rects):
            win.blit(image, rect)

    def draw_bar(self, index, amount, win):
        """ draws a bar of stat filled based on level of the stat"""

        pygame.draw.rect(win, (255, 255, 255), (10, 150 * index + 70, 494, 38))
        pygame.draw.rect(win, (0, 0, 0), (15, 150 * index + 75, 484, 28))
        for i in range(amount):
            pygame.draw.rect(
                win, (255, 255, 255), (19 + 24 * i, 150 * index + 79, 20, 20))

    def draw_plus(self, index, win):
        """draws a plus of desired position"""

        plus = self.scale_image(
            pygame.image.load('resources/shop/plus.png'), 38)
        gray_plus = self.scale_image(
            pygame.image.load('resources/shop/gray_plus.png'), 38)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        rect = pygame.Rect(520, 150 * index + 70, 38, 38)

        win.blit(plus, rect)
        if rect.collidepoint(mouse_x, mouse_y):
            win.blit(gray_plus, rect)
            return True

        return False

    def draw_left_arrow(self, win):
        """draws left arrow for the skins"""

        arrow = self.scale_image(pygame.image.load(
            'resources/shop/left_arrow.png'), 38)
        gray_arrow = self.scale_image(pygame.image.load(
            'resources/shop/gray_left_arrow.png'), 38)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        rect = pygame.Rect(700, 370, 38, 38)

        win.blit(arrow, rect)
        if rect.collidepoint(mouse_x, mouse_y):
            win.blit(gray_arrow, rect)
            return True

        return False

    def draw_right_arrow(self, win):
        """draws right arrow for the skins"""

        arrow = self.scale_image(pygame.image.load(
            'resources/shop/right_arrow.png'), 38)
        gray_arrow = self.scale_image(pygame.image.load(
            'resources/shop/gray_right_arrow.png'), 38)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        rect = pygame.Rect(850, 370, 38, 38)

        win.blit(arrow, rect)
        if rect.collidepoint(mouse_x, mouse_y):
            win.blit(gray_arrow, rect)
            return True

        return False

    def draw_coin(self, x, y, win):
        """draws a coin on given position"""

        coin = self.scale_image(
            pygame.image.load('resources/shop/coin.png'), 50)
        rect = pygame.Rect(x - coin.get_width(), y, coin.get_width(), 50)

        win.blit(coin, rect)
        return coin.get_width() + 20

    def draw_number(self, number, x, y, win):
        """draws a number on given position"""

        image = self.scale_image(
            pygame.image.load(
                'resources/numbers/' +
                number +
                '.png'),
            50)
        rect = pygame.Rect(x - image.get_width(), y, image.get_width(), 50)

        win.blit(image, rect)
        return image.get_width() + 5

    def draw_coins(self, amount, x, y, win):
        """draws coins with numbers on given position"""

        amount = str(amount)[::-1]

        x -= self.draw_coin(x, y, win)

        for number in amount:
            x -= self.draw_number(number, x, y, win)

    def total_coins(self, win):
        """draws total coins in the top right corner"""
        self.draw_coins(self.coins, win.get_width() - 30, 30, win)

    def draw_price(self, win, name):
        """draws price for currently displayed skin"""
        image = pygame.transform.scale(
            pygame.image.load(
                'resources/shop/' + name), (50, 30))
        gray_image = pygame.transform.scale(
            pygame.image.load(
                'resources/shop/gray_' + name), (50, 30))

        rect = pygame.Rect(769, 550, 50, 30)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        win.blit(image, rect)
        if rect.collidepoint(mouse_x, mouse_y):
            win.blit(gray_image, rect)
            return True

        return False

    def skin_click(self, win):
        """checks if user is trying to buy or use a skin"""

        if self.curr_skin == self.displayed_skin:
            return
        if self.skins[self.displayed_skin][1]:
            if self.draw_price(win, 'use.png'):
                self.curr_skin = self.displayed_skin
        else:
            if self.draw_price(win, 'price.png') and self.coins >= 10:
                self.coins -= 10
                self.skins[self.displayed_skin] = (
                    self.skins[self.displayed_skin][0], True)

    def draw_skin(self, win):
        """draws currently displayed skin and its price or use option"""

        skin = pygame.image.load('resources/skins/' +
                                 self.skins[self.displayed_skin][0])
        skin = pygame.transform.scale(skin, (50, 250))

        rect = pygame.Rect(769, 264, 50, 250)
        win.blit(skin, rect)

        if self.displayed_skin == self.curr_skin:
            return
        if self.skins[self.displayed_skin][1]:
            self.draw_price(win, 'use.png')
        else:
            self.draw_price(win, 'price.png')

    def draw_back(self, win):
        """draws a back button"""
        back = self.scale_image(
            pygame.image.load('resources/shop/back.png'), 100)
        gray_back = self.scale_image(
            pygame.image.load('resources/shop/gray_back.png'), 100)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        rect = pygame.Rect(
            win.get_width() -
            back.get_width() -
            30,
            win.get_height() -
            130,
            back.get_width(),
            100)

        win.blit(back, rect)
        if rect.collidepoint(mouse_x, mouse_y):
            win.blit(gray_back, rect)
            return True

        return False

    def draw(self, win):
        """draws everything"""

        self.draw_stats_names(win)
        self.total_coins(win)
        self.draw_back(win)
        self.draw_title(win)
        self.draw_left_arrow(win)
        self.draw_right_arrow(win)
        self.draw_skin(win)

        for index, stat in enumerate(self.stats, start=1):
            self.draw_bar(index, stat, win)
            if stat < 20:
                self.draw_plus(index, win)
                self.draw_coins(stat + 1, 450, 150 * index, win)

    def buy_stat(self, index):
        """increases stat if there is enough coins"""

        if self.coins > self.stats[index] + 1:
            self.stats[index] += 1
            self.coins -= self.stats[index]

    def checked_pressed(self, win):
        """checkes if any button is pressed"""

        if self.draw_back(win):
            return True

        for i, stat in enumerate(self.stats):
            if stat >= 20:
                continue
            if self.draw_plus(i + 1, win):
                self.buy_stat(i)

        if self.draw_left_arrow(win):
            self.displayed_skin = (self.displayed_skin - 1) % len(self.skins)
        if self.draw_right_arrow(win):
            self.displayed_skin = (self.displayed_skin + 1) % len(self.skins)

        self.skin_click(win)
        return False

    def display(self, win):
        """main shop loop"""

        # stay in the shop unless back is pressed
        back = False

        clock = pygame.time.Clock()

        while not back:
            win.fill((0, 0, 0))
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # save everything before quitting
                    save(self.stats, self.coins, self.skins, self.curr_skin)
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    back = self.checked_pressed(win)

            self.draw(win)

            pygame.display.update()

        save(self.stats, self.coins, self.skins, self.curr_skin)
