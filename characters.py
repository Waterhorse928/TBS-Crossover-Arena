
class Char:
    def __init__(self):
        self.name = "I AM ERROR."
        self.hp = 10
        self.sp = 10
        self.dfn = 0
        self.res = 0
        self.spd = 0
        self.eva = 0
        self.fullname = "I AM ERROR, YES IT'S TRUE. I AM ERROR, HOW ABOUT YOU?"
        self.p1 = ""
        self.p2 = ""
        self.p3 = ""
        self.s1 = ""
        self.s2 = ""
        self.s3 = ""
        self.s4 = ""
        self.s5 = ""
        self.passives = 0
        self.skills = 0
        self.id = "000"
        self.acc = 0
        self.maxHp = self.hp
        self.maxSp = self.sp
        self.atkC = 0
        self.magC = 0
        self.dfnC = 0
        self.resC = 0
        self.spdC = 0
        self.evaC = 0
        self.accC = 0
        self.atkT = 0
        self.magT = 0
        self.dfnT = 0
        self.resT = 0
        self.spdT = 0
        self.evaT = 0
        self.accT = 0
        self.action = False
        self.KO = False

def base(self):
    self.maxHp = self.hp
    self.maxSp = self.sp
    self.atkB = 0
    self.magB = 0
    self.dfnB = self.dfn
    self.resB = self.res
    self.spdB = self.spd
    self.evaB = self.eva
    self.accB = 0


class Template(Char):
    def __init__(self):
        super().__init__()
        self.name = "I AM ERROR."
        self.hp = 1
        self.sp = 1
        self.dfn = 0
        self.res = 0
        self.spd = 0
        self.eva = 0
        self.fullname = "I AM ERROR"
        self.p1 = ""
        self.p2 = ""
        self.p3 = ""
        self.s1 = ""
        self.s2 = ""
        self.s3 = ""
        self.s4 = ""
        self.s5 = ""
        self.passives = 0
        self.skills = 0
        self.id = "000"
        base(self)

class Reimu(Char):
    def __init__(self):
        super().__init__()
        self.name = "Reimu"
        self.hp = 5
        self.sp = 9
        self.dfn = 1
        self.res = 1
        self.spd = 5
        self.eva = 1
        self.fullname = "Reimu Hakurei"
        self.p1 = "Grand Incantation\nWhen Reimu rallies, she gains [Crit 3]."
        self.p2 = ""
        self.p3 = ""
        self.s1 = "Yin-Yang Orb\n[ATK] Cost 2 SP\nSingle Enemy: [Spirit 3]"
        self.s2 = "Fantasy Seal\n[MAG] Cost 3 SP\nAll Enemies: [Spirit 3]\nThis Skill has -1 ACC. "
        self.s3 = "Exorcising Border\n[SUP] Cost 3 SP\nAll Allies : Recover 3 HP."
        self.s4 = "Great Hakurei Barrier\n[SUP] Cost 5 SP\nAll Allies : [+3 DEF] or [+3 RES]"
        self.s5 = ""
        self.passives = 1
        self.skills = 4
        self.id = "001"
        base(self)

class Marisa(Char):
    def __init__(self):
        super().__init__()
        self.name = "Marisa"
        self.hp = 3
        self.sp = 18
        self.dfn = 0
        self.res = 1
        self.spd = 7
        self.eva = 3
        self.fullname = "Marisa Kirisame"
        self.p1 = "Magic Overflowing\nWhile this unit is in front,\nall Mystic damage is increased by 1."
        self.p2 = ""
        self.p3 = ""
        self.s1 = "Magic Missile\n[MAG] Cost 2 SP\nSingle Enemy: [Mystic 4]"
        self.s2 = "Asteroid Belt\n[MAG] Cost 4 SP\nAll Enemies: [Mystic 3]\nThis Skill has -1 ACC."
        self.s3 = "Concentration\n[SUP] Cost 3 SP\nSelf: [+3 SP] Recover 6 SP."
        self.s4 = "Master Spark\n[MAG] Cost X SP\nAll Enemies: [Mystic Y]\nThis Skill has -1 ACC.\nX = Marisa's current SP.\nY = X - 3"
        self.s5 = ""
        self.passives = 1
        self.skills = 4
        self.id = "002"
        base(self)

class Chen(Char):
    def __init__(self):
        super().__init__()
        self.name = "Chen"
        self.hp = 3
        self.sp = 3
        self.dfn = 0
        self.res = 0
        self.spd = 10
        self.eva = 5
        self.fullname = "Chen"
        self.p1 = "Instant Attack\nWhen Chen is swapped,\nShe recovers her turn this round."
        self.p2 = ""
        self.p3 = ""
        self.s1 = "Flight of Idaten\n[ATK] Cost 1 SP\nOne Enemy : [Pierce 3]"
        self.s2 = "Phoenix Spread Wings\n[ATK] Cost 2 SP\nTwo Enemies : [Fire 2]"
        self.s3 = "Kimontonkou\n[SUP] Cost 1 SP\nSelf : [+3 ATK]"
        self.s4 = ""
        self.s5 = ""
        self.passives = 1
        self.skills = 3
        self.id = "003"
        base(self)

class Cirno(Char):
    def __init__(self):
        super().__init__()
        self.name = "Cirno"
        self.hp = 4
        self.sp = 7
        self.dfn = 2
        self.res = 2
        self.spd = 7
        self.eva = 3
        self.fullname = "Cirno"
        self.p1 = "Blizzard Blowout\nWhen this unit is KO'ed,\nAll front enemies gain [-2 SPD]."
        self.p2 = ""
        self.p3 = ""
        self.s1 = "Icicle Fall\n[ATK] Cost 2 SP\nOne Enemy: [Cold 2] [-3 SPD]"
        self.s2 = "Diamond Blizzard\n[ATK] Cost 6 SP\nAll Enemies: [Cold 4] [Paralysis 1]\nThis Skill has -1 ACC."
        self.s3 = "Perfect Freeze\n[ATK] Cost 5 SP\nAll Enemies: [Cold 3] {50% -3 SPD}\nThis Skill has -1 ACC."
        self.s4 = "White Album\n[SUP] Cost 3 SP\nSelf: [+3 DEF, RES]"
        self.s5 = ""
        self.passives = 1
        self.skills = 4
        self.id = "004"
        base(self)

class Emilie(Char):
    def __init__(self):
        super().__init__()
        self.name = "Emilie"
        self.hp = 6
        self.sp = 8
        self.dfn = 1
        self.res = 0
        self.spd = 7
        self.eva = 4
        self.fullname = "Sophie de Belmond"
        self.p1 = "Dashing In\nWhen Emilie is switched in,\nShe gains [+3 SPD]."
        self.p2 = ""
        self.p3 = ""
        self.s1 = "Beatdown\n[ATK] Cost 2 SP\nTwo Enemies : [Impact 2]\nDeals +1 damage if Emilie has [+3 SPD]."
        self.s2 = "Faucon Poing\n[ATK] Cost 4 SP\nOne Enemy : [Fire 5] {20% Burn 3}"
        self.s3 = "Amber Thrust\n[ATK] Cost 6 SP\nAll Enemies : [Electric 2] [Paralysis 2]\nThis Skill has -1 ACC."
        self.s4 = "Azure Strike\n[ATK] Cost 4 SP\nOne Enemy : [Impact X]\nX = (Emilie' SPD) - (Target's SPD)"
        self.s5 = ""
        self.passives = 1
        self.skills = 4
        self.id = "005"
        base(self)

