import characters
import skills
import random
import math
import csv
import re

#Use attublutes for common skill mechics, lists of IDs for more uncommon effects.
#Speed Order Button
#Indirect Targeting needs to overlook KO'ed frontliners

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
roundNumber = 0
playerA = ["Player A","","","","","","","",""]
playerB = ["Player B","","","","","","","",""]
thueMorse = [0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0]
wikiList = list(range(1,13))
oneEnemy = ["One Enemy","Two Enemies","Three Enemies"]
allEnemies = ["All Enemies"]
oneAlly = ["One Ally"]
oneAllyDead = ["One Ko'ed Ally"]
allAllies = ["All Allies"]
self = ["Self", None]
statusList = ["Crit","Paralysis"]
statusListStop = ["Crit"]

#//ANCHOR Display
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

#//ANCHOR Input
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

#//ANCHOR Setup
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
    damageType = [skillWiki[id][9]]
    damage = skillWiki[id][10]
    if skillWiki[id][11]:
        inflict = eval(skillWiki[id][11])
    else:
        inflict = []
    accuracy = int(skillWiki[id][12]) if skillWiki[id][12] else 0
    skill = getattr(skills,"Temp")
    skill = skill(name,display,id,skillType,cost,target,damageType,damage,inflict,accuracy)
    return skill

#//ANCHOR Refresh
def refreshSlot():
    for x in playerA[1:]:
        x.slot = playerA.index(x)
    for x in playerB[1:]:
        x.slot = playerB.index(x)

def refreshStats():
    l = playerA[1:] + playerB[1:]
    for x in l:
        x.maxHp = x.maxHpB + x.maxHpC
        x.maxSp = x.maxSpB + x.maxSpC
        x.atk = x.atkB + x.atkC
        x.mag = x.magB + x.magC
        x.dfn = x.dfnB + x.dfnC
        x.res = x.resB + x.resC
        x.spd = x.spdB + x.spdC
        x.eva = x.evaB + x.evaC
        x.acc = x.accB + x.accC

def refreshStatus():
    l = playerA[1:] + playerB[1:]
    stats = ["maxHpC","maxSpC","atkC","magC","dfnC","resC","spdC","evaC","accC"]
    for x in l:
        x.status = []
        for stat in stats:
            value = getattr(x, stat)
            if value != 0:
                if value > 0:
                    x.status.append(f"+{value} {stat[:-1].upper()}")
                else:
                    x.status.append(f"{value} {stat[:-1].upper()}")
        for status in statusList:
            value = getattr(x, status.lower())
            if value != 0:
                x.status.append(f"{status} {value}")

def refreshMax():
    l = playerA[1:] + playerB[1:]
    for char in l:
        if char.hp > char.maxHp:
            char.hp = char.maxHp
        if char.sp > char.maxSp:
            char.sp = char.maxSp

#//ANCHOR Team List   
def strList(list):
    result = ""
    for x in list:
        result += str(x)
    return result

def inFront():
    l = [playerA[1],playerA[2],playerA[3],playerA[4],playerB[1],playerB[2],playerB[3],playerB[4]]
    return l

def inBack():
    l = [playerA[5],playerA[6],playerA[7],playerA[8],playerB[5],playerB[6],playerB[7],playerB[8]]
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
    for x in l:
        if x.paralysis != 0:
            x.spd -= 100
    l.sort(key=lambda x : x.slot)
    l.sort(key=lambda x : -x.spd)
    refreshStats()
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

#//ANCHOR Shortcuts
def getTeam(char):
    if char in playerA:
        return playerA 
    if char in playerB:
        return playerB

def getTeamList(char):
    if char in playerA:
        return playerA [1:]
    if char in playerB:
        return playerB [1:]

#//ANCHOR Actions
#//ANCHOR -Skill
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
        skill = getattr(char,"s" + str(skill))
        if checkCost(char,skill):
            useSkill(char,skill)
            return True
        else:
            print("Cannot use skill.")

