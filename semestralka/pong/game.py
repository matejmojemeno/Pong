from .ball import Ball
from .player import Player
from .opponent import Opponent
from .collision import top_bottom_collision, ball_paddle_collision
import pygame
import sys

class Game:
    def __init__(self, win, difficulty):
        self.win = win

        self.left_player = Player(self.win, left=True, is_default=False)
        self.right_player = Opponent(win, difficulty)

        self.ball = Ball(self.win)
        self.left_player_turn = True

        self.ball_stop = 0


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
            if event.type == pygame.QUIT:
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
        if self.left_player_turn:
            hit = ball_paddle_collision(self.ball, self.left_player.paddle)
        else:
            hit = ball_paddle_collision(self.ball, self.right_player.paddle)
        
        if hit:
            self.left_player_turn = not self.left_player_turn

        top_bottom_collision(self.ball, self.win)


    def add_point(self):
        hit = self.ball.won(self.win)
        if hit == 1:
            self.ball_stop = 30
            self.left_player_turn = True
            self.right_player.score += 1
        elif hit == -1:
            self.ball_stop = 30
            self.left_player_turn = False
            self.left_player.score += 1


    def draw_number(self, number, left):
        image = pygame.image.load('resources/numbers/' + number + '.png')
        image = pygame.transform.scale(image, (50*len(number), 70))

        rect = pygame.Rect(self.win.get_width()/2 - 100 + 150*(not left) - 50*left*(len(number) - 1), 20, 50*len(number), 70)

        self.win.blit(image, rect)


    def draw_score(self, left):
        if left:
            score = self.left_player.score
        else:
            score = self.right_player.score
        
        self.draw_number(str(score), left)


    def press_space_to_continue(self):
        pygame.font.init()
        font = pygame.font.Font(None, 36)
        text = font.render("Press Space to Continue", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = self.win.get_width() / 2 - text_rect.width / 2
        text_y = self.win.get_height() * 3 / 4
        self.win.blit(text, [text_x, text_y])


    def wait_for_space(self):
        waiting = True

        self.press_space_to_continue()
        self.handle_players()
        self.draw_decorations()
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
        self.dashed_line()
        self.draw_score(left=True)
        self.draw_score(left=False)


    def game_iteration(self, ball_in_play):
        if ball_in_play:
            self.handle_ball()
        self.handle_players()
        self.handle_collision()
        self.draw_decorations()
        self.add_point()


    def check_winner(self):
        if self.left_player.score == 10 or self.right_player.score == 10:
            return False
        return True


    def end_game(self):
        if self.left_player.score == 10:
            left_winner = True
        else:
            left_winner = False
        self.draw_winner(left_winner)
        self.wait_for_space()


    def draw_winner(self, left):
        image = pygame.transform.scale(pygame.image.load('resources/winner.png'), (230, 50))
        rect = pygame.Rect(205 + left*self.win.get_width()/2, self.win.get_height()/2 - 25, 230, 50)

        self. win.blit(image, rect)


    def play(self):
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


class Two_playess_game(Game):
    def __init__(self, win):
        self.win = win

        self.left_player = Player(self.win, left=True, is_default=True)
        self.right_player = Player(self.win, left=False, is_default=True)

        self.ball = Ball(self.win)
        self.left_player_turn = True

        self.ball_stop = 0