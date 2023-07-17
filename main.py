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

# Display
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

def checkTeams():
    print(f'{"Player A": <{20}}{"Player B": <{20}}')
    for x in range(1,9):
        print(f'{str(x) + ". " + playerA[x].name: <{20}}{str(x) + ". " + playerB[x].name: <{20}}')

# Input
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

# Setup
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

# Team List   
def strList(list):
    result = ""
    for x in list:
        result += str(x)
    return result

def refreshSlot():
    for x in playerA[1:]:
        x.slot = playerA.index(x)
    for x in playerB[1:]:
        x.slot = playerB.index(x)

def inFront():
    l = [playerA[1],playerA[2],playerA[3],playerA[4],playerB[1],playerB[2],playerB[3],playerB[4]]
    return l

def allCharacters():
    l = [playerA[1],playerA[2],playerA[3],playerA[4],playerA[5],playerA[6],playerA[7],playerA[8],playerB[1],playerB[2],playerB[3],playerB[4],playerB[5],playerB[6],playerB[7],playerB[8]]
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

def onTeam(l,char,on=True):
    if (char in playerA and on) or (not char in playerA and not on):
        team = playerA
    if (char in playerB and on) or (not char in playerB and not on):
        team = playerB
    newList = []
    for x in l:
        if x in team:
            newList.append(x)
    return newList

def beforeSlot(l,target):
    newList = []
    for x in l:
        if x.slot <= target.slot:
            newList.append(x)
    return newList

# Shortcuts
def getTeam(char):
    if char in playerA:
        return playerA
    if char in playerB:
        return playerB

# Actions
# - Skill
def skillSelect(char):
    while True:
        print(f"---{char.name}'s Skills---")
        for x in range(1,char.skills+1):
            print()
            print(f"{x}. ",end="")
            print(getattr(char,"s" + str(x)).display)
        print()
        print("0. Back")
        print()
        skill = ask(0,char.skills)
        if skill == 0:
            return False
        if checkCost(char,skill):
            useSkill(char,skill)
            return True
        else:
            print("Cannot use skill.")

def useSkill(char,skill):
    skill = getattr(char,"s" + str(skill))
    payCost(char,skill)
    target = selectTarget(char,skill)
    if skill.skillType == "ATK" or skill.skillType == "MAG":
        target = targeting(char,skill,target)
        hit  = accuracy(char,skill,target)
        if hit:
            if dealDamage(char,skill,target):
                KOswap(target)

def KOswap(target):
    pass

def dealDamage(char,skill,target):
    damage = int(skill.damage)
    
    if skill.skillType == "ATK":
        damage += char.atk
        damage -= target.dfn
        damage = max(0,damage)

    if skill.skillType == "MAG":
        damage += char.mag
        damage -= target.res
        damage = max(0,damage)

    print (f'{char.name} deals {damage} damage to {target.name}.')
    target.hp -= damage
    if target.hp <= 0:
        print(f"{target.name} is KO'ed.")
        target.hp = 0
        target.KO = True
        return True
    return False

def targeting(char,skill,target):
    if skill.target == "One Enemy":
        l = beforeSlot(onTeam(alive(inFront()),target,True),target)
        interceptList = []
        for x in l:
            for y in range(0,x.intercept):
                interceptList.append(x.name)
        for x in range(0,6):
            interceptList.append(target.name)
        roll = []
        for x in range(0,6):
            roll.append(interceptList[x])
        print("rolling targeting")
        y = 0
        for x in roll:
            y += 1
            print(f"{y}. {x}")
        n = random.randint(1,6)
        for x in l:
            if roll[n-1] == x.name:
                target = x
        print(f"Rolled a {n}. Targeting {target.name}")
        return target

def accuracy(char,skill,target):
    miss = 0
    miss += target.eva
    miss -= char.acc
    miss -= skill.acc
    n = random.randint(1,10)
    print(f"Rolling Accuracy. Number to beat is {miss}.")
    if n > miss:
        print(f"Rolled {n}. Hit")
        return True
    else:
        print(f"Rolled {n}. Miss")
        return False

def payCost(char,skill):
    if checkIfSP(skill.cost):
        char.sp -= pullSP(skill.cost)
        print(f"{char.name} spends {skill.cost}.")

def selectTarget(char,skill):
    if skill.target == "One Enemy":
        y = 0
        l = onTeam(alive(inFront()),char,False)
        for x in l:
            y += 1
            print(f"{y}. {x.name}")
        target = ask(1,y)
        target = l[target-1]
        return target

def checkCost(char,skill):
    skill = getattr(char,"s" + str(skill))
    if checkIfSP(skill.cost):
        if char.sp >= pullSP(skill.cost):
            return True
    return False

def checkIfSP(variable):
    pattern = r"^\d+ SP$"
    match = re.match(pattern, variable)
    return match is not None

def pullSP(variable):
    pattern = r"(\d+) SP"
    match = re.search(pattern, variable)
    if match:
        number = int(match.group(1))
        return number
    else:
        return None

# - Rally
def rally(char):
    char.sp = min(char.sp+4,char.maxSp)

# - Swap
def swapSelect(char):
    party = onTeam(alive(allCharacters()),char,True)
    if len(party) >= 2: 
        print("Swap whom?")
        y = 0
        for x in party:
            y += 1
            print(f"{y}. {x.name}")
        print(f"0. Back")
        n = ask(0,y)
        if n == 0:
            return False
        target1 = party.pop(n-1)
        print(f"Swap {target1.name} with whom?")
        y = 0
        for x in party:
            y += 1
            print(f"{y}. {x.name}")
        print(f"0. Back")
        n = ask(0,y)
        if n == 0:
            return False
        target2 = party.pop(n-1)
        swap(target1,target2)
        return True
        
    else:
        print("Too few allies to swap.")
        return False

def swap(target1,target2):
    refreshSlot()
    trigger1 = False
    trigger2 = False
    if target1.turn == True and target1.slot >= 5:
        trigger1 = True
    if target2.turn == True and target2.slot >= 5:
        trigger2 = True

    print(f"Swapped {target1.name} and {target2.name}.")
    party = getTeam(target1)
    a, b = party.index(target1), party.index(target2)
    party[b], party[a] = party[a], party[b]

    refreshSlot()
    if (target1.turn == True and target1.slot >= 5) or trigger1:
        target1.turn = False
        print(f"{target1.name} lost their turn.")
    if (target2.turn == True and target2.slot >= 5) or trigger2:
        target2.turn = False
        print(f"{target2.name} lost their turn.")

# - Check
def check(char):
    if char in playerA:
        player = playerA
    if char in playerB:
        player = playerB
    displaySelect(player)

def displaySelect(player):
    box([[strList([c.slot,". ",c.name])] + [strList(["HP ",c.hp,"/",c.maxHp])] + [strList(["SP ",c.sp,"/",c.maxSp])] + [strList(["DEF ",c.dfn])] + [strList(["RES ",c.res])] + [strList(["SPD ",c.spd])] + [strList(["EVA ",c.eva])] for c in player[1:]],"left")
    print("0. Back")
    result = ask(0,8)
    if result == 0:
        return
    result = player[result]
    display(result)

def display(char):
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

# - Scout
def scout(char):
    if char in playerA:
        player = playerB
    if char in playerB:
        player = playerA
    displaySelect(player)
    
# - Order
def order():
    pass

# Turn
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
            if skillSelect(char):
                break
        if x == 2:
            rally(char)
            break
        if x == 3:
            if swapSelect(char):
                break
        if x == 4:
            check(char)
        if x == 5:
            scout(char)
        if x == 6:
            order()
    char.turn = False

# Gameflow
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