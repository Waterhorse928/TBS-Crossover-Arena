import characters
import pygame
import os
import random
import sys

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP, K_x, K_z



pygame.font.init()
#pygame.mixer.init()

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
FONT_TEXT = pygame.font.SysFont('consolas', 20)
FONT_SKILL = pygame.font.SysFont('consolas', 20, bold=True, italic=False)
FONT_PASSIVE = pygame.font.SysFont('consolas', 20, bold=True, italic=False)
FONT_ATT = pygame.font.SysFont('consolas', 20, bold=False, italic=True)
FONT_PASSIVE.underline = True

BACKGROUND = pygame.image.load(os.path.join('images', 'Background.png'))
BOX = pygame.image.load(os.path.join('images', 'box.png'))
BOX_FILL = pygame.image.load(os.path.join('images', 'box_fill.png'))
LOWER_BOX = pygame.image.load(os.path.join('images', 'lower_box2.png'))
HIGHER_BOX = pygame.image.load(os.path.join('images', 'higher_box.png'))
BUTTON = pygame.image.load(os.path.join('images', 'button.png'))
BUTTON_OUTLINE = pygame.image.load(os.path.join('images', 'button_outline.png'))
PANEL = pygame.image.load(os.path.join('images', 'panel.png'))
PANEL2 = pygame.image.load(os.path.join('images', 'panel2.png'))
PANEL2_OUTLINE = pygame.image.load(os.path.join('images', 'panel2_outline.png'))
PANEL2_OUTLINE2 = pygame.image.load(os.path.join('images', 'panel2_outline2.png'))
BAR = pygame.image.load(os.path.join('images', 'bar.png'))
ICON = pygame.image.load(os.path.join('images', 'icon.png'))
BAR_OUTLINE = pygame.image.load(os.path.join('images', 'bar_outline.png'))

FPS = 60