def useSkill(char,skill):
    beforeCost(char,skill)
    payCost(char,skill)
    target = selectTarget(char,skill)
    while True:
        if skill.skillType == "ATK" or skill.skillType == "MAG":
            crit = char.crit
            char.crit = 0
            if crit > 0:
                print(f"Crit {crit} activates!")
            target = targeting(char,skill,target)
            target = indirectTargeting(char,skill,target)
            if not isinstance(target, list):
                target = [target]
            hitList = []
            if target == []:
                print(f"No target can be hit!")
                break
            for x in target:
                hitList.append(accuracy(char,skill,x))
            if not any(hitList):
                break
            n = 0
            crit += typeBoost(char,skill)
            for x in target:
                if hitList[n]:
                    if dealDamage(char,skill,x,crit):
                        refreshSlot()
                        KOswap(x)
                        KOEffect(x)
                n += 1
        break
    if skill.skillType == "SUP":
        if not isinstance(target, list):
            target = [target]
        supportInput(char,skill,target)
        applyStatus(char,skill,target)

#//ANCHOR --Cost
def checkCost(char,skill):
    if skill.cost == "X SP":
        if costXSP(char,skill):
            return True
        else:
            return False
    if checkIfSP(skill.cost):
        if char.sp >= pullSP(skill.cost):
            return True
    return False

def payCost(char,skill):
    if checkIfSP(skill.cost):
        char.sp -= pullSP(skill.cost)
        print(f"{char.name} spends {skill.cost}.")

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

#//ANCHOR --Targeting
def selectTarget(char,skill):
    if skill.target in oneEnemy or skill.target in oneAlly:
        y = 0
        if skill.target in oneEnemy:
            l = onTeam(alive(inFront()),char,False)
        if skill.target in oneAlly:
            l = onTeam(alive(inFront()),char)
        for x in l:
            y += 1
            print(f"{y}. {x.name}")
        target = ask(1,y)
        target = l[target-1]
        return target
    if skill.target in allEnemies:
        target = alive(onTeam(inFront(),char,False))
        return target
    if skill.target in allAllies:
        target = alive(onTeam(inFront(),char))
        return target
    if skill.target in self:
        target = char
        return target

def targeting(char,skill,target):
    if skill.target in oneEnemy:
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
    if skill.target in allEnemies:
        return target

def indirectTargeting(char,skill,target):
    refreshSlot()
    inTargets = []
    if skill.target in oneEnemy:
        if skill.target == "One Enemy":
            return target
        if skill.target == "Two Enemies":
            for x in alive(onTeam(inFront(),char)):
                if x.slot == target.slot + 1:
                    inTargets.append(x)
    if skill.target in allEnemies:
        return target
    target = [target] + inTargets
    return target

#//ANCHOR --Accuracy
def accuracy(char,skill,target):
    miss = 0
    miss += target.eva
    miss -= char.acc
    miss -= skill.accuracy
    n = random.randint(1,10)
    print(f"Rolling Accuracy. Number to beat is {miss}.")
    if n > miss:
        print(f"Rolled {n}. Hit {target.name}")
        return True
    else:
        print(f"Rolled {n}. Misssed {target.name}")
        return False

#//ANCHOR --Damage
def dealDamage(char,skill,target,crit):
    refreshStats()
    damage = int(skill.damage)
    damage += crit
    
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
    if skill.inflict:
        applyStatus(char,skill,target)
    if target.hp <= 0:
        print(f"{target.name} is KO'ed.")
        target.hp = 0
        target.turn = False
        return True
    return False

def KOswap(target):
    target.KO = True
    party = alive(getTeamList(target))
    if len(party) >= 4:
        target.turn = False
        party = alive(onTeam(inBack(),target))
        swapSelect(party,target,False)

#//ANCHOR --Effects
def applyStatus(char, skill, target):
    if not isinstance(target, list):
            target = [target]
    for x in target:
        e = skill.inflict
        statChanges(char, e, x)
        statuses(char, e, x)
        recover(char, e, x)    

