from menu import Menu
from game import Game, Two_playess_game
import pygame


def difficulty_menu(win):
    menu_items = ['easy', 'medium', 'hard']

    menu = Menu(menu_items, win)

    action = menu.display_menu(win)

    game = Game(win, difficulty=action)
    game.play()


def players_menu(win):
    menu_items = ['1player', '2player']

    menu = Menu(menu_items, win)

    action = menu.display_menu(win)

    if action == 0:
        difficulty_menu(win)
    else:
        game = Two_playess_game(win)
        game.play()


def main_menu(win):
    menu_items = ['play', 'shop', 'exit']

    menu = Menu(menu_items, win)

    action = menu.display_menu(win)

    if action == 0:
        players_menu(win)
    elif action == 1:
        pass
    else:
        return


pygame.init()

win = pygame.display.set_mode((1280, 720))

main_menu(win)

