import characters
import skills
import random
import math
import csv
import re

#Indirect Targeting needs to overlook KO'ed frontliners
#Death and Distance

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
wikiList = list(range(1,20))
oneEnemy = ["One Enemy","Two Enemies","Three Enemies"]
allEnemies = ["All Enemies"]
oneAlly = ["One Ally","One KO'ed Ally"]
dead = ["One KO'ed Ally","Any KO'ed Ally"]
anyTarget = ["Any Target","Any KO'ed Ally"]
allAllies = ["All Allies"]
self = ["Self", None]
oneTarget = ["One Target", "One Other Target"]
ally = oneAlly + allAllies + ["Any KO'ed Ally"]
one = oneTarget + oneAlly + oneEnemy
other = ["One Other Target"]
statusList = ["Crit","Paralysis","Burn",["Break","brea"],"Terror","Silence","Precision","Death","Distance","Taunt","Scope","Cure","Weaken","Disable","Bold"]
debuffList = ["Paralysis","Burn","Terror","Silence","Death","Weaken","Disable"]
statusListStop = ["Crit"]
statusListCount = ["Death"]

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

def displayBox(l):
    if len(l) <= 4:
        #box([[strList([c.slot,". ",c.name])] + [strList(["HP ",c.hp if not c.KO else "KO","/",c.maxHp])] + [strList(["SP ",c.sp,"/",c.maxSp])] + [strList(["DEF ",c.dfn])] + [strList(["RES ",c.res])] + [strList(["SPD ",c.spd])] + [strList(["EVA ",c.eva])] for c in player[1:]],"left")
        box([[f"Player {'A' if l[0] in playerA else 'B'}"],[f"Slot {c.slot}" for c in l],[f"{c.name}" for c in l],[f"HP {c.hp if not c.KO else 'KO'}/{c.maxHpB} - SP {c.sp}/{c.maxSpB}" for c in l],[f"{c.status if c.status else ''}" for c in l]])
    elif len(l) <= 8:
        pass
    else:
        pass

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
        inflict = {}
    accuracy = int(skillWiki[id][12]) if skillWiki[id][12] else 0
    if skillWiki[id][13]:
        effect = eval(skillWiki[id][13])
    else:
        effect = {}
    if skillWiki[id][14]:
        self = eval(skillWiki[id][14])
    else:
        self = {}
    skill = getattr(skills,"Temp")
    skill = skill(name,display,id,skillType,cost,target,damageType,damage,inflict,accuracy,effect,self)
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
            statusA = status.lower() if not isinstance(status,list) else status[1]
            statusD = status if not isinstance(status,list) else status[0]
            value = getattr(x, statusA)
            if value != 0:
                x.status.append(f"{statusD} {value}")

def refreshMax():
    l = playerA[1:] + playerB[1:]
    for char in l:
        if char.hp > char.maxHp and not uncappedHP(char):
            char.hp = char.maxHp
        if char.sp > char.maxSp and not uncappedSP(char):
            char.sp = char.maxSp

def refreshCleanse():
    l = playerA[1:] + playerB[1:]
    for char in l:
        if char.cure != 0:
            cleanse(char,{"Cure":char.cure})

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

def playerAList():
    l = [playerA[1],playerA[2],playerA[3],playerA[4],playerA[5],playerA[6],playerA[7],playerA[8]]
    return l

def playerBList():
    l = [playerB[1],playerB[2],playerB[3],playerB[4],playerB[5],playerB[6],playerB[7],playerB[8]]
    return l

def alive(l):
    newList = []
    for x in l:
        if x.KO == False:
            newList.append(x)
    return newList

def deadList(l):
    newList = []
    for x in l:
        if x.KO == True:
            newList.append(x)
    return newList

def speedOrder(l):
    refreshSlot()
    random.shuffle(l)
    l = speedEffects(l)
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

def getStatChangeDict(char):
    stats = ["maxHpC","maxSpC","atkC","magC","dfnC","resC","spdC","evaC","accC"]
    statDict = {}
    for stat in stats:
        value = getattr(char,stat)
        if value != 0:
            statDict[stat[:-1].upper()] = value
    return statDict

