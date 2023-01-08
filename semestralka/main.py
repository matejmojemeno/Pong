"""main file"""

import pygame
from pong import Application

#window resolution
WIN_WIDTH = 1280
WIN_HEIGHT = 720

#create game window
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

#run the application
app = Application(win)
app.run()
