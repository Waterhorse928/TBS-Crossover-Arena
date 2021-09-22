import pygame
import os
import sys

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP, K_x, K_z

import c
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
BLUE = (0, 0, 255)
DARK_BLUE = (0,8,53)

FONT_MENU = pygame.font.SysFont('consolas', 50)
FONT_STAT = pygame.font.SysFont('consolas', 20)

CHEN_IMAGE = pygame.image.load(os.path.join('images', 'chen-trimmy.png'))
BACKGROUND = pygame.image.load(os.path.join('images', 'Background.png'))
BOX = pygame.image.load(os.path.join('images', 'box.png'))
LOWER_BOX = pygame.image.load(os.path.join('images', 'lower_box2.png'))
HIGHER_BOX = pygame.image.load(os.path.join('images', 'higher_box.png'))
BUTTON = pygame.image.load(os.path.join('images', 'button.png'))
BUTTON_OUTLINE = pygame.image.load(os.path.join('images', 'button_outline.png'))
PANEL = pygame.image.load(os.path.join('images', 'panel.png'))
PANEL2 = pygame.image.load(os.path.join('images', 'panel2.png'))
PANEL2_OUTLINE = pygame.image.load(os.path.join('images', 'panel2_outline.png'))

FPS = 60

player1 = {1:c.characters.chen,2:c.characters.chen,3:c.characters.chen,4:c.characters.chen}
player2 = {1:c.characters.chen,2:c.characters.chen,3:c.characters.chen,4:c.characters.chen}