def getSkillList(char):
    l = []
    for x in range(1,char.skills+1):
        l.append(getattr(char,"s" + str(x)))
    return l

def getDamageTypes(char):
    typeList = []
    for skill in getSkillList(char):
        typeList.append(skill.damageType)
    return typeList

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
            if useSkill(char,skill):
                return True
            else:
                print("Cannot use skill.")
        else:
            print("Cannot use skill.")

def useSkill(char,skill):
    beforeCost(char,skill)
    payCost(char,skill)
    target = selectTarget(char,skill)
    if target == False:
        return False
    while True:
        if skill.skillType == "ATK" or skill.skillType == "MAG":
            skill.damageDealt = 0
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
                if accuracy(char,skill,x):
                    hitList.append(x)
            if not any(hitList):
                break
            n = 0
            crit += typeBoost(char,skill)
            for x in hitList:
                    dealDamage(char,skill,x,crit)
        break
    if skill.skillType == "SUP":
        if not isinstance(target, list):
            target = [target]
        supportInput(char,skill,target)
        applyStatus(char,skill,target)
        uniqueSupports(char,skill,target)
    if skill.self:
        selfEffect(char,skill)
        applyStatus(char,skill.self,char)
    cleanupSkill(char,skill)
    return True

#//ANCHOR --Cost
def checkCost(char,skill):
    if checkIfBlocked(char,skill):
        return False
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
    if skill.target in one or skill.target in anyTarget:
        y = 0
        if skill.target in oneEnemy:
            l = onTeam(inFront(),char,False)
        if skill.target in oneAlly:
            l = onTeam(inFront(),char)
        if skill.target in oneTarget:
            l = onTeam(inFront(),char) + onTeam(inFront(),char,False)
        if skill.target in anyTarget:
            l = allCharacters()
        if skill.target not in dead:
            l = alive(l)
        else:
            l = deadList(l)
        if skill.target in other:
            l.remove(char)
        if l:
            for x in l:
                y += 1
                print(f"{y}. {x.name}")
            target = ask(1,y)
            target = l[target-1]
            return target
        else:
            print(f"No available targets.")
            return False
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
        if not autoTarget(char,skill,target):
            l = beforeSlot(onTeam(alive(inFront()),target,True),target)
            interceptList = []
            interceptEffects(l)
            for x in l:
                for y in range(0,x.intercept):
                    interceptList.append(x.name)
            for x in range(0,6):
                interceptList.append(target.name)
            roll = []
            for x in range(0,6):
                roll.append(interceptList[x])
            print("Rolling targeting.")
            y = 0
            for x in roll:
                y += 1
                print(f"{y}. {x}")
            n = random.randint(1,6)
            for x in l:
                if roll[n-1] == x.name:
                    target = x
            print(f"Rolled a {n}, targeting {target.name}.")
            return target
        else:
            return target
    if skill.target in allEnemies:
        return target

def indirectTargeting(char,skill,target):
    refreshSlot()
    inTargets = []
    if skill.target in oneEnemy:
        party = alive(onTeam(inFront(),target))
        if skill.target == "One Enemy":
            return target
        if skill.target == "Two Enemies":
            for x in party:
                if party.index(x) == party.index(target) + 1:
                    if indirectTargetBlock(x):
                        pass
                    else:
                        inTargets.append(x)
    if skill.target in allEnemies:
        for x in target:
            print(x.distance)
            if indirectTargetBlock(x):
                target.remove(x)
            else:
                pass
        return target
    target = [target] + inTargets
    return target

#//ANCHOR --Accuracy
def accuracy(char,skill,target):
    refreshStats()
    beforeAccuracy(char,skill,target)
    miss = 0
    miss += target.eva
    miss -= char.acc
    miss -= skill.accuracy
    n = random.randint(1,10)
    if autoMiss(char,skill,target):
        return False
    else:
        print(f"Rolling Accuracy. Number to beat is {miss}.")
        if alwaysHit(char,skill,target):
            return True
        if n > miss:
            print(f"Rolled {n}, Hit {target.name}.")
            return True
        else:
            print(f"Rolled {n}, Missed {target.name}.")
            return False