player1 = [characters.Momiji(),characters.Momiji(),characters.Momiji(),characters.Momiji(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen()]
player2 = [characters.Momiji(),characters.Momiji(),characters.Momiji(),characters.Momiji(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen()]
turn = 1
round = 0
menu = 1
x_gui= 1
y_gui= 1
current = 0

class Label:
    def __init__(self, font, text, color, position, anchor="topleft"):
        self.image = font.render(text, 1, color)
        self.rect = self.image.get_rect()
        setattr(self.rect, anchor, position)
        #print(self.rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def panel(x,y,slot,player):
    char = player[slot]
    if char == current:
        WIN.blit(PANEL2_OUTLINE2,(x-1,y-1))
    WIN.blit(PANEL2,(x,y))
    icon = pygame.transform.scale(ICON, (128,128))
    WIN.blit(icon,(x+36,y+71))
    icon = pygame.transform.scale(char.image, (128,128))
    WIN.blit(icon,(x+36,y+71))
    Label(FONT_STAT,f"{char.name}",WHITE,(x+1,y+1),"topleft").draw(WIN)
    Label(FONT_STAT,f"Slot {slot+1}",WHITE,(x+1,y+22),"topleft").draw(WIN)
    Label(FONT_STAT,f"HP {char.hp}/{char.maxHp}",WHITE,(x+1,y+269),"bottomleft").draw(WIN)
    Label(FONT_STAT,f"SP {char.sp}/{char.maxSp}",WHITE,(x+199,y+269),"bottomright").draw(WIN)
    Label(FONT_STAT,f"DEF {char.dfn}",WHITE,(x+1,y+248),"bottomleft").draw(WIN)
    Label(FONT_STAT,f"RES {char.res}",WHITE,(x+1,y+227),"bottomleft").draw(WIN)
    Label(FONT_STAT,f"SPD {char.spd}",WHITE,(x+199,y+248),"bottomright").draw(WIN)
    Label(FONT_STAT,f"EVA {char.eva}",WHITE,(x+199,y+227),"bottomright").draw(WIN)


def panels(x_pixels, y_pixels, player):
    if player == p1():
        number = 0
        for y in range(len(y_pixels)):
            for x in range(len(x_pixels)):
                panel (x_pixels[x],y_pixels[y],number,player)
                number += 1
    if player == p2():
        number = len(x_pixels) * len(y_pixels)
        for y in range(len(y_pixels)):
            for x in range(len(x_pixels)):
                number -= 1
                panel (x_pixels[x],y_pixels[y],number,player)

def p1():
    if turn == 1:
        return player1
    if turn == 2:
        return player2

def p2():
    if turn == 1:
        return player2
    if turn == 2:
        return player1

#sorts list by Spd, Slot, randomly.
def speedOrder(l):
    refreshSlot()
    random.shuffle(l)
    l.sort(key=lambda x : x.slot)
    l.sort(key=lambda x : -x.spd)
    return l

#returns a list of character in front
def inFront():
    l = [player1[0],player1[1],player1[2],player1[3],player2[0],player2[1],player2[2],player2[3]]
    return l

#Removes characters that have taken an action
def removeAction(l):
    l2 = l.copy()
    for x in l2:
        if x.action == False:
            l.remove(x)
    return l

#Removes KOed Character from a list
def removeKO(l):
    l2 = l.copy()
    for x in l2:
        if x.KO == True:
            l.remove(x)
    return l


def actionsLeft():
    l = inFront()
    l = removeKO(l)
    actions = 0
    for x in l:
        if x.action == True:
            actions += 1
    return actions

#start a new round and set in front's actions to true
def newRound():
    for x in removeKO(inFront()):
                x.action = True
                print (f"{x.name}.action = True")
    global round
    round += 1
    print(f"Round {round}")

#update currnt slot number
def refreshSlot():
    for x in player1:
        x.slot = player1.index(x)
    for x in player2:
        x.slot = player2.index(x)

#Cursor for Info Screen
def sel(number):
    if number == y_gui:
        return "> "
    else:
        return "  "

#Menus
#1 Action Select
#2 Check
#3 Scout
#4 Swap
#5 Speed Order
#6 Choose Skill
#7 Character Info

def main():
    clock = pygame.time.Clock()
    run = True
    global menu, round, turn, x_gui, y_gui, current
    while run:
        clock.tick(FPS)
        refreshSlot()
        if current == 0  or current.action == False:
            if actionsLeft() == 0:
                newRound()
            current = speedOrder(removeAction(inFront()))[0]
            print (f"Current is {current.name}")
            if (current in player1):
                turn = 1 
            if (current in player2):
                turn = 2
            print (f"Turn = {turn}")
            

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
            panel(70,360,0,p1())
            panel(290,360,1,p1())
            panel(510,360,2,p1())
            panel(730,360,3,p1())

                #Player 2
            panel(730,70,0,p2())
            panel(510,70,1,p2())
            panel(290,70,2,p2())
            panel(70,70,3,p2())
            

            WIN.blit(LOWER_BOX,(50,700))
            WIN.blit(BUTTON_OUTLINE, (-230+(x_gui*300),595+(y_gui*125)))

            WIN.blit(BUTTON,(75,725))
            Label(FONT_MENU,"Skill",WHITE,(90, 740)).draw(WIN)
    

            WIN.blit(BUTTON,(375,725))
            Label(FONT_MENU,"Rally",WHITE,(390, 740)).draw(WIN)


            WIN.blit(BUTTON,(675,725))
            Label(FONT_MENU,"Swap",WHITE,(690,740)).draw(WIN)
            

            WIN.blit(BUTTON,(75,850))
            Label(FONT_MENU,"Check",WHITE,(90,865)).draw(WIN)
    

            WIN.blit(BUTTON,(375,850))
            Label(FONT_MENU,"Scout",WHITE,(390,865)).draw(WIN)
    

            WIN.blit(BUTTON,(675,850))
            Label(FONT_MENU,"Order",WHITE,(690,865)).draw(WIN)

        
        if menu == 2 or menu == 3 or menu == 4:
            #Varibles
            y_limit_lower = 1
            y_limit_upper = 3

            x_limit_lower = 1
            x_limit_upper = 4

        
            #Background
            WIN.blit(BACKGROUND,(0,0))
            WIN.blit(BOX,(50,50))
            
            #Outline
            WIN.blit(PANEL2_OUTLINE,(-155+(x_gui*220),-230+(y_gui*295)))

            
            #Panels
            if menu == 2 or menu == 4:
                panels([70,290,510,730],[70,365,660],p1())

            if menu == 3:
                panels([70,290,510,730],[70,365,660],p2())

        if menu == 5:
            y_limit_lower = 1
            y_limit_upper = 8

            x_limit_lower = 1
            x_limit_upper = 1

            WIN.blit(BACKGROUND,(0,0))
            WIN.blit(BOX,(50,50))
            WIN.blit(BAR_OUTLINE,(65,-45+(y_gui*110)))
            
            for x in range(8):
                WIN.blit(BAR,(70,70+(x*110)))
                WIN.blit(ICON,(73,93+(x*110)))
                speedList = speedOrder(inFront())
                WIN.blit(speedList[x].image,(73,93+(x*110)))
                Label(FONT_STAT,f"{speedList[x].name}",WHITE,(71,71+(x*110)),"topleft").draw(WIN)

        if menu == 6 or menu == 7:
            WIN.blit(BACKGROUND,(0,0))
            WIN.blit(BOX,(50,50))
            WIN.blit(BOX_FILL,(55,55)) #(260,55)
            panel(55,55,current.slot,p1())
            line = 1
            if current.name == "Momiji":
                y_limit_lower = 1
                y_limit_upper = 2
                x_limit_lower = 1
                x_limit_upper = 1

                Label(FONT_PASSIVE,f"Ability to See Far Distances",WHITE,(261,35+(21*1)),"topleft").draw(WIN)
                Label(FONT_STAT,f"While this unit is on the front, all allies gain +2 ACC.",WHITE,(261,35+(21*2)),"topleft").draw(WIN)

                Label(FONT_SKILL,f"{sel(1)}Rabies Bite",WHITE,(56,310+(21*1)),"topleft").draw(WIN)
                Label(FONT_STAT,f"[ATK] Cost 1 SP",WHITE,(56,310+(21*2)),"topleft").draw(WIN)
                Label(FONT_STAT,f"One Enemy: [Pierce 3]",WHITE,(56,310+(21*3)),"topleft").draw(WIN)
                Label(FONT_STAT,f"This skill ignores 2 DEF.",WHITE,(56,310+(21*4)),"topleft").draw(WIN)

                Label(FONT_SKILL,f"{sel(2)}Expellee's Canaan",WHITE,(56,310+(21*5)),"topleft").draw(WIN)
                Label(FONT_STAT,f"[ATK] Cost 2 SP",WHITE,(56,310+(21*6)),"topleft").draw(WIN)
                Label(FONT_STAT,f"All Enemies: [Wind 4]",WHITE,(56,310+(21*7)),"topleft").draw(WIN)
                

            else:
                y_limit_lower = 1
                y_limit_upper = 1
                x_limit_lower = 1
                x_limit_upper = 1
                Label(FONT_PASSIVE,f"Passive",WHITE,(261,35+(21*1)),"topleft").draw(WIN)
                Label(FONT_STAT,f"Passive Text.",WHITE,(261,35+(21*2)),"topleft").draw(WIN)
                Label(FONT_SKILL,f"{sel(1)}1st Skill",WHITE,(56,310+(21*1)),"topleft").draw(WIN)
                Label(FONT_STAT,f"[?] Cost ?",WHITE,(56,310+(21*2)),"topleft").draw(WIN)

            

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
                    #Action Select
                    if menu == 1:
                        #Skill
                        if x_gui == 1 and y_gui == 1:
                            menu = 6
                            x_gui= 1
                            y_gui= 1 
                        #Rally
                        if x_gui == 2 and y_gui == 1:
                            current.action = False
                            current.sp += 3
                            if current.sp > current.maxSp:
                                current.sp = current.maxSp
                            x_gui= 1
                            y_gui= 1
                        #Swap
                        if x_gui == 3 and y_gui == 1:
                            menu = 4
                            x_gui= 1
                            y_gui= 1 
                        #Check
                        if x_gui== 1 and y_gui== 2:
                            menu = 2
                            x_gui= 1
                            y_gui= 1
                        #Scout
                        if x_gui== 2 and y_gui== 2:
                            menu = 3
                            x_gui= 4
                            y_gui= 3
                        #Order
                        if x_gui== 3 and y_gui== 2:
                            menu = 5
                            x_gui= 1
                            y_gui= 1
                if event.key == K_x:
                    if menu == 2 or menu == 3 or menu == 4 or menu == 5 or menu == 6:
                        menu = 1
                        x_gui= 1
                        y_gui= 1


                


                

   

main()