class Label:
    def __init__(self, font, text, color, position, anchor="topleft"):
        self.image = font.render(text, 1, color)
        self.rect = self.image.get_rect()
        setattr(self.rect, anchor, position)
        print(self.rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


def panel(x,y,pos,char):
    WIN.blit(PANEL2,(x,y))
    Label(FONT_STAT,f"POS {pos}",WHITE,(x+1,y+1),"topleft").draw(WIN)
    Label(FONT_STAT,f"Order {0}",WHITE,(x+199,y+1),"topright").draw(WIN)
    Label(FONT_STAT,f"HP {char.hp}/{char.maxHP}",WHITE,(x+1,y+269),"bottomleft").draw(WIN)
    Label(FONT_STAT,f"SP {10}/{10}",WHITE,(x+199,y+269),"bottomright").draw(WIN)

def main():
    clock = pygame.time.Clock()
    run = True
    x_gui= 1
    y_gui= 1
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

            WIN.blit(HIGHER_BOX,(50,50))

                #Player 1
            panel(70,360,1,player1(1))
            panel(290,360,2,player1(2))
            panel(510,360,3,player1(3))
            panel(730,360,4,player1(4))

                #Player 2
            panel(730,70,1,player2(1))
            panel(510,70,2,player2(2))
            panel(290,70,3,player2(3))
            panel(70,70,4,player2(4))
            
            

            WIN.blit(LOWER_BOX,(50,700))
    
            if y_gui== 1 and x_gui== 1:
                WIN.blit(BUTTON_OUTLINE, (70,720))
            WIN.blit(BUTTON,(75,725))
            Label(FONT_MENU,"Skill",WHITE,(90, 740)).draw(WIN)
    
            if y_gui== 1 and x_gui== 2:
                WIN.blit(BUTTON_OUTLINE, (370,720))
            WIN.blit(BUTTON,(375,725))
            Label(FONT_MENU,"Rally",WHITE,(390, 740)).draw(WIN)
    
            if y_gui== 1 and x_gui== 3:
                WIN.blit(BUTTON_OUTLINE, (670,720))
            WIN.blit(BUTTON,(675,725))
            Label(FONT_MENU,"Swap",WHITE,(690,740)).draw(WIN)
            
            if y_gui== 2 and x_gui== 1:
                WIN.blit(BUTTON_OUTLINE, (70,845))
            WIN.blit(BUTTON,(75,850))
            Label(FONT_MENU,"Info",WHITE,(90,865)).draw(WIN)
    
            if y_gui== 2 and x_gui== 2:
                WIN.blit(BUTTON_OUTLINE, (370,845))
            WIN.blit(BUTTON,(375,850))
            Label(FONT_MENU,"Scout",WHITE,(390,865)).draw(WIN)
    
            if y_gui== 2 and x_gui== 3:
                WIN.blit(BUTTON_OUTLINE, (670,845))
            WIN.blit(BUTTON,(675,850))
            Label(FONT_MENU,"Order",WHITE,(690,865)).draw(WIN)

            pygame.display.update()
        
        if menu == 2 or menu == 3:
            #Varibles
            y_limit_lower = 1
            y_limit_upper = 3

            x_limit_lower = 1
            x_limit_upper = 4

            #Display
            WIN.blit(BACKGROUND,(0,0))
            WIN.blit(BOX,(50,50))
            if y_gui== 1 and x_gui== 1:
                WIN.blit(PANEL2_OUTLINE,(65,65))
            WIN.blit(PANEL2,(70,70))
            if y_gui== 1 and x_gui== 2:
                WIN.blit(PANEL2_OUTLINE,(285,65))
            WIN.blit(PANEL2,(290,70))
            if y_gui== 1 and x_gui== 3:
                WIN.blit(PANEL2_OUTLINE,(505,65))
            WIN.blit(PANEL2,(510,70))
            if y_gui== 1 and x_gui== 4:
                WIN.blit(PANEL2_OUTLINE,(725,65))
            WIN.blit(PANEL2,(730,70))
            if y_gui== 2 and x_gui== 1:
                WIN.blit(PANEL2_OUTLINE,(65,360))
            WIN.blit(PANEL2,(70,365))
            if y_gui== 2 and x_gui== 2:
                WIN.blit(PANEL2_OUTLINE,(285,360))
            WIN.blit(PANEL2,(290,365))
            if y_gui== 2 and x_gui== 3:
                WIN.blit(PANEL2_OUTLINE,(505,360))
            WIN.blit(PANEL2,(510,365))
            if y_gui== 2 and x_gui== 4:
                WIN.blit(PANEL2_OUTLINE,(725,360))
            WIN.blit(PANEL2,(730,365))
            if y_gui== 3 and x_gui== 1:
                WIN.blit(PANEL2_OUTLINE,(65,655))
            WIN.blit(PANEL2,(70,660))
            if y_gui== 3 and x_gui== 2:
                WIN.blit(PANEL2_OUTLINE,(285,655))
            WIN.blit(PANEL2,(290,660))
            if y_gui== 3 and x_gui== 3:
                WIN.blit(PANEL2_OUTLINE,(505,655))
            WIN.blit(PANEL2,(510,660))
            if y_gui== 3 and x_gui== 4:
                WIN.blit(PANEL2_OUTLINE,(725,655))
            WIN.blit(PANEL2,(730,660))

            pygame.display.update()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    y_gui+= 1
                    if y_gui> y_limit_upper:
                        y_gui= y_limit_lower
                if event.key == K_UP:
                    y_gui-= 1
                    if y_gui< y_limit_lower:
                        y_gui= y_limit_upper
                if event.key == K_RIGHT:
                    x_gui+= 1
                    if x_gui> x_limit_upper:
                        x_gui= x_limit_lower
                if event.key == K_LEFT:
                    x_gui-= 1
                    if x_gui< x_limit_lower:
                        x_gui= x_limit_upper
                if event.key == K_z:
                    if menu == 1:
                        if x_gui== 1 and y_gui== 2:
                            menu = 2
                            x_gui= 1
                            y_gui= 1
                        if x_gui== 2 and y_gui== 2:
                            menu = 3
                            x_gui= 4
                            y_gui= 3
                if event.key == K_x:
                    if menu == 2 or menu == 3:
                        menu = 1
                        x_gui= 1
                        y_gui= 1


                


                
            
            

main()