#//ANCHOR --Damage
def dealDamage(char,skill,target,crit):
    refreshStats()
    crit = beforeDamage(char,skill,target,crit)
    damage = int(skill.damage)
    damage += crit
    ignore = gatherBreak(char,skill,target)
    opposite = oppositeCheck(char,skill,target)
    
    if skill.skillType == "ATK":
        damage += char.atk
        damage = beforeBlock(char,skill,target,damage)
        if opposite:
            damage -= max(target.res-ignore,0)
        else:
            damage -= max(target.dfn-ignore,0)
        damage = max(0,damage)

    if skill.skillType == "MAG":
        damage += char.mag
        damage = beforeBlock(char,skill,target,damage)
        if opposite:
            damage -= max(target.dfn-ignore,0)
        else:
            damage -= max(target.res-ignore,0)
        damage = max(0,damage)

    before = target.hp
    target.hp -= damage
    refreshMax()
    dealt = before - target.hp
    print (f'{char.name} deals {dealt} damage to {target.name}.')
    skill.damageDealt += dealt
    onHitEffects(char,skill,target)
    if skill.inflict:
        applyStatus(char,skill,target)
    if KOcheck(target):
        effectOnKO(char,skill,target)

def KOswap(target):
    target.KO = True
    party = alive(getTeamList(target))
    if len(party) >= 4:
        target.turn = False
        party = alive(onTeam(inBack(),target))
        swapSelect(target,party,target,False)

#//ANCHOR --Effects
def applyStatus(char, skill, target):
    if not isinstance(target, list):
            target = [target]
    for x in target:
        if isinstance(skill,dict):
            e = skill
        else:
            e = skill.inflict
        revive(char, e, x)
        statChanges(char, e, x)
        statuses(char, e, x)
        recover(char, e, x)

def revive(char, e, target):
    refreshStats()
    effects = ["Revive"]
    for effect in effects:
        if effect in e:
            target.KO = False
            print(f"{target.name} is revived and no longer KO'ed.")

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

            if e[stat.upper()] == "R" and valueC != 0:
                change_value = abs(valueC)
                change_sign = "-" if valueC < 0 else "+"
                change_string = f"{change_sign}{change_value} {stat.upper()}"
                setattr(target, statC, 0)
                print(f"{change_string} was removed from {target.name}.")
                continue

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
        statusA = status.lower() if not isinstance(status,list) else status[1]
        statusD = status if not isinstance(status,list) else status[0]
        if statusD in e:
            if isinstance(e[statusD],list):
                if not e[statusD][0] >= random.randint(1,100):
                    print(f"{target.name} resisted [{statusD} {e[statusD][1]}].")
                    continue
                else:
                    e[statusD] = e[statusD][1]
            stat = e[statusD]
            value = getattr(target, statusA)

            if stat == "R" and value != 0:
                setattr(target, statusA, 0)
                print(f"{statusD} {value} was removed from {target.name}.")
                continue
            
            if stat == 0 and value == 0:
                if statusD == "Cure":
                    print(f"{target.name} recevied {statusD} {stat}.")
                    cleanse(target,{statusD:stat})

            if stat >= value and not statusD in statusListCount:
                setattr(target,statusA,stat)
                setattr(target,statusA+"T",True)
                print(f"{target.name} recevied {statusD} {stat}.")
            elif not statusD in statusListCount:
                print(f"{target.name}'s already has {statusD} {value}.")

            if (stat < value or value == 0) and statusD in statusListCount:
                setattr(target,statusA,stat)
                setattr(target,statusA+"T",True)
                print(f"{target.name} recevied {statusD} {stat}.")
                if stat == 0:
                    countdown(statusD,target)
                    KOcheck(target)
            elif statusD in statusListCount:
                print(f"{target.name}'s already has {statusD} {value}.")

            refreshCleanse()

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
        if swapSelect(char,party,None,True):
            return True
        else:
            return False
    else:
        print("Too few allies to swap.")
        return False

