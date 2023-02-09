import characters
import random
import math
from characters import wikiList

teamPickMode = 0
playerA = ["Player A","","","","","","","",""]
playerB = ["Player B","","","","","","","",""]

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
        
print ("-Team Pick-\n 1. Draft\n 2. List")
teamPickMode = ask(1,2)   

if teamPickMode == 1:
    wikiListA = [*range(1,len(wikiList))]
    for y in range(1,9):
        print("Player A: Choose a character")
        for x in wikiListA:
            print(f"{x}. {wikiList[x].name}")
        n = askList(wikiListA)
        wikiListA.remove(n)
        playerA[y] = wikiList[n]
        print (f"Selected {playerA[y].name}")
    for x in playerA:
        if x != "":
            print(f"{x.name}")

elif teamPickMode == 2:
    playerA = listPick(playerA)
    playerB = listPick(playerB)
    for x in range(1,9):
        print(f'{x}.{playerA[x].name: <{20}}{x}.{playerB[x].name: <{20}}')
