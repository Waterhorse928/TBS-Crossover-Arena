import pygame
import os
import sys
import battle
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TBS Crossover Arena")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_BLUE = (0,8,53)

FONT = pygame.font.SysFont('consolas', 50)

CHEN_IMAGE = pygame.image.load(os.path.join('images', 'chen-trimmy.png'))
BACKGROUND = pygame.image.load(os.path.join('images', 'Background.png'))
BOX = pygame.image.load(os.path.join('images', 'box.png'))
LOWER_BOX = pygame.image.load(os.path.join('images', 'lower_box2.png'))
HIGHER_BOX = pygame.image.load(os.path.join('images', 'higher_box.png'))
BUTTON = pygame.image.load(os.path.join('images', 'button.png'))

FPS = 60

def text(t, pos, color):
    WIN.blit (FONT.render(t,0,color), pos)

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        WIN.blit(BACKGROUND,(0,0))
        WIN.blit(LOWER_BOX,(50,700))
        WIN.blit(HIGHER_BOX,(50,50))
        WIN.blit(BUTTON,(75,725))
        WIN.blit(BUTTON,(375,725))
        WIN.blit(BUTTON,(675,725))
        WIN.blit(BUTTON,(75,850))
        WIN.blit(BUTTON,(375,850))
        WIN.blit(BUTTON,(675,850))
        text("Skill 1", (90, 740), WHITE)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                print (f"{0}: You pressed {event.key}")
            if event.type == pygame.KEYUP:
                print (f"{0}: You released {event.key}")
            

main()