def swapSelect(char,party,target1,turnAction=False):
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
        formation(char)
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
    box([[strList([c.slot,". ",c.name])] + [strList(["HP ",c.hp if not c.KO else "KO","/",c.maxHp])] + [strList(["SP ",c.sp,"/",c.maxSp])] + [strList(["DEF ",c.dfn])] + [strList(["RES ",c.res])] + [strList(["SPD ",c.spd])] + [strList(["EVA ",c.eva])] for c in player[1:]],"left")
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
    ko = "KO'ed"
    print(f'{"" if not char.KO else ko}')
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
def order(char):
    player = speedOrder(inFront())
    refreshStats()
    box([[strList([player.index(c)+1,". ",c.name])] + [strList(["Turn ","[X]" if c.turn else "[ ]"])] + [strList(["SPD ",c.spd])] + [strList([c.status])] for c in player],"left")
    print("0. Back")
    result = ask(0,8)
    if result == 0:
        return
    result = player[result-1]
    display(result)

#//ANCHOR Turn
def startTurn(char):
    char.turn = False
    startOfTurn(char)
    #Bare Bones displays only
    #Start of turn effects
    #Actions
    #End of turn effects
    #Status Effects Resolve
    while True:
        refreshStatus()
        displayBox(onTeam(inFront(),playerA[0]))
        displayBox(onTeam(inFront(),playerB[0]))
        box([[f"Player {'A' if char in playerA else 'B'}'s"],[f"---{char.name}'s Turn---"],[f"HP {char.hp}/{char.maxHpB} - SP {char.sp}/{char.maxSpB}"],[f"{char.status if char.status else ''}"],["1. Skill","2. Rally","3. Swap","4. Check","5. Scout","6. Order"]])
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
            order(char)
    resolveStatus(char)
    endOfTurnEffects(char)
    endTurn()

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

        statusA = status.lower() if not isinstance(status,list) else status[1]
        statusD = status if not isinstance(status,list) else status[0]

        value = getattr(char,statusA)
        valueT = getattr(char,statusA + "T")

        
        if value != 0 and not valueT:
            recoverEffects(value,valueT,status,statusD,statusA,char)
            drainEffects(value,valueT,status,statusD,statusA,char)
            setattr(char, statusA, value - 1)
            if value - 1 != 0:
                print(f"[{statusD} {value}] drops to [{statusD} {value - 1}]")
            else:
                print(f"[{statusD} {value}] drops to [{statusD} {value - 1}] and is removed")
                if statusD in statusListCount:
                    countdown(statusD,char)
    KOcheck(char)

def endTurn():
    l = playerA[1:] + playerB[1:]
    stats = ["maxHp", "maxSp", "atk", "mag", "dfn", "res", "spd", "eva", "acc"]
    for x in l:
        for stat in stats:
            setattr(x, stat + "T", False)
        for status in statusList:
            statusA = status.lower() if not isinstance(status,list) else status[1]
            statusD = status if not isinstance(status,list) else status[0]
            setattr(x, statusA + "T", False)
    refreshSlot()
    refreshStats()
    refreshStatus()
    refreshMax()
    refreshCleanse()
    
