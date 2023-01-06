from paddle import Paddle
from stamina import Stamina

class Player:
    def __init__(self, win, left):
        self.paddle = Paddle(left, 0, 0, win)
        self.stamina = Stamina(1000)


    def handle_stamina(self, shift, up, down):
        if shift and up or shift and down:
            self.paddle.sprint(is_sprinting=True)
            self.stamina.decrease()
        else:
            self.stamina.increase()


    def move(self, up, down, win):
        if up:
            self.paddle.move(up, win)
        if down:
            self.paddle.move(down, win)


    def handle_movement(self, shift, up, down, win):
        #playes is trying to move up and down so he stays in the same place
        if up and down:
            return
        
        self.handle_stamina(shift, up, down)
        self.move(up, down, win)
