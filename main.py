import characters
import random
import math
from characters import wikiList
import csv

with open('TBS Tracker Template - Characters.csv', mode='r',encoding='utf-8') as infile:
    reader = csv.reader(infile)
    count= 0
    wiki = {}
    for row in reader:
        wiki[count] = row
        count += 1

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
    result = [player[0],"","","","","","","",""]
    for y in range(1,9):
        print(f'{player[0]}: Choose a character for Slot {y}.')
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

def box(text,align = "center"):
    boxSize = 120
    print(f'{"":-^{boxSize+2}}')
    if align == "center":
        rows = len(text)
        for x in range(0,rows):
            columns = len(text[x])
            margin = boxSize//columns
            print ("|",end="")
            for y in text[x]:
                print(f'{y: ^{margin}}',end="")
            print ("|")
        print(f'{"":-^{boxSize+2}}')
    if align == "left":
        rows = len(text)
        for x in range(0,rows):
            columns = len(text[x])
            margin = boxSize//columns
            print ("|",end="")
            for y in text[x]:
                print(f'{y: <{margin}}',end="")
            print ("|")
        print(f'{"":-^{boxSize+2}}')

def percentage(part, whole, size):
    return size * float(part) / float(whole)

def healthbar(HP,maxHP,size):
    if maxHP <= size:
        bar = ('|'*HP)
        result = (f'[{bar: <{maxHP}}]')
    elif maxHP > size:
        percent = math.ceil(percentage(HP,maxHP,size))
        bar = ('|'*percent)
        result = (f'[{bar: <{size}}]')
    return result

def strList(list):
    result = ""
    for x in list:
        result += str(x)
    return result

def display(l):

    pass

def refreshSlot():
    for x in playerA[1:]:
        x.slot = playerA.index(x)
    for x in playerB[1:]:
        x.slot = playerB.index(x)

def inFront():
    l = [playerA[1],playerA[2],playerA[3],playerA[4],playerB[1],playerB[2],playerB[3],playerB[4]]
    return l

def alive(l):
    newList = []
    for x in l:
        if x.KO == False:
            newList.append(x)
    return newList

def speedOrder(l):
    refreshSlot()
    random.shuffle(l)
    l.sort(key=lambda x : x.slot)
    l.sort(key=lambda x : -x.spd)
    return l

def names(l):
    newList = []
    for x in l:
        newList.append(x.name)
    return newList
        
def hasTurn(l):
    newList = []
    for x in l:
        if x.turn == True:
            newList.append(x)
    return newList

def skillSelect(char):
    pass

def rally(char):
    char.sp = min(char.sp+4,char.maxSp)

def swapSelect(char):
    pass

def checkSelect(char):
    if char in playerA:
        player = playerA
    if char in playerB:
        player = playerB
    box([[strList([c.slot,". ",c.name])] + [strList(["HP ",c.hp,"/",c.maxHp])] + [strList(["SP ",c.sp,"/",c.maxSp])] + [strList(["DEF ",c.dfn])] + [strList(["RES ",c.res])] + [strList(["SPD ",c.spd])] + [strList(["EVA ",c.eva])] for c in player[1:]],"left")
    result = ask(1,8)
    result = player[result]
    check(result)

def check(char):
    print(f"{char.name} - {char.fullname}")
    print()
    print(f"HP {char.hp}/{char.maxHp} DEF {char.dfn} SPD {char.spd}")
    print(f"SP {char.sp}/{char.maxSp} RES {char.res} EVA {char.eva}")
    for x in range(1,char.passives+1):
        print()
        attr_name = "p" + str(x)
        attr_value = getattr(char, attr_name)
        print(attr_value)
    for x in range(1,char.skills+1):
        print()
        attr_name = "s" + str(x)
        attr_value = getattr(char, attr_name)
        print(attr_value)
    input(f"")

def scout(char):
    if char in playerA:
        player = playerB
    if char in playerB:
        player = playerA
    box([[strList([c.slot,". ",c.name])] + [strList(["HP ",c.hp,"/",c.maxHp])] + [strList(["SP ",c.sp,"/",c.maxSp])] + [strList(["DEF ",c.dfn])] + [strList(["RES ",c.res])] + [strList(["SPD ",c.spd])] + [strList(["EVA ",c.eva])] for c in player[1:]],"left")
    result = ask(1,8)
    result = player[result]
    check(result)

def order():
    pass

def startTurn(char):
    #Bare Bones displays only
    #Start of turn effects
    #Actions
    #End of turn effects
    #Status Effects Resolve
    while True:
        box([[f"---{char.name}'s Turn---"],["1. Skill","2. Rally","3. Swap","4. Check","5. Scout","6. Order"]])
        refreshSlot()
        x = ask(1,6)
        if x == 1:
            skillSelect(char)
        if x == 2:
            rally(char)
            break
        if x == 3:
            swapSelect(char)
        if x == 4:
            checkSelect(char)
        if x == 5:
            scout(char)
        if x == 6:
            order()
    char.turn = False

def start():
    global playerA
    global playerB
    # Team Pick        
    box([["---Team Pick---"],["1. Draft Select","2. List Select","3. Debug Select"]])
    teamPickMode = ask(1,3)   
    if teamPickMode == 1:
        draftPick()     
        checkTeams()
    elif teamPickMode == 2:
        playerA = listPick(playerA)
        playerB = listPick(playerB)
        checkTeams()
    elif teamPickMode == 3:
        playerA = ["Player A",
                   characters.Reimu(),
                   characters.Marisa(),
                   characters.Chen(),
                   characters.Cirno(),
                   characters.Emilie(),
                   characters.Momiji(),
                   characters.Gaius(),
                   characters.Parsee()]
        playerB = ["Player B",
                   characters.Parsee(),
                   characters.Gaius(),
                   characters.Momiji(),
                   characters.Emilie(),
                   characters.Cirno(),
                   characters.Chen(),
                   characters.Marisa(),
                   characters.Reimu()]

    # Slot Order
    if teamPickMode != 3:
        playerA = slotOrder(playerA)
        playerB = slotOrder(playerB)
        checkTeams()

    #Main Flow
    while True:
        #Setup
        for x in alive(inFront()):
            x.turn = True
        #Flow
        while True:
            #Setup
            if all(char.turn == False for char in alive(inFront())):
                break
            #Next Turn in Speed Order
            startTurn(hasTurn(alive(speedOrder(inFront())))[0])

        #Cleanup
            #Check Win Condtion
            #Rest
    
start()