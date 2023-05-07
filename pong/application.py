"""wraps the whole application"""

from .menu import Menu
from .game import Game
from .twoplayergame import Two_players_game
from .shop import Shop
from .parse_config_file import add_money


class Application:
    """application class"""

    def __init__(self, win):
        """creates application object"""
        self.win = win

    def run(self):
        """runs main menu"""
        self.main_menu()

    def difficulty_menu(self):
        """choose difficulty of opponent in single player"""

        menu_items = ['easy', 'medium', 'hard', 'back']

        menu = Menu(menu_items, self.win)
        action = menu.display_menu(self.win)

        if action == 3:
            # return true when back is chosen
            return True

        self.win.fill((0, 0, 0))
        game = Game(self.win, difficulty=action)
        if game.play():
            add_money(5 + action * 5)

        return False

    def players_menu(self):
        """choose between 1 player and 2 player mode"""

        menu_items = ['1player', '2player', 'back']

        menu = Menu(menu_items, self.win)
        action = menu.display_menu(self.win)

        # choosing what to do based on menu return
        if action == 0:
            if self.difficulty_menu():
                # prevent from going to main menu when back is chosen
                self.players_menu()
        elif action == 1:
            self.win.fill((0, 0, 0))
            game = Two_players_game(self.win)
            game.play()

    def main_menu(self):
        """main menu of the game"""

        menu_items = ['play', 'shop', 'exit']

        # create a menu object with main menu items
        menu = Menu(menu_items, self.win)
        action = menu.display_menu(self.win)

        # action is 2 when player clicked back
        while action != 2:
            # choosing what to do based on menu return
            if action == 0:
                self.players_menu()
            else:
                shop = Shop()
                shop.display(self.win)

            # stay in main menu after returnim from playing and shop
            action = menu.display_menu(self.win)
