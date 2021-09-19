import pygame
import os
import battle
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TBS Crossover Arena")

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)

FONT = pygame.font.SysFont('consolas', 20)

FPS = 60

def text(t, pos, color):
    WIN.blit (FONT.render(t,0,color), pos)

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        text("test",(10,10),WHITE)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


main()

