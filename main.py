import characters
import os
import random
import sys




DIR_PATH = os.path.dirname(os.path.abspath(__file__))




FPS = 60

player1 = [characters.Momiji(),characters.Momiji(),characters.Momiji(),characters.Momiji(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen()]
player2 = [characters.Momiji(),characters.Momiji(),characters.Momiji(),characters.Momiji(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen(),characters.Chen()]
turn = 1
round = 0
menu = 1
current = 0
gamemode = 0
partysize = 0
players = 0
wikiList = ["Momiji","Aya"]






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

#Menus
#1 Action Select
#2 Check
#3 Scout
#4 Swap
#5 Speed Order
#6 Choose Skill
#7 Character Info

def numberSelect(min,max):
    while True:
        try:
            x = int(input("Choose a number: "))
            if x >= min and x <= max:
                break
            if x < min:
                print("Error: Number too low.")
            if x > max:
                print("Error: Number too high.")
        except ValueError:
            print("Error: Not a integer.")
    return x

def wikiCharacterSelect():
    while True:
        try:
            x = str(input("Choose a character: "))
            if x in wikiList:
                break
            else:
                print("Error: Invalid.")
            
        except ValueError:
            print("Error: Invalid.")
    return x

def gameModeSelect():
    global gamemode
    print("Select a gamemode\n1. Duel")
    gamemode = numberSelect(1,1)
    

def playerNumberSelect():
    global players
    if gamemode == 1:
        players = 2
        
    

def partySizeSelect():
    global partysize
    print("Select party size")
    partysize = numberSelect(8,12)

def startCharacterSelect():
    for x in range(0, players):
        for y in range(0, partysize):
            print(f"Player {x+1} Slot {y+1}")
            print (wikiCharacterSelect())

    
    

def main():
    global menu, round, turn, current, gamemode, partysize, players
    gameModeSelect()
    playerNumberSelect()
    partySizeSelect()
    startCharacterSelect()


    

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
        

        

        for x in range(current.passives):
            y = open(f"{DIR_PATH}/characters/{current.name}/passive{x}.txt","r",encoding='utf-8')
            y = y.readlines()
            


        for x in range(current.skills):
            y = open(f"{DIR_PATH}/characters/{current.name}/skill{x}.txt","r",encoding='utf-8')
            y = y.readlines()
            


        
        
            


   


                


                

   

main()

