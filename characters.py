
class Char:
    def __init__(self):
        self.name = "I AM ERROR."
        self.slot = 0
        self.hp = 1
        self.sp = 1
        self.dfn = 0
        self.res = 0
        self.spd = 0
        self.eva = 0
        self.fullname = "I AM ERROR, YES IT'S TRUE. I AM ERROR, HOW ABOUT YOU?"
        self.pronoun = ["they","their"]
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
        self.status = []
        self.id = "000"
        self.pids = []
        self.acc = 0
        self.atk = 0
        self.mag = 0
        self.intercept = 1
        self.maxHp = self.hp
        self.maxSp = self.sp
        self.maxHpC = 0
        self.maxSpC = 0
        self.atkC = 0
        self.magC = 0
        self.dfnC = 0
        self.resC = 0
        self.spdC = 0
        self.evaC = 0
        self.accC = 0
        self.maxHpT = False
        self.maxSpT = False
        self.atkT = False
        self.magT = False
        self.dfnT = False
        self.resT = False
        self.spdT = False
        self.evaT = False
        self.accT = False
        self.turn = False
        self.KO = False
        self.slot = 0
        self.oncePerRound = True
        #status effects
        self.crit = 0
        self.critT = False
        self.paralysis = 0
        self.paralysisT = False
        self.burn = 0
        self.burnT = 0
        self.brea = 0
        self.breaT = 0
        self.terror = 0
        self.terrorT = 0
        self.silence = 0
        self.silenceT = 0
        self.weaken = 0
        self.weakenT = 0
        self.precision = 0
        self.precisionT = 0
        self.death = 0
        self.deathT = 0
        self.distance = 0
        self.distanceT = 0
        self.taunt = 0
        self.tauntT = 0
        self.scope = 0
        self.scopeT = 0
        self.cure = 0
        self.cureT = 0
        self.disable = 0
        self.disableT = 0
        self.bold = 0
        self.boldT = 0

def base(self):
    self.maxHpB = self.hp
    self.maxSpB = self.sp
    self.atkB = 0
    self.magB = 0
    self.dfnB = self.dfn
    self.resB = self.res
    self.spdB = self.spd
    self.evaB = self.eva
    self.accB = 0

class Template(Char):
    def __init__(self,a0,a1,a2,a3,a4,a5,a6,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22):
        super().__init__()
        self.name = a0
        self.hp = a1
        self.sp = a2
        self.dfn = a3
        self.res = a4
        self.spd = a5
        self.eva = a6
        self.fullname = a11
        self.p1 = a12
        self.p2 = a13
        self.p3 = a14
        self.s1 = a15
        self.s2 = a16
        self.s3 = a17
        self.s4 = a18
        self.s5 = a19
        self.passives = a20
        self.skills = a21
        self.id = a22
        self.maxHp = self.hp
        self.maxSp = self.sp
        for x in range(1,self.passives+1):
            self.pids.append((self.id*10)+x)
        base(self)