#//ANCHOR Gameflow
def main():
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
        playerA = testA
        playerB = testB

    # Slot Order
    if teamPickMode != 3:
        playerA = slotOrder(playerA)
        playerB = slotOrder(playerB)
        checkTeams()

    playerAwin =False
    playerBwin =False
    #Main Flow
    startOfGame()
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
        n = 0
        for x in playerAList():
            if x.KO:
                n+=1
        if n == len(playerAList()):
            playerBwin = True
        n = 0
        for x in playerBList():
            if x.KO:
                n+=1
        if n == len(playerBList()):
            playerAwin = True
        if playerAwin or playerBwin:
            if playerAwin and playerBwin:
                box([[""],["GAME END"],[""],["---DRAW?---"],[""]])
                input()
                break
            if playerAwin:
                box([[""],["GAME END"],[""],["---PLAYER A WINS!---"],[""]])
                input()
                break
            if playerBwin:
                box([[""],["GAME END"],[""],["---PLAYER B WINS!---"],[""]])
                input()
                break
        #Rest
        for x in alive(inBack()):
            beforeHP = x.hp
            beforeSP = x.sp
            x.hp = min(x.hp+2,x.maxHp)
            x.sp = min(x.sp+2,x.maxSp)
            restStep(x)
            refreshMax()
            recoveredHP = x.hp - beforeHP
            recoveredSP = x.sp - beforeSP
            if recoveredHP > 0:
                print(f"{x.name} recovered {recoveredHP} HP.")
            if recoveredSP > 0:
                print(f"{x.name} recovered {recoveredSP} SP.")
        endOfRound()

def KOcheck(char):
    if char.hp <= 0:
        print(f"{char.name} is KO'ed.")
        char.hp = 0
        char.turn = False
        refreshSlot()
        KOswap(char)
        KOEffect(char)
        return True
    return False

#//ANCHOR Status Effect Funcions
def gatherBreak(char,skill,target):
    b = 0
    if "Break" in skill.effect:
        b += skill.effect["Break"]
    if char.brea != 0:
        b += char.brea
    return b

def checkIfBlocked(char,skill):
    atkBlocks = ["Weaken"]
    magBlocks = ["Silence"]
    supBlocks = ["Disable"]
    types = ["ATK","MAG","SUP"]
    for type in types:
        if skill.skillType == type:
            for block in eval(f"{type.lower()}Blocks"):
                value = getattr(char,block.lower())
                if value != 0:
                    print(f"Suffering {block}.")
                    return True
    return False

def countdown(status,char):
    if status == "Death":
        print("Death hit 0!")
        char.hp = 0

def speedEffects(l):
    for x in l:
        if x.paralysis != 0:
            x.spd -= 100
    return l

def indirectTargetBlock(x):
    if x.distance != 0:
        print(f"{x.name} has [Distance {x.distance}] and is out of range!")

def alwaysHit(char,skill,target):
    if char.precision != 0 or "Precision" in skill.effect:
        print(f"Precision! Hit {target.name}.")
        return True
    return False

def recoverEffects(value,valueT,status,statusD,statusA,char):
    healHP = []
    healSP = ["Bold"]
    if status in healHP:
        before = char.hp
        char.hp += value
        gain = char.hp - before
        print(f"{char.name} recovered {gain} HP due to {statusD}.")
    if status in healSP:
        before = char.sp
        char.sp += value
        gain = char.sp - before
        print(f"{char.name} recovered {gain} SP due to {statusD}.")

def drainEffects(value,valueT,status,statusD,statusA,char):
    drainHP = ["Burn"]
    drainSP = ["Burn","Terror"]
    if status in drainHP:
        before = char.hp
        char.hp -= value
        lost = before - char.hp
        print(f"{char.name} lost {lost} HP due to {statusD}.")
    if status in drainSP:
        before = char.sp
        char.sp -= value
        lost = before - char.sp
        print(f"{char.name} lost {lost} SP due to {statusD}.")

def interceptEffects(l):
    for x in l:
        x.intercept = 1
        x.intercept += x.taunt
        x.intercept += tauntPassives(x)

def autoTarget(char,skill,target):
    if char.scope != 0 or "Scope" in skill.effect:
        print(f"Scope! Targeting {target.name}.")
        return True
    return False

