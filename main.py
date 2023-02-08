import characters
import random
import math
from characters import wikiList

teamPickMode = 0
playerA = ["","","","","","","","",""]
playerB = []
choosen = []

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
        
print ("-Team Pick-\n 1. Draft\n 2. List")
teamPickMode = ask(1,2)   

#replace choosen with a list of character not choosen yet. For x in list of not choosen.
if teamPickMode == 1:
    print("Player A: Choose a character")
    for y in range(1,9):
        for x in range(1,len(wikiList)):
            if not x in choosen:
                print(f"{x}. {wikiList[x].name}")
        n = ask(1,12)
        choosen.append(n)
        playerA[y] = wikiList[n]
        print (f"Selected {wikiList[n].name}")
    for x in playerA:
        if x != "":
            print(f"{x.name}")
elif teamPickMode == 2:
    print ("filth")
