"""game"""

import sys
import pygame
from .ball import Ball
from .player import Player
from .opponent import Opponent
from .collision import top_bottom_collision, ball_paddle_collision
from.parse_config_file import add_money


class Game:
    """game class"""

    def __init__(self, win, difficulty):
        """creates a game object"""
        self.win = win

        self.ball = Ball(self.win)

        # player turn variable to help avoiding bugs
        # left always starts
        self.left_player_turn = True

        self.left_player = Player(self.win, left=True, is_default=False)
        self.right_player = Opponent(self.ball, win, difficulty)

        # variable to help pause the ball after scoring
        self.ball_stop = 0

    def dashed_line(self):
        """draws a dashed line in the middle of the screen"""
        # this looks weird but it works
        line_length = self.win.get_height() / 20 + 1
        line_space = self.win.get_height() / 30 + 1
        middle = self.win.get_width() / 2

        for i in range(12):
            pygame.draw.rect(self.win, (255, 255, 255), (middle - 2, i * line_length + i * line_space, 4, line_length))

    def check_closed_window(self):
        """exit if player clicked the red X"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def handle_collision(self):
        """checks for collision"""

        if self.left_player_turn:
            hit = ball_paddle_collision(self.ball, self.left_player.paddle)
        else:
            hit = ball_paddle_collision(self.ball, self.right_player.paddle)

        if hit:
            self.left_player_turn = not self.left_player_turn

        top_bottom_collision(self.ball, self.win)

    def add_point(self):
        """adds point to player if ball went out of the screen"""

        hit = self.ball.scored_point(self.win)
        if hit == 1:
            # the ball wont be in play for 60 ticks
            self.ball_stop = 60
            self.left_player_turn = True
            self.right_player.score += 1
        elif hit == -1:
            self.ball_stop = 60
            self.left_player_turn = False
            self.left_player.score += 1

    def draw_number(self, number, left):
        """draws a number, used to draw the score"""

        image = pygame.image.load('resources/numbers/' + number + '.png')
        image = pygame.transform.scale(image, (50 * len(number), 70))

        rect = pygame.Rect(self.win.get_width() / 2 - 100 + 150 * (not left) - 50 * left * (len(number) - 1), 20, 50 * len(number), 70)

        self.win.blit(image, rect)

    def draw_score(self, left):
        """draws both players score"""

        if left:
            score = self.left_player.score
        else:
            score = self.right_player.score

        self.draw_number(str(score), left)

    def press_space_to_continue(self):
        """draws text saying press space to continue"""

        pygame.font.init()
        font = pygame.font.Font(None, 36)
        text = font.render("Press Space to Continue", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = self.win.get_width() / 2 - text_rect.width / 2
        text_y = self.win.get_height() * 3 / 4
        self.win.blit(text, [text_x, text_y])

    def wait_for_space(self):
        """displays a wait for space sign to start or end the game"""
        waiting = True

        # we want to draw eveything in the background
        self.press_space_to_continue()
        self.draw(ball_in_play=False)
        pygame.display.update()

        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False

    def draw_decorations(self):
        """draws every decoration"""

        self.dashed_line()
        self.draw_score(left=True)
        self.draw_score(left=False)

    def check_winner(self):
        """checks if someone won the game"""

        if self.left_player.score == 10 or self.right_player.score == 10:
            return False
        return True

    def end_game(self):
        """decides who won, calss draw winner based on it"""

        self.draw_winner(self.left_player.score == 10)
        self.wait_for_space()

        if self.left_player.score == 10:
            add_money(5 + 5*self.right_player.difficulty)

    def draw_winner(self, left):
        """displays a winner sign on side of the winner"""

        image = pygame.transform.scale(
            pygame.image.load('resources/winner.png'), (230, 50))
        rect = pygame.Rect(205 + (not left) * self.win.get_width() / 2, self.win.get_height() / 2 - 25, 230, 50)

        self. win.blit(image, rect)

    def move(self, ball_in_play):
        """moves everything"""
        if ball_in_play:
            self.ball.move()

        for player in [self.left_player, self.right_player]:
            player.move(self.win)

    def draw(self, ball_in_play):
        """draws everything"""

        if ball_in_play:
            self.ball.draw(self.win)

        for player in [self.left_player, self.right_player]:
            player.draw(self.win)

        self.draw_decorations()

    def game_iteration(self, ball_in_play):
        """makes one iteration of the game cycle"""
        self.draw(ball_in_play)
        self.move(ball_in_play)

        self.handle_collision()
        self.add_point()

    def play(self):
        """main game loop"""

        running = True
        clock = pygame.time.Clock()

        self.wait_for_space()

        while running:
            self.check_closed_window()

            clock.tick(60)
            self.win.fill((0, 0, 0))

            if self.ball_stop <= 0:
                self.game_iteration(ball_in_play=True)
            else:
                self.ball_stop -= 1
                self.game_iteration(ball_in_play=False)

            running = self.check_winner()

            pygame.display.update()

        return self.end_game()