def cleanse(char,effect):
    removeList = []
    removeStat = [False,False]
    if "Cure" in effect:
        removeList += debuffList
        removeStat[1] = True
        eName = "Cure"

    for status in removeList:
        statusA = status.lower() if not isinstance(status,list) else status[1]
        statusD = status if not isinstance(status,list) else status[0]
        value = getattr(char, statusA)
        if value != 0:
            setattr(char, statusA, 0)
            print(f"{statusD} {value} was removed from {char.name} due to {eName}.")

    if True in removeStat:
        stats = ["maxHp", "maxSp", "atk", "mag", "dfn", "res", "spd", "eva", "acc"]
        for stat in stats:
            statC = stat + "C"
            statT = stat + "T"
            valueC = getattr(char, statC)
            change_made = False

            if (valueC > 0 and removeStat[0]) or (valueC < 0 and removeStat[1]):
                change_value = abs(valueC)
                change_sign = "-" if valueC < 0 else "+"
                change_string = f"{change_sign}{change_value} {stat.upper()}"
                setattr(char, statC, 0)
                print(f"{change_string} was removed from {char.name} due to {eName}.")

def oppositeCheck(char,skill,target):
    if skill.id == 184:
        print(f"Swapping defensive stat.")
        return True
    return False

#//ANCHOR INDIVIDUAL MECHANICS (The beginning of the end)
def supportInput(char,skill,target):
    if skill.id == 17: #Reimu's Great Hakurei Barrier
        print ("(1) +3 DEF or\n(2) +3 RES?")
        n = ask(1,2)
        if n == 1:
            skill.inflict = {"DFN":3}
        if n == 2:
            skill.inflict = {"RES":3}

def uniqueSupports(char,skill,target):
    stats = ["maxHpC","maxSpC","atkC","magC","dfnC","resC","spdC","evaC","accC"]
    for tar in target:
        if skill.id == 74: #Gaius's Steal
            charStats = {}
            targetStats = {}
            for stat in stats:
                value = getattr(tar, stat)
                if value != 0:
                    charStats[stat[:-1].upper()] = value
                    targetStats[stat[:-1].upper()] = "R"
            for status in statusList:
                statusA = status.lower() if not isinstance(status,list) else status[1]
                statusD = status if not isinstance(status,list) else status[0]
                value = getattr(tar,statusA)
                if value != 0:
                    charStats[statusD] = value
                    targetStats[statusD] = "R"
            applyStatus(char,targetStats,tar)
            applyStatus(char,charStats,char)
    if skill.id == 127:
        party = alive(onTeam(allCharacters(),char))
        tug = None
        for x in party:
            if x.id == 60:
                tug = x
                party.remove(tug)
                swapSelect(char,party,tug)

def costXSP(char,skill):
    if skill.id == 27:#Marisa's Master Spark
        return True
    if skill.id == 106:#Therion's Share SP
        return True
    return False

def beforeCost(char,skill):
    if skill.id == 27: #Marisa's Master Spark
        skill.cost = f"{char.sp} SP"
        skill.damage = char.sp-3
        print(f"{skill.name}'s damage is {char.sp} - 3 = {skill.damage}.")
    if skill.id == 106: #Therion's Share SP
        print(f"Choose the value of X, a number between 0 and {char.sp}.")
        skill.x = ask(0,char.sp)
        skill.cost = f"{skill.x} SP"
        skill.inflict = {"RecoverSP":skill.x}

def beforeDamage(char,skill,target,crit):
    refreshStats()
    if 62 in char.pids: #Momiji's Eyes that Perceive Reality
        if target.dfn > target.dfnB:
            print(f"-Eyes that Perceive Reality-\n{char.name} ignores {target.name}'s +{target.dfnC} DEF.")
            target.dfn = target.dfnB
        if target.res > target.resB:
            print(f"-Eyes that Perceive Reality-\n{char.name} ignores {target.name}'s +{target.resC} RES.")
            target.res = target.resB

    if 151 in char.pids:#Youmu
        if char.hp == char.maxHp:
            print(f"-Phantom Half-\n{char.name} deals +3 damage while at max HP.")
            crit += 3

    if skill.id == 54: #Emilie's Beatdown
        if char.spdC >= 3:
            skill.damage = 3
            print(f"+{char.spdC} SPD, {skill.name} does +1 damage.")
        else:
            skill.damage = 2 
    
    if skill.id == 57: #Emilie's Azure Strike
        skill.damage = char.spd - target.spd
        print(f"{char.name}'s SPD {char.spd} - {target.name}'s SPD {target.spd} = {skill.damage} damage.")

    if skill.id == 107: #Therion's Aeber's Reckoning
        skill.damage = char.spd*2
        print(f"{char.name}'s SPD {char.spd} * 2 = {skill.damage} damage.")

    if skill.id == 175: #Vaike
        skill.damage = 10 - char.spd
        print(f"5 - {char.name}'s SPD {char.spd} = X\n[Impact 5 + X] = [Impact {skill.damage}]")

    if skill.id == 195: #minoriko
        skill.damage = char.res
        print(f"{char.name}'s RES {char.res} = {skill.damage} damage.")

    return crit

