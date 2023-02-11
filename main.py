import characters
import random
import math
from characters import wikiList

teamPickMode = 0
playerA = ["Player A","","","","","","","",""]
playerB = ["Player B","","","","","","","",""]
thueMorse = [0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0]

def ask (lowRange,highRange):
    while True:
        try:
            result = int(input(""))
        except:
            continue
        if lowRange <= result <= highRange:
            return result
        
def askList (numberList):
    while True:
        try:
            result = int(input(""))
        except:
            continue
        if result in numberList:
            return result

def listPick (player):
    wikiListTaken = [*range(1,len(wikiList))]
    for y in range(1,9):
        print(f"{player[0]}: Choose a character")
        for x in wikiListTaken:
            print(f"{x}. {wikiList[x].name}")
        n = askList(wikiListTaken)
        wikiListTaken.remove(n)
        player[y] = wikiList[n]
        print (f"Selected {player[y].name}")
    return player

def draftPick ():
    wikiListTakenA = [*range(1,len(wikiList))]
    wikiListTakenB = [*range(1,len(wikiList))]
    a = 1
    b = 1
    for y in thueMorse:
        if y == 0:
            print(f"{playerA[0]}: Choose a character")
            for x in wikiListTakenA:
                print(f"{x}. {wikiList[x].name}")
            n = askList(wikiListTakenA)
            wikiListTakenA.remove(n)
            playerA[a] = wikiList[n]
            print (f"Selected {playerA[a].name}")
            a += 1
        elif y == 1:
            print(f"{playerB[0]}: Choose a character")
            for x in wikiListTakenB:
                print(f"{x}. {wikiList[x].name}")
            n = askList(wikiListTakenB)
            wikiListTakenB.remove(n)
            playerB[b] = wikiList[n]
            print (f"Selected {playerB[b].name}")
            b += 1
        
def slotOrder (player):
    playerListTaken = [*range(1,9)]
    result = [player[0]]
    for y in range(1,9):
        print(f'Choose a character for Slot {y}')
        for x in playerListTaken:
            print(f"{x}. {player[x].name}")
        n = askList(playerListTaken)
        playerListTaken.remove(n)
        result[y] = player[n]
        print (f"Selected {result[y].name} for Slot {y}")
    return result
    
def checkTeams():
    print(f'{"Player A": <{20}}{"Player B": <{20}}')
    for x in range(1,9):
        print(f'{str(x) + ". " + playerA[x].name: <{20}}{str(x) + ". " + playerB[x].name: <{20}}')


# Team Pick        
print ("-Team Pick-\n 1. Draft\n 2. List")
print (f'{"---Team Pick---": ^{40}}\n{"1. Draft": ^{20}}{"2. List": ^{20}}')
teamPickMode = ask(1,2)   
if teamPickMode == 1:
    draftPick()     
elif teamPickMode == 2:
    playerA = listPick(playerA)
    playerB = listPick(playerB)
checkTeams()

# Slot Order
playerA = slotOrder(playerA)
playerB = slotOrder(playerB)
checkTeams()

