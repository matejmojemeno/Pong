import pygame
from ball import Ball
from paddle import Paddle
import collision
from opponent import Opponent

class Game:
    def __init__(self, win):
        self.win = win

        self.left_paddle = Paddle(True, 0, 0, self.win)
        self.opponent = Opponent(1, self.win)

        self.ball = Ball(self.win)


    def draw(self):
        self.ball.draw(self.win)

        for paddle in [self.left_paddle, self.right_paddle]:
            paddle.draw(self.win)


    def handle_window(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                return False
        
        return True


    def handle_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LSHIFT]:
            self.left_paddle.sprint(True)
        else:
            self.left_paddle.sprint(False)
        if keys[pygame.K_w]:
            self.left_paddle.move(up=True, win=self.win)
        if keys[pygame.K_s]:
            self.left_paddle.move(up=False, win=self.win)

        return ()

    def play(self):
        running = True

        clock = pygame.time.Clock()

        while running:
            running = self.handle_window()
            
            clock.tick(60)

            self.win.fill((0, 0, 0))

            self.handle_keys()
            self.opponent.move(self.ball, self.win)

            self.left_paddle.draw(self.win)
            self.opponent.draw(self.win)

            self.ball.move()
            self.ball.draw(self.win)

            self.ball.won(self.win)

            collision.ball_paddle_collision(self.ball, self.left_paddle)
            collision.ball_paddle_collision(self.ball, self.opponent.paddle)

            collision.top_bottom_collision(self.ball, self.win)

            pygame.display.update()