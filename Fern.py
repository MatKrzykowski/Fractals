# Fern.py
#
# Script inspired by "Chaos Game - Numberphile" on YouTube
# https://www.youtube.com/watch?v=kbKtFN71Lfs
#
# https://en.wikipedia.org/wiki/Barnsley_fern
#
# Changelog:
# 12.08.2017 - Script created based on Chaos_Game.py
# 26.09.2017 - Script clean-up

# Import mathematical libraries
import random

# Import graphical libraries
import pygame
import sys
from pygame.locals import QUIT

WIDTH, HEIGHT = 800, 600  # Size of the window


class particle:

    def __init__(self, x, y, color=(0, 255, 0)):
        self.x = x
        self.y = y
        self.color = color

    def step(self):
        i = random.random()
        if i < 0.01:
            self.x, self.y = 0, 0.16 * self.y
        elif i < 0.86:
            self.x, self.y = 0.85 * self.x + 0.04 * \
                self.y, -0.04 * self.x + 0.85 * self.y + 1.6
        elif i < 0.93:
            self.x, self.y = 0.2 * self.x - 0.26 * \
                self.y, 0.23 * self.x + 0.22 * self.y + 1.6
        else:
            self.x, self.y = -0.15 * self.x + 0.28 * \
                self.y, 0.26 * self.x + 0.24 * self.y + 0.44

    def draw_point(self, screen):
        screen.set_at((int(400 + 100 * self.x),
                       int(HEIGHT - self.y * HEIGHT / 10)), self.color)

if __name__ == "__main__":
    pygame.init()  # Initialize pygame

    FPS = 60  # Frames per second
    fpsClock = pygame.time.Clock()  # Clock initialization

    fontsize = 18

    # Prepare the display
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    pygame.display.set_caption('Chaos Game')

    # Prepare print of the text
    fontObj = pygame.font.Font('freesansbold.ttf', fontsize)
    textSurfaceObj = fontObj.render('', True, (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()

    point = particle(0, 0)

    DISPLAYSURF.fill((255, 255, 255))  # Clear the surface

    # Draw the simulation
    while True:
        for i in range(100):
            point.step()
            point.draw_point(DISPLAYSURF)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FPS)
