
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
        self.hp = 10
        self.sp = 10
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

wikiList = [Reimu()]