def statChanges(char, e, target):
    stats = ["maxHp", "maxSp", "atk", "mag", "dfn", "res", "spd", "eva", "acc"]
    for stat in stats:
        if stat.upper() in e:
            
            if isinstance(e[stat.upper()],list):
                if not e[stat.upper()][0] >= random.randint(1,100):
                    change_value = abs(e[stat.upper()][1])
                    change_sign = "-" if e[stat.upper()][1] < 0 else "+"
                    change_string = f"{change_sign}{change_value} {stat.upper()}"
                    print(f"{target.name} resisted {change_string}.")
                    continue
                else:
                    e[stat.upper()] = e[stat.upper()][1]
            statC = stat + "C"
            statT = stat + "T"
            valueC = getattr(target, statC)
            change_made = False

            if e[stat.upper()] >= valueC >= 0 or e[stat.upper()] <= valueC <= 0 :
                setattr(target, statC, e[stat.upper()])
                change_made = True

            elif e[stat.upper()] > 0 > valueC or e[stat.upper()] < 0 < valueC:
                new_value = valueC + e[stat.upper()]
                setattr(target, statC, new_value)
                change_made = True

            if change_made:
                setattr(target, statT, True)
                change_value = abs(e[stat.upper()])
                change_sign = "-" if e[stat.upper()] < 0 else "+"
                change_string = f"{change_sign}{change_value} {stat.upper()}"
                print(f"{target.name} received {change_string}.")

def statuses(char, e, target):
    for status in statusList:
        if status in e:
            if isinstance(e[status],list):
                if not e[status][0] >= random.randint(1,100):
                    print(f"{target.name} resisted {stat} {status}.")
                    continue
                else:
                    e[status] = e[status][1]
            stat = e[status]
            value = getattr(target, status.lower())

            if stat >= value:
                setattr(target,status.lower(),stat)
                setattr(target,status.lower()+"T",True)
                print(f"{target.name} recevied {stat} {status}.")
            else:
                print(f"{target.name}'s already has {value} {status}.")

def recover(char, e, target):
    refreshStats()
    effects = ["RecoverHP","RecoverSP"]
    for effect in effects:
        if effect in e:
            n = e[effect]
            value = getattr(target,effect[-2:].lower())
            before = value
            setattr(target, effect[-2:].lower(), value+n)
            refreshMax()
            value = getattr(target,effect[-2:].lower())
            print(f"{target.name} recovered {value-before} {effect[-2:]}.")

#//ANCHOR -Rally
def rally(char):
    before = char.sp
    char.sp = min(char.sp+4,char.maxSp)
    print(f"{char.name} recovered {char.sp-before} SP.")
    rallyEffects(char)

#//ANCHOR -Swap
def swapTurn(char):
    party = onTeam(alive(allCharacters()),char,True)
    if len(party) >= 2: 
        if swapSelect(party,None,True):
            return True
        else:
            return False
    else:
        print("Too few allies to swap.")
        return False

def swapSelect(party,target1,turnAction):
    if target1 == None:
        print("Swap whom?")
        y = 0
        for x in party:
            y += 1
            print(f"{y}. {x.name}")
        if turnAction:
            print(f"0. Back")
            n = ask(0,y)
            if n == 0:
                return False
        else:
            n = ask(1,y)
        target1 = party.pop(n-1)

    print(f"Swap {target1.name} with whom?")
    y = 0
    for x in party:
        y += 1
        print(f"{y}. {x.name}")
    if turnAction:
        print(f"0. Back")
        n = ask(0,y)
        if n == 0:
            return False
    else:
        n = ask(1,y)
    target2 = party.pop(n-1)

    swap(target1,target2)
    if turnAction:
        return True

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
    swapEffect(target1,target2)

    refreshSlot()
    if (target1.turn == True and target1.slot >= 5) or trigger1:
        target1.turn = False
        print(f"{target1.name} lost their turn.")
    if (target2.turn == True and target2.slot >= 5) or trigger2:
        target2.turn = False
        print(f"{target2.name} lost their turn.")

#//ANCHOR -Check
def check(char):
    if char in playerA:
        player = playerA
    if char in playerB:
        player = playerB
    displaySelect(player)

def displaySelect(player):
    refreshStats()
    box([[strList([c.slot,". ",c.name])] + [strList(["HP ",c.hp,"/",c.maxHp])] + [strList(["SP ",c.sp,"/",c.maxSp])] + [strList(["DEF ",c.dfn])] + [strList(["RES ",c.res])] + [strList(["SPD ",c.spd])] + [strList(["EVA ",c.eva])] for c in player[1:]],"left")
    print("0. Back")
    result = ask(0,8)
    if result == 0:
        return
    result = player[result]
    display(result)

