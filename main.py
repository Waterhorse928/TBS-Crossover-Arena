from io import TextIOBase
import characters
import os
import random
import sys

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

# -Global Varibles-

turn = 1
round = 0
menu = 1
current = 0
gamemode = 0
partysize = 0
players = 0
wikiList = ["Momiji","Aya"]








# -Functions-

# Ask the player to choose a number and returns it
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

# Ask the player to a character from the wiki and returns it
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

# Ask the player to choose a gamemode
def gameModeSelect():
    global gamemode
    print("Select a gamemode\n1. Duel")
    gamemode = numberSelect(1,1)

# sets how many players. skips asking for input if unessasary
def playerNumberSelect():
    global players
    if gamemode == 1:
        players = 2
        
# Ask the player to choose the party size. skips asking for input if unessasary 
def partySizeSelect():
    global partysize
    if gamemode == 1:
        print("Select party size")
        partysize = numberSelect(1,12)

# calls the global player dictonaries. use number to select which player.
def player(number):
    x = "player" + str(number)
    x = globals()[x]
    return x

# sets up global player dictonaries.
def setUpPlayerDict():
    for x in range(0, players):
        player = "player" + str(x)
        globals()[player] = {}



# I need to turn the strings in the player dicts into the classes from characters




# Asks and inputs player slots in order.
def startCharacterSelect():
    for x in range(0, players):
        for y in range(0, partysize):
            print(f"Player {x+1} Slot {y+1}")
            player(x)[y] = wikiCharacterSelect()


# gets key from dict using value
def getKey(d,v):
    for key, value in d.items():
        if v == value:
            return key

#updates current slot numbers on characters (WIP)
def refreshSlot():
    for y in range(0,players):
        for x in range(0, partysize):
            break
            player(y)[x].slot = getKey(player(y),player(y)[x])
            print (x.slot)

#returns a list of character in front
def inFront():
    l = []
    for x in range(0, players):
        for y in range(0, partysize):
            l.append (player(x)[y])
    return l

#sorts list by Spd, Slot, randomly.
def speedOrder(l):
    refreshSlot()
    random.shuffle(l)
    l.sort(key=lambda x : x.slot)
    l.sort(key=lambda x : -x.spd)
    return l


    
# -MAIN-

def main():
    global menu, round, turn, current, gamemode, partysize, players
    gameModeSelect()
    playerNumberSelect()
    partySizeSelect()
    setUpPlayerDict()
    startCharacterSelect()
    battleOver = False
    while battleOver == False:
        refreshSlot()
        print (inFront())
        break


main()

