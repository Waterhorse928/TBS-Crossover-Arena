import characters
import skills
import random
import math
import csv
import re

#Next up is probably skill reslolution. Use attublutes for every skill text, lists of IDs for more uncommon effects.

with open('TBS Tracker Template - Characters.csv', mode='r',encoding='utf-8') as infile:
    reader = csv.reader(infile)
    count= 0
    wiki = {}
    for row in reader:
        wiki[count] = row
        count += 1

with open('TBS Tracker Template - Code List.csv', mode='r',encoding='utf-8') as infile:
    reader = csv.reader(infile)
    skillWiki = {}
    for row in reader:
        if row[4] == "Skill ID":
            continue
        skillWiki[int(row[4])] = row

teamPickMode = 0
playerA = ["Player A","","","","","","","",""]
playerB = ["Player B","","","","","","","",""]
thueMorse = [0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0]
wikiList = list(range(1,13))

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
    wikiListTaken = wikiList.copy()
    for y in range(1,9):
        print(f"{player[0]}: Choose a character")
        for x in wikiListTaken:
            print(f"{x}. {wiki[x][0]}")
        n = askList(wikiListTaken)
        wikiListTaken.remove(n)
        player[y] = wikiToClass(n)
        print (f"Selected {player[y].name}")
    return player

def draftPick ():
    wikiListTakenA = wikiList.copy()
    wikiListTakenB = wikiList.copy()
    a = 1
    b = 1
    for y in thueMorse:
        if y == 0:
            print(f"{playerA[0]}: Choose a character")
            for x in wikiListTakenA:
                print(f"{x}. {wiki[x][0]}")
            n = askList(wikiListTakenA)
            wikiListTakenA.remove(n)
            playerA[a] = wikiToClass(n)
            print (f"Selected {playerA[a].name}")
            a += 1
        elif y == 1:
            print(f"{playerB[0]}: Choose a character")
            for x in wikiListTakenB:
                print(f"{x}. {wiki[x][0]}")
            n = askList(wikiListTakenB)
            wikiListTakenB.remove(n)
            playerB[b] = wikiToClass(n)
            print (f"Selected {playerB[b].name}")
            b += 1

def wikiToClass(id):
    char = getattr(characters,"Template")
    char = char(wiki[id][0],int(wiki[id][1]),int(wiki[id][2]),int(wiki[id][3]),int(wiki[id][4]),int(wiki[id][5]),int(wiki[id][6]),wiki[id][11],wiki[id][12],wiki[id][13],wiki[id][14],idToSkill(id,4),idToSkill(id,5),idToSkill(id,6),idToSkill(id,7),idToSkill(id,8),int(wiki[id][20]),int(wiki[id][21]),int(wiki[id][22]))
    return char

def idToSkill(idChar,idSkill):
    ref = wiki[idChar][idSkill + 11]
    refList = ref.splitlines()
    try:
        name = refList[0]
    except:
        return ""
    display = ref
    id = (idChar*10)+idSkill
    skillType = skillWiki[id][6]
    cost = skillWiki[id][7]
    target = skillWiki[id][8]
    damageType = skillWiki[id][9]
    damage = skillWiki[id][10]
    inflict = []
    skill = getattr(skills,"Temp")
    skill = skill(name,display,id,skillType,cost,target,damageType,damage,inflict)
    return skill

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
        print(attr_value.display)
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
                   wikiToClass(1),
                   wikiToClass(2),
                   wikiToClass(3),
                   wikiToClass(4),
                   wikiToClass(5),
                   wikiToClass(6),
                   wikiToClass(7),
                   wikiToClass(8)]
        playerB = ["Player B",
                   wikiToClass(1),
                   wikiToClass(2),
                   wikiToClass(3),
                   wikiToClass(4),
                   wikiToClass(5),
                   wikiToClass(6),
                   wikiToClass(7),
                   wikiToClass(8)]

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