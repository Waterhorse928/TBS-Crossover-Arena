import characters
import random
import math
from characters import wikiList

teamPickMode = 0

def ask (lowRange,highRange):
    while True:
        try:
            result = int(input(""))
        except:
            continue
        if lowRange <= result <= highRange:
            return result
        
print ("-Team Pick-\n 1. Draft\n 2. List")
teamPickMode = ask(1,2)   

if teamPickMode == 1:
    print("Player A: Choose a character")
    for x in range(len(wikiList)):
        print(f"{x}. {wikiList[x].name}")
    ask(0,11)
elif teamPickMode == 2:
    print ("filth")
