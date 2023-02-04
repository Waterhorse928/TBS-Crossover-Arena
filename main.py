import characters
import random
import math

teamPickMode = 0

def ask (lowRange,highRange):
    while True:
        try:
            result = int(input("Please input a valid number: "))
        except:
            continue
        if lowRange <= result <= highRange:
            return result
        
print ("-Team Pick-\n 1. Draft\n 2. List")
teamPickMode = ask(1,2)   

if teamPickMode == 1:
    print ("the good one")
elif teamPickMode == 2:
    print ("filth")
