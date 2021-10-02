import characters
import pygame
import os
import random
import sys

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP, K_x, K_z



pygame.font.init()
#pygame.mixer.init()

WIDTH, HEIGHT = 500, 500
flags = 0

WIN = pygame.display.set_mode((WIDTH, HEIGHT),flags)

pygame.display.set_caption("TBS Crossover Arena")

DIR_PATH = os.path.dirname(os.path.abspath(__file__))



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0,8,53)

FONT_MENU = pygame.font.SysFont('consolas', 25)
FONT_STAT = pygame.font.SysFont('consolas', 10)
FONT_TEXT = pygame.font.SysFont('consolas', 10)
FONT_SKILL = pygame.font.SysFont('consolas', 10, bold=True, italic=False)
FONT_PASSIVE = pygame.font.SysFont('consolas', 10, bold=True, italic=False)
FONT_ATT = pygame.font.SysFont('consolas', 10, bold=False, italic=True)
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
    icon = pygame.transform.scale(ICON, (64,64))
    WIN.blit(icon,(x+18,y+36))
    icon = pygame.transform.scale(char.image, (64,64))
    WIN.blit(icon,(x+18,y+36))
    Label(FONT_STAT,f"{char.name}",WHITE,(x+2,y+1),"topleft").draw(WIN)
    Label(FONT_STAT,f"Slot {slot+1}",WHITE,(x+2,y+11),"topleft").draw(WIN)
    Label(FONT_STAT,f"HP {char.hp}/{char.maxHp}",WHITE,(x+2,y+134),"bottomleft").draw(WIN)
    Label(FONT_STAT,f"SP {char.sp}/{char.maxSp}",WHITE,(x+98,y+134),"bottomright").draw(WIN)
    Label(FONT_STAT,f"DEF {char.dfn}",WHITE,(x+2,y+124),"bottomleft").draw(WIN)
    Label(FONT_STAT,f"RES {char.res}",WHITE,(x+2,y+113),"bottomleft").draw(WIN)
    Label(FONT_STAT,f"SPD {char.spd}",WHITE,(x+98,y+123),"bottomright").draw(WIN)
    Label(FONT_STAT,f"EVA {char.eva}",WHITE,(x+98,y+113),"bottomright").draw(WIN)


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

            WIN.blit(HIGHER_BOX,(25,25))

                #Player 1
            panel(35,180,0,p1())
            panel(145,180,1,p1())
            panel(255,180,2,p1())
            panel(365,180,3,p1())

                #Player 2
            panel(365,35,0,p2())
            panel(255,35,1,p2())
            panel(145,35,2,p2())
            panel(35,35,3,p2())
            

            WIN.blit(LOWER_BOX,(25,350))
            WIN.blit(BUTTON_OUTLINE, (-115+(x_gui*150),297+(y_gui*62)))

            WIN.blit(BUTTON,(37,362))
            Label(FONT_MENU,"Skill",WHITE,(45, 370)).draw(WIN)
            WIN.blit(BUTTON,(187,362))
            Label(FONT_MENU,"Rally",WHITE,(195, 370)).draw(WIN)
            WIN.blit(BUTTON,(337,362))
            Label(FONT_MENU,"Swap",WHITE,(345,370)).draw(WIN)
            WIN.blit(BUTTON,(37,425))
            Label(FONT_MENU,"Check",WHITE,(45,432)).draw(WIN)
            WIN.blit(BUTTON,(187,425))
            Label(FONT_MENU,"Scout",WHITE,(195,432)).draw(WIN)
            WIN.blit(BUTTON,(337,425))
            Label(FONT_MENU,"Order",WHITE,(345,432)).draw(WIN)

        
        if menu == 2 or menu == 3 or menu == 4:
            #Varibles
            y_limit_lower = 1
            y_limit_upper = 3

            x_limit_lower = 1
            x_limit_upper = 4

        
            #Background
            WIN.blit(BACKGROUND,(0,0))
            WIN.blit(BOX,(25,25))
            
            #Outline
            WIN.blit(PANEL2_OUTLINE,(-77+(x_gui*110),-115+(y_gui*147)))

            
            #Panels
            if menu == 2 or menu == 4:
                panels([35,145,255,365],[35,182,330],p1())

            if menu == 3:
                panels([35,145,255,365],[35,182,330],p2())

        if menu == 5:
            y_limit_lower = 1
            y_limit_upper = 8

            x_limit_lower = 1
            x_limit_upper = 1

            WIN.blit(BACKGROUND,(0,0))
            WIN.blit(BOX,(25,25))
            WIN.blit(BAR_OUTLINE,(32,-22+(y_gui*55)))
            
            for x in range(8):
                WIN.blit(BAR,(35,35+(x*55)))
                WIN.blit(ICON,(36,46+(x*55)))
                speedList = speedOrder(inFront())
                WIN.blit(speedList[x].image,(36,46+(x*55)))
                Label(FONT_STAT,f"{speedList[x].name}",WHITE,(35,35+(x*55)),"topleft").draw(WIN)

        if menu == 6 or menu == 7:
            if menu == 6:
                char = current
            WIN.blit(BACKGROUND,(0,0))
            WIN.blit(BOX,(25,25))
            WIN.blit(BOX_FILL,(27,27)) #(260,55)
            panel(27,27,char.slot,p1())
            y_limit_lower = 1
            x_limit_lower = 1
            x_limit_upper = 1
            y_limit_upper = char.skills
            
            line = 1
            for x in range(char.passives):
                y = open(f"{DIR_PATH}/characters/{char.name}/passive{x}.txt","r",encoding='utf-8')
                y = y.readlines()
                first = True
                for z in y:
                    z = z.replace("\n","")
                    if first == True:
                        font = FONT_PASSIVE
                        first =False
                    else: 
                        font = FONT_STAT
                    Label(font,f"{z}",WHITE,(130,17+(10*line)),"topleft").draw(WIN)
                    line += 1

            line = 1
            for x in range(char.skills):
                y = open(f"{DIR_PATH}/characters/{char.name}/skill{x}.txt","r",encoding='utf-8')
                y = y.readlines()
                first = True
                for z in y:
                    z = z.replace("\n","")
                    if first == True:
                        font = FONT_SKILL
                        if menu == 6:
                            skill_indention = sel(x+1)
                        else:
                            skill_indention = ""
                        first = False
                    else:
                        font = FONT_STAT
                        skill_indention = ""
                    Label(font,f"{skill_indention}{z}",WHITE,(28,155+(10*line)),"topleft").draw(WIN)
                    line += 1


        
        
            
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
                    if menu == 6:
                        if y_gui == 1:
                            
                            pass
                        if y_gui == 1:
                            pass
                        pass
                if event.key == K_x:
                    if menu == 2 or menu == 3 or menu == 4 or menu == 5 or menu == 6:
                        menu = 1
                        x_gui= 1
                        y_gui= 1

        
        pygame.display.update()


                


                

   

main()

