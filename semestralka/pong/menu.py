import pygame
import sys

class Menu:
    PATH = 'resources/menu/'
    SUFFIX = '.png'

    ITEM_HEIGHT = 100
    ITEM_SPACE = 50


    def __init__(self, menu_items, win):
        self.win = win

        self.menu_items = self.menu(menu_items, win)


    def menu(self, menu_items, win):
        start = (win.get_height() - len(menu_items)*self.ITEM_HEIGHT - (len(menu_items) - 1)*self.ITEM_SPACE) // 2

        menu = []
        for i, item in enumerate(menu_items):
            image, image_gray = self.scale_image(item)
            rect = self.get_rect(image.get_size()[0], i, start, win)

            menu.append((rect, image, image_gray))
        
        return menu

    
    def scale_image(self, item):
        image = pygame.image.load(self.PATH + item + self.SUFFIX)
        image_gray = pygame.image.load(self.PATH  + 'gray_' + item + self.SUFFIX)
        
        image_height = self.ITEM_HEIGHT
        image_width = image.get_size()[0] * self.ITEM_HEIGHT / image.get_size()[1]

        return (pygame.transform.scale(image, (image_width, image_height)), pygame.transform.scale(image_gray, (image_width, image_height)))


    def get_rect(self, image_width, index, indent_y, win):
        start_x = win.get_width()//2 - image_width//2
        start_y = indent_y + index*(self.ITEM_HEIGHT + self.ITEM_SPACE)

        return pygame.Rect(start_x, start_y, image_width, self.ITEM_HEIGHT)


    def draw_menu(self, win):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for rect, image, gray_image in self.menu_items:
            if not rect.collidepoint(mouse_x, mouse_y):
                win.blit(image, rect)
            else:
                win.blit(gray_image, rect)    


    def pressed(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for item in self.menu_items:
            if item[0].collidepoint(mouse_x, mouse_y):
                return True
        
        return False


    def pressed_item(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for i, item in enumerate(self.menu_items):
            if item[0].collidepoint(mouse_x, mouse_y):
                return i


    def display_menu(self, win):
        chosen = False
        
        while not chosen:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    chosen = self.pressed()

            win.fill((0, 0, 0))
            self.draw_menu(win)
            pygame.display.update()
        
        return self.pressed_item()


def difficulty_menu(win):
    menu_items = ['easy', 'medium', 'hard']

    menu = Menu(menu_items, win)

    action = menu.display_menu(win)

    return


def main_menu(win):
    menu_items = ['play', 'shop', 'exit']

    menu = Menu(menu_items, win)

    action = menu.display_menu(win)

    if action == 0:
        difficulty_menu(win)
    elif action == 1:
        pass
    else:
        return