def display(char):
    refreshStats()
    refreshStatus()
    print(f"{char.name} - {char.fullname}")
    print()
    print(f"HP {char.hp}/{char.maxHpB} DEF {char.dfnB} SPD {char.spdB}")
    print(f"SP {char.sp}/{char.maxSpB} RES {char.resB} EVA {char.evaB}")
    print(f"{char.status}")
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

#//ANCHOR -Scout
def scout(char):
    if char in playerA:
        player = playerB
    if char in playerB:
        player = playerA
    displaySelect(player)
 
#//ANCHOR -Order
def order():
    pass

#//ANCHOR Turn
def startTurn(char):
    char.turn = False
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
            if swapTurn(char):
                break
        if x == 4:
            check(char)
        if x == 5:
            scout(char)
        if x == 6:
            order()
    resolveStatus(char)
    endOfTurn()

def resolveStatus(char):
    stats = ["maxHp","maxSp","atk","mag","dfn","res","spd","eva","acc"]
    for stat in stats:
        statC = stat + "C"
        statT = stat + "T"
        valueC = getattr(char, statC)
        valueT = getattr(char, statT)

        if valueC > 0 and not valueT:
            setattr(char, statC, valueC - 1)
        elif valueC < 0 and not valueT:
            setattr(char, statC, valueC + 1)

    for status in statusList:
        if status in statusListStop:
            continue
        value = getattr(char,status.lower())
        valueT = getattr(char,status.lower()+"T")

        if value != 0 and not valueT:
            setattr(char, status.lower(), value - 1)

def endOfTurn():
    l = playerA[1:] + playerB[1:]
    stats = ["maxHp", "maxSp", "atk", "mag", "dfn", "res", "spd", "eva", "acc"]
    for x in l:
        for stat in stats:
            setattr(x, stat + "T", False)
        for status in statusList:
            setattr(x, status.lower() + "T", False)
    refreshSlot()
    refreshStats()
    refreshStatus()
    refreshMax()

#//ANCHOR Gameflow
def start():
    global playerA
    global playerB
    global roundNumber
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
        roundNumber += 1
        print (f"---Round {roundNumber}---")
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
        for x in alive(inBack()):
            beforeHP = x.hp
            beforeSP = x.sp
            x.hp += 2
            x.sp += 2
            restStep(x)
            refreshMax()
            recoveredHP = x.hp - beforeHP
            recoveredSP = x.sp - beforeSP
            if recoveredHP > 0:
                print(f"{x.name} recovered {recoveredHP} HP.")
            if recoveredSP > 0:
                print(f"{x.name} recovered {recoveredSP} SP.")
        endOfRound()

#//ANCHOR INDIVIDUAL MECHNICS (the begining of the end)
def supportInput(char,skill,target):
    if skill.id == 17:
        print ("1.DEF or 2.RES?")
        n = ask(1,2)
        if n == 1:
            skill.inflict = {"DFN":3}
        if n == 2:
            skill.inflict = {"RES":3}

def rallyEffects(char):
    if char.id == 1:
        if char.crit < 3:
            print(f"-Grand Incantation-")
            e = {"Crit":3}
            statuses(char,e,char)

def typeBoost(char,skill):
    party = alive(onTeam(inFront(),char))
    boost = 0
    for x in party:
        if x.id == 2 and "Mystic" in skill.damageType:
            boost += 1
            print(f"-Magic Overflowing-\nMystic damage increased by 1.")
    return boost

def costXSP(char,skill):
    if skill.id == 27:
        return True
    return False

def beforeCost(char,skill):
    if skill.id == 27:
        skill.cost = f"{char.sp} SP"
        skill.damage = char.sp-3

def swapEffect(target1,target2):
    for x in [target1,target2]:
        if x.id == 3 and x.oncePerRound and not x.KO:
            print(f"-Instant Attack-\n{x.name} recovered her turn.")
            x.turn = True
            x.oncePerRound = False

def restStep(x):
    pass

def endOfRound():
    for x in alive(allCharacters()):
        x.oncePerRound = True

def KOEffect(char):
    if char.id == 4:
        e = {"SPD":-2}
        otherParty = alive(onTeam(inFront(),char,False))
        print(names(otherParty))
        for x in otherParty:
            statChanges(char,e,x)

start()