def beforeBlock(char,skill,target,damage):
    e = skill.inflict
    effects = ["damage"]
    for effect in effects:
        if effect in e:
            if effect == "damage": # For % *damage
                if not e[effect][0] >= random.randint(1,100):
                    print(f"Unlucky... ({e[effect][1]}*damage does not activate)")
                else:
                    damage *= e[effect][1]
                    print(f"Lucky!!! (Damage multiplied by {e[effect][1]})")
    return damage

def onHitEffects(char,skill,target):
    if 101 in char.pids and target.sp != 0:
        target.sp -= 1
        print(f"-Snatch-\n{target.name} loses 1 SP.")
    if 111 in char.pids and target.terror != 0:
        print(f"-Troubled Forgotten Item-")
        applyStatus(char,{"RecoverHP":5,"RecoverSP":8},char)

def endOfTurnEffects(char):
    if 91 in char.pids:#Stahl's The Exact Median of the Army
        statDict = getStatChangeDict(char)
        party = alive(onTeam(inFront(),char))
        if char in party:
            party.remove(char) 
        if statDict and party:
            print("-The Exact Median of the Army-")
            applyStatus(char,statDict,party)
    
    if 161 in char.pids:#Sully
        party = alive(onTeam(inFront(),char,False))
        print(f"-Verbal Abuse-")
        applyStatus(char,{"ATK":-1},party)

def restStep(x):
    if 191 in x.pids:#Minoriko
        print(f"-Rapid Charge-")
        applyStatus(x,{"RecoverSP":2},x)

def endOfRound():
    for x in alive(allCharacters()):
        x.oncePerRound = True

def KOEffect(char):
    if 41 in char.pids:#Cirno's Blizzard Blowout
        e = {"SPD":-2}
        otherParty = alive(onTeam(inFront(),char,False))
        for x in otherParty:
            statChanges(char,e,x)

def effectOnKO(char,skill,target):
    if 71 in char.pids: #Gaius's Pay me in Candy
        print("-Pay me in Candy-")
        e = {"RecoverSP":6}
        recover(char,e,char)

def cleanupSkill(char,skill):
    if skill.id == 27:#Marisa's Master Spark
        skill.cost = "X SP"
    if skill.id == 106:#Therion's Share SP
        skill.cost = "X SP"

def startOfTurn(char):
    if 61 in char.pids: # Momiji's Ability to See Far Distances
        print("-Ability to See Far Distances-")
        e = {"ACC":2}
        party = alive(onTeam(inFront(),char))
        for x in party:
            statChanges(char,e,x)

def beforeAccuracy(char,skill,target):
    if 62 in char.pids: #Momiji's Eyes that Perceive Reality
        if target.eva > target.evaB:
            print(f"-Eyes that Perceive Reality-\n{char.name} ignores {target.names}'s +{target.evaC} EVA.")
            target.eva = target.evaB

def autoMiss(char,skill,target):
    if skill.id == 87: #Parsee's Jealousy of the Kind and Lovely
        if target.terror != 0:
            return False
        else:
            print(f"{target.name} is not terrified and cannot be hit.")
            return True
        
    if skill.id == 165: #Sully's Swordbreaker
        dt = "Blade"
        for x in getDamageTypes(target):
            if dt in x:
                return False
        print(f"{target.name} wields no {dt} skills, {skill.name} is ineffective.")
        return True
    return False

