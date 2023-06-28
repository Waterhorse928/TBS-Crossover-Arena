
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
        self.intercept = 1
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
        self.turn = False
        self.KO = False
        self.slot = 0

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
        base(self)