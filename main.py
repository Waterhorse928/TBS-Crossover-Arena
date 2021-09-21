import pygame
import os
import sys

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
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
BUTTON_OUTLINE = pygame.image.load(os.path.join('images', 'button_outline.png'))

FPS = 60

def text(t, pos, color):
    WIN.blit (FONT.render(t,0,color), pos)




def main():
    clock = pygame.time.Clock()
    run = True
    x = 1
    y = 1
    menu = 1
    while run:
        clock.tick(FPS)

        if menu == 1:
            #Varibles
            y_limit_lower = 1
            y_limit_upper = 2

            x_limit_lower = 1
            x_limit_upper = 3

            #Display
            WIN.blit(BACKGROUND,(0,0))
    
            WIN.blit(LOWER_BOX,(50,700))
            WIN.blit(HIGHER_BOX,(50,50))
    
            if y == 1 and x == 1:
                WIN.blit(BUTTON_OUTLINE, (70,720))
            WIN.blit(BUTTON,(75,725))
            text("Skill", (90, 740), WHITE)
    
            if y == 1 and x == 2:
                WIN.blit(BUTTON_OUTLINE, (370,720))
            WIN.blit(BUTTON,(375,725))
    
            if y == 1 and x == 3:
                WIN.blit(BUTTON_OUTLINE, (670,720))
            WIN.blit(BUTTON,(675,725))
            
            if y == 2 and x == 1:
                WIN.blit(BUTTON_OUTLINE, (70,845))
            WIN.blit(BUTTON,(75,850))
    
            if y == 2 and x == 2:
                WIN.blit(BUTTON_OUTLINE, (370,845))
            WIN.blit(BUTTON,(375,850))
    
            if y == 2 and x == 3:
                WIN.blit(BUTTON_OUTLINE, (670,845))
            WIN.blit(BUTTON,(675,850))

            pygame.display.update()
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    y += 1
                    if y > y_limit_upper:
                        y = y_limit_lower
                if event.key == K_UP:
                    y -= 1
                    if y < y_limit_lower:
                        y = y_limit_upper
                if event.key == K_RIGHT:
                    x += 1
                    if x > x_limit_upper:
                        x = x_limit_lower
                if event.key == K_LEFT:
                    x -= 1
                    if x < x_limit_lower:
                        x = x_limit_upper


                
            
            

main()