def uncappedHP(char):
    if 201 in char.pids:
        return True
    return False

def uncappedSP(char):
    if 101 in char.pids:
        return True
    return False

def updateVaribles(char):
    for x in getSkillList(char):
        if x.id == 104:
            x.x = x.damageDealt * 2

def selfEffect(char,skill):
    updateVaribles(char)
    if skill.id == 104:
        skill.self = {"RecoverSP":skill.x}

def tauntPassives(x):
    if 141 in x.pids:#Olberic
        print(f"-Cover-\n{x.name} has Taunt 2.")
        return 2
    return 0

def startOfGame():
    refreshSlot()
    for x in allCharacters():
        if 171 in x.pids and x.slot <= 4:
            print(f"-Slightly Forgetful-")
            applyStatus(x,{"Weaken":1,"Disable":1},x)

def formation(char):
    party = alive(onTeam(inFront(),char))
    if 181 in char.pids:#Keine
        print("-Organized Formation-")
        applyStatus(char,{"RecoverSP":2},party)

#//ANCHOR -Common Passives
def rallyEffects(char):
    if 11 in char.pids:#Reimu's Grand Incantation
        if char.crit < 3:
            print(f"-Grand Incantation-")
            e = {"Crit":3}
            statuses(char,e,char)
    if 131 in char.pids:#Komachi's Slacking Off
        print("-Slacking Off-")
        applyStatus(char,{"RecoverHP":6},char)
    if 151 in char.pids:#Youmu
        print("Intense Concentration")
        applyStatus(char,{"DFN":1,"RES":1,"EVA":2},char)
    if 191 in char.pids:#Minoriko
        print(f"-Rapid Charge-")
        applyStatus(char,{"RecoverSP":4},char)

def typeBoost(char,skill):
    party = alive(onTeam(inFront(),char))
    boost = 0
    damageTypes = [["Mystic",21,"Magic Overflowing"],
                 ["Dark",81,"Flames of Jealousy"]]
    for x in party:
        for type in damageTypes:
            if type[1] in x.pids and type[0] in skill.damageType:
                boost += 1
                print(f"-{type[2]}-\n{type[0]} damage increased by 1.")
    return boost

def swapEffect(target1,target2):
    for x in [target1,target2]:
        if not x.KO:
            if 31 in x.pids and x.oncePerRound: #Chen's Instant Attack
                print(f"-Instant Attack-\n{x.name} recovered her turn.")
                x.turn = True
                x.oncePerRound = False
            if 121 in x.pids and x.crit <= 3:
                print(f"-Unseen Movement-\n{x.name} gains [Crit 3].")
                applyStatus(x,{"Crit":3},x)
            if 171 in x.pids:
                print(f"-Slightly Forgetful-")
                applyStatus(x,{"Weaken":1,"Disable":1},x)
    #Swap In Effects
    swappedIn = None
    if target1.slot >= 5 and target2.slot < 5:
        swappedIn = target1
    if target1.slot < 5 and target2.slot >= 5:
        swappedIn = target2
    if swappedIn:
        if 51 in swappedIn.pids: #Emilie's Dashing In
            e = {"SPD":3}
            print("-Dashing In-")
            statChanges(swappedIn,e,swappedIn)

#//ANCHOR Test Section
testA = ["Player A",
            wikiToClass(18),
            wikiToClass(16),
            wikiToClass(17),
            wikiToClass(12),
            wikiToClass(2),
            wikiToClass(3),
            wikiToClass(4),
            wikiToClass(5)]
testB = ["Player B",
            wikiToClass(15),
            wikiToClass(19),
            wikiToClass(20),
            wikiToClass(6),
            wikiToClass(7),
            wikiToClass(8),
            wikiToClass(9),
            wikiToClass(10)]

main()