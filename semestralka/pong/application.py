from .menu import Menu
from .game import Game, Two_playess_game
from .shop import Shop
from .readplayer import add_money
import pygame

class Application:
    def __init__(self, win):
        self.win = win


    def run(self):
        self.main_menu()


    def difficulty_menu(self):
        menu_items = ['easy', 'medium', 'hard', 'back']

        menu = Menu(menu_items, self.win)

        action = menu.display_menu(self.win)

        if action == 3:
            return

        self.win.fill((0, 0, 0))
        game = Game(self.win, difficulty=action)
        if game.play():
            add_money(5 + action*5)


    def players_menu(self):
        menu_items = ['1player', '2player', 'back']

        menu = Menu(menu_items, self.win)

        action = menu.display_menu(self.win)

        if action == 0:
            self.difficulty_menu()
        else:
            self.win.fill((0, 0, 0))
            game = Two_playess_game(self.win)
            game.play()


    def main_menu(self):
        menu_items = ['play', 'shop', 'exit']

        menu = Menu(menu_items, self.win)

        action = menu.display_menu(self.win)

        while action != 2:
            if action == 0:
                self.players_menu()
            else:
                shop = Shop()
                shop.display(self.win)

            action = menu.display_menu(self.win)
