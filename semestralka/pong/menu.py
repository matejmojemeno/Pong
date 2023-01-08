"""menu"""

import sys
import pygame


class Menu:
    """menu class"""

    # path to folder with menu items images
    PATH = 'resources/menu/'
    # every image is png
    SUFFIX = '.png'
    # gray image prefix
    PREFIX = 'gray_'

    # every menu item will be 100 pixels tall
    ITEM_HEIGHT = 100
    # 50 pixels space between menu items
    ITEM_SPACE = 50

    def __init__(self, menu_items, win):
        """creates a menu object"""

        self.win = win
        self.menu_items = self.menu(menu_items, win)

    def menu(self, menu_items, win):
        """creates list of tuples (image, rectangle)"""

        # want to have the same amount of space on each side
        start = (win.get_height() - len(menu_items) *
                 self.ITEM_HEIGHT - (len(menu_items) - 1) * self.ITEM_SPACE) / 2

        menu = []
        for i, item in enumerate(menu_items):
            image, image_gray = self.scale_image(item)
            rect = self.get_rect(image.get_size()[0], i, start, win)

            menu.append((rect, image, image_gray))

        return menu

    def scale_image(self, item):
        """scales the image to width x 100 pixels"""

        image = pygame.image.load(self.PATH + item + self.SUFFIX)
        image_gray = pygame.image.load(
            self.PATH + self.PREFIX + item + self.SUFFIX)

        image_height = self.ITEM_HEIGHT
        # calculates the wwidth so the ratio of original image isnt changed
        image_width = image.get_size()[0] * \
            self.ITEM_HEIGHT / image.get_size()[1]

        # returns tuple of transformed images
        return (
            pygame.transform.scale(
                image, (image_width, image_height)), pygame.transform.scale(
                image_gray, (image_width, image_height)))

    def get_rect(self, image_width, index, indent_y, win):
        """rectangle for each image"""

        start_x = win.get_width() // 2 - image_width // 2
        start_y = indent_y + index * (self.ITEM_HEIGHT + self.ITEM_SPACE)

        return pygame.Rect(start_x, start_y, image_width, self.ITEM_HEIGHT)

    def draw_menu(self, win):
        """draws menu"""

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for rect, image, gray_image in self.menu_items:
            # gray images are drawn when you hover over them with a mouse
            if not rect.collidepoint(mouse_x, mouse_y):
                win.blit(image, rect)
            else:
                win.blit(gray_image, rect)

    def pressed(self):
        """checks if some menu item is pressed, also returns index if pressed"""

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for i, item in enumerate(self.menu_items):
            if item[0].collidepoint(mouse_x, mouse_y):
                return True, i

        return False

    def display_menu(self, win):
        """main menu loop"""

        # determines if any option was chosen
        chosen = False

        while not chosen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    chosen, option = self.pressed()

            win.fill((0, 0, 0))
            self.draw_menu(win)
            pygame.display.update()

        # return the option after being chosen
        return option