class Momiji(Char):
    def __init__(self):
        super().__init__()
        self.name = "Momiji"
        self.hp = 8
        self.sp = 9
        self.dfn = 4
        self.res = 2
        self.spd = 6
        self.eva = 2
        self.fullname = "Momiji Inubashiri"
        self.p1 = "Ability to See Far Distances\nAt the start of Momiji's turn,\nall allies gain [+2 ACC]."
        self.p2 = "Eyes that Perceive Reality\nMomiji ignores her target's Stat Boosts."
        self.p3 = ""
        self.s1 = "Rabies Bite\n[ATK] Cost 3 SP\nOne Enemy: [Pierce 3]\nThis Skill has Break 2 and +2 ACC."
        self.s2 = "Expellee's Canaan\n[ATK] Cost 4 SP\nAll Enemies: [Wind 3]\nThis Skill has -1 ACC."
        self.s3 = ""
        self.s4 = ""
        self.s5 = ""
        self.passives = 2
        self.skills = 2
        self.id = "006"
        base(self)

class Gaius(Char):
    def __init__(self):
        super().__init__()
        self.name = "Gaius"
        self.hp = 8
        self.sp = 7
        self.dfn = 1
        self.res = 0
        self.spd = 7
        self.eva = 4
        self.fullname = "Gaius"
        self.p1 = "Pay me in Candy\nWhen Gaius KOs a target,\nrecover 6 SP."
        self.p2 = ""
        self.p3 = ""
        self.s1 = "Steal\n[SUP] Cost 1 SP\nOne Target : All of the target's Status Effects\nare transferred onto Gaius."
        self.s2 = "Candied Dagger\n[ATK] Cost 3 SP\nOne Enemy: [3 Blade] {50% -2 DEF,RES}"
        self.s3 = "Levin Sword\n[MAG] Cost 2 SP\nOne Enemy: [3 Electric]"
        self.s4 = ""
        self.s5 = ""
        self.passives = 1
        self.skills = 3
        self.id = "007"
        base(self)

class Parsee(Char):
    def __init__(self):
        super().__init__()
        self.name = "Parsee"
        self.hp = 4
        self.sp = 7
        self.dfn = 2
        self.res = 4
        self.spd = 5
        self.eva = 6
        self.fullname = "Parsee Mizuhashi"
        self.p1 = "Flames of Jealousy\nWhen Parsee is in front,\nAll Dark damage is increased by 1."
        self.p2 = ""
        self.p3 = ""
        self.s1 = "Large Box and Small Box\n[ATK] Cost 3 SP\nOne Enemy: [Impact 2] {20% 3*damage}"
        self.s2 = "Midnight Anathema Ritual\n[ATK] Cost 1 SP\nOne Enemy: [Dark 0] {50% Terror 4, Silence 2}"
        self.s3 = "Grudge Returning\n[ATK] Cost 2 SP\nAll Enemies: [Dark 0] [Terror 2]\nThis Skill has -1 ACC."
        self.s4 = "Jealousy of the Kind and Lovely\n[ATK] Cost 4 SP\nAll Enemies: [Dark 6]\nOnly hits targets with Terror.\nThis Skill has -1 ACC."
        self.s5 = ""
        self.passives = 1
        self.skills = 4
        self.id = "008"
        base(self)

class Stahl(Char):
    def __init__(self):
        super().__init__()
        self.name = "Stahl"
        self.hp = 8
        self.sp = 8
        self.dfn = 2
        self.res = 2
        self.spd = 5
        self.eva = 1
        self.fullname = "Stahl"
        self.p1 = "The Exact Median of the Army\nAt the end of Stahl's turn,\nAll Other Allies gain Stahl's Stat Changes."
        self.p2 = ""
        self.p3 = ""
        self.s1 = "Apprentice Apothecary\n[SUP] Cost 2 SP\nOne Ally : Recover 4 HP."
        self.s2 = "Viridian Shield\n[SUP] Cost 2 SP\nSelf : [+2 ATK,DEF] [-2 SPD]"
        self.s3 = "Strike of the Panther\n[ATK] Cost 4 SP\nTwo Enemies : [Blade 4]"
        self.s4 = ""
        self.s5 = ""
        self.passives = 1
        self.skills = 3
        self.id = "009"
        base(self)

