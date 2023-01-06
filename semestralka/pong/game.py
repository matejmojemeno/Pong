from ball import Ball
from player import Player
from opponent import Opponent
import collision
import pygame
import sys

class Game:
    def __init__(self, win, difficulty):
        self.win = win

        self.left_player = Player(self.win, left=True, is_default=False)
        self.right_player = Opponent(win, difficulty)

        self.ball = Ball(self.win)

        self.left_plaer_turn = True


    def draw(self):
        self.ball.draw(self.win)

        for paddle in [self.left_paddle, self.right_paddle]:
            paddle.draw(self.win)
        
        self.dashed_line()


    def dashed_line(self):
        #this looks weird but it works
        line_length = self.win.get_height() / 20 + 1
        line_space = self.win.get_height() / 30 + 1
        middle = self.win.get_width() / 2

        for i in range(12):
            pygame.draw.rect(self.win, (255, 255, 255), (middle - 2, i*line_length + i*line_space, 4, line_length))


    def check_closed_window(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def handle_players(self):
        for player in [self.left_player, self.right_player]:
            player.move(self.win, self.ball)
            player.draw(self.win)


    def handle_ball(self):
        self.ball.move()
        self.ball.draw(self.win)


    def handle_collision(self):
        if self.left_plaer_turn:
            hit = collision.ball_paddle_collision(self.ball, self.left_player.paddle)
        else:
            hit = collision.ball_paddle_collision(self.ball, self.right_player.paddle)
        
        if hit:
            self.left_plaer_turn = not self.left_plaer_turn

        collision.top_bottom_collision(self.ball, self.win)


    def add_point(self):
        hit = self.ball.won(self.win)
        if hit == 1:
            self.left_plaer_turn = True
        elif hit == -1:
            self.left_plaer_turn = False


    def play(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            self.check_closed_window()
            
            clock.tick(60)
            self.win.fill((0, 0, 0))

            self.handle_players()
            self.handle_ball()
            self.handle_collision()
            self.add_point()

            self.dashed_line()

            pygame.display.update()


class Two_playess_game(Game):
    def __init__(self, win):
        self.win = win

        self.left_player = Player(self.win, left=True, is_default=True)
        self.right_player = Player(self.win, left=False, is_default=False)

        self.ball = Ball(self.win)