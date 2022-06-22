# Chaos_Game.py
#
# Script inspired by "Chaos Game - Numberphile" on YouTube
# https://www.youtube.com/watch?v=kbKtFN71Lfs
#
# Changelog:
# 08.08.2017 - Script created
# 12.08.2017 - Point drawing method changed

import numpy as np  # Import math modules
import random

# Libraries import
import pygame
import sys
import pygame.gfxdraw
from pygame.locals import *

WIDTH, HEIGHT = 800, 600  # Size of the window

class particle:
    def __init__(self, x, y, color=(200, 0, 255), radius=10):
        self.x = int(x)
        self.y = int(y)
        self.color = color
        self.radius = radius

    def intpos(self):
        return (self.x, self.y)

    def draw_particle(self, screen):
        pygame.draw.circle(screen, self.color, self.intpos(), self.radius)
        pygame.gfxdraw.aacircle(screen, *self.intpos(), self.radius, self.color)

    def chaos_step(self, other):
        self.x = (self.x + other.x) // 2
        self.y = (self.y + other.y) // 2

    def draw_point(self, screen):
        screen.set_at((self.x, self.y), self.color)
        #pygame.gfxdraw.pixel(screen, self.x, self.y, self.color)
        #screen.fill(self.color, ((self.x, self.y), (1, 1)))

def draw_FPS(screen):
    textSurfaceObj = fontObj.render("FPS: " + str(round(fpsClock.get_fps(), 1)),
                                    True, (0, 0, 0))
    textRectObj.topright = (699, 0)
    screen.blit(textSurfaceObj, textRectObj)

triangle = [
    particle(15, 15),
    particle(WIDTH-15, 15),
    particle(WIDTH//2, HEIGHT-15)
]

triangle_with_middle = [
    particle(15, 15),
    particle(WIDTH-15, 15),
    particle(WIDTH//2, HEIGHT-15),
    particle(WIDTH//2, HEIGHT//2)
]

square = [
    particle(15, 15),
    particle(WIDTH-15, 15),
    particle(15, HEIGHT-15),
    particle(WIDTH-15, HEIGHT-15)
]

triangle1 = [
    particle(15, HEIGHT*3//5),
    particle(WIDTH*5//11, HEIGHT*8//10),
    particle(WIDTH*4//11, HEIGHT*7//10)
]

triangle2 = [
    particle(WIDTH-15, HEIGHT*3//4-15, color=(0,255,0)),
    particle(WIDTH//2, HEIGHT-15, color=(0,255,0)),
    particle(WIDTH-15, 15, color=(0,255,0))
]

pentagon = [particle(300+300*np.sin(i*2*np.pi/5),300+300*np.cos(i*2*np.pi/5)) for i in range(5)]
equ_triangle = [particle(300+300*np.sin(i*2*np.pi/3),300+300*np.cos(i*2*np.pi/3)) for i in range(3)]
decagon = [particle(300+300*np.sin(i*2*np.pi/10),300+300*np.cos(i*2*np.pi/10)) for i in range(10)]
hexagon = [particle(300+300*np.sin(i*2*np.pi/6),300+300*np.cos(i*2*np.pi/6)) for i in range(6)]
octagon = [particle(300+300*np.sin(i*2*np.pi/8),300+300*np.cos(i*2*np.pi/8)) for i in range(8)]

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

    items = octagon
    alt_items = []

    is_alt_items = False

    point = particle(WIDTH//2, HEIGHT//2, color=(20, 0, 0))

    DISPLAYSURF.fill((255, 255, 255))  # Clear the surface

    # Draw all particles
    for item in items + alt_items:
        item.draw_particle(DISPLAYSURF)

    # Draw the simulation
    while True:
        #draw_FPS(DISPLAYSURF)  # Write the FPS text

        for i in range(100):
            if is_alt_items:
                point.chaos_step(alt_items[random.choice([j for j in range(len(alt_items))])])
                point.draw_point(DISPLAYSURF)
            else:
                point.chaos_step(items[random.choice([j for j in range(len(items))])])
                point.draw_point(DISPLAYSURF)
            if alt_items:
                if random.random() < 0.85:
                    is_alt_items = not is_alt_items

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FPS)