class Therion(Char):
    def __init__(self):
        super().__init__()
        self.name = "Therion"
        self.hp = 8
        self.sp = 10
        self.dfn = 1
        self.res = 1
        self.spd = 7
        self.eva = 3
        self.fullname = "Therion"
        self.p1 = "Snatch\nEnemies damaged by Therion's skills lose 1 SP.\nTherion's SP may go above his MAX SP."
        self.p2 = ""
        self.p3 = ""
        self.s1 = "Steal SP\n[ATK] Cost 2 SP\nOne Enemy : [Blade 3]\nSelf: Recover X SP.\nX = damage dealt * 2"
        self.s2 = "Wildfire\n[MAG] Cost 4 SP\nOne Enemy : [Fire 5]"
        self.s3 = "Share SP\n[SUP] Cost X SP\nOne Ally : Recover X SP.\nX may be any positive number."
        self.s4 = "Aeber's Reckoning\n[ATK] Cost 14 SP\nAll Enemies : [X Blade]\nX = Therion's SPD * 2\nThis Skill has -1 ACC."
        self.s5 = ""
        self.passives = 1
        self.skills = 4
        self.id = "010"
        base(self)

class Kogasa(Char):
    def __init__(self):
        super().__init__()
        self.name = "Kogasa"
        self.hp = 5
        self.sp = 8
        self.dfn = 3
        self.res = 1
        self.spd = 3
        self.eva = 0
        self.fullname = "Kogasa Tatara"
        self.p1 = "Troubled Forgotten Item\nWhen Kogasa hits an enemy affected by Terror,\nShe recovers 8 SP and 5 HP."
        self.p2 = ""
        self.p3 = ""
        self.s1 = "Karakasa Surprising Flash\n[ATK] Cost 3 SP\nAll Enemies: [Nature 2] {40% Terror 2}\nThis Skill has -1 ACC."
        self.s2 = "A Rainy Night's Ghost Story\n[ATK] Cost 2 SP\nOne Enemy: [Dark 2] {70% -2 RES} {70% Terror 3}"
        self.s3 = "Drizzling Large Raindrops\n[ATK] Cost 2 SP\nAll Enemies: [Water 1]\nThis Skill has -1 ACC."
        self.s4 = "Competent Blacksmith?\n[SUP] Cost 3 SP\nOne Ally : [+2 ATK,DEF]"
        self.s5 = ""
        self.passives = 1
        self.skills = 4
        self.id = "011"
        base(self)

class Will(Char):
    def __init__(self):
        super().__init__()
        self.name = "Will"
        self.hp = 1
        self.sp = 1
        self.dfn = 0
        self.res = 0
        self.spd = 0
        self.eva = 0
        self.fullname = "Will Treaty"
        self.p1 = "Unseen Movement\nWhen Will is swapped,\ngain [Crit 3]."
        self.p2 = ""
        self.p3 = ""
        self.s1 = "Expert Shot\n[ATK] Cost 4 SP\nOne Enemy : [Pierce 3]\nThis skill has Precision."
        self.s2 = "Unexpected Strategy\n[SUP] Cost 4 SP\nAll Enemies : [-2 DEF,RES]"
        self.s3 = "Double Knife Defense\n[SUP] Cost 1 SP\nOne Enemy : [Blade 1]\nSelf : [+2 DEF]"
        self.s4 = "Hit-and-Run Tactics\n[SUP] Cost 3 SP\nOne Enemy : [Terror 2]\nSwap an ally Tug."
        self.s5 = ""
        self.passives = 1
        self.skills = 4
        self.id = "012"
        base(self)



wikiList = ["",Reimu(),Marisa(),Chen(),Cirno(),Emilie(),Momiji(),Gaius(),Parsee(),Stahl(),Therion(),Kogasa(),Will()]