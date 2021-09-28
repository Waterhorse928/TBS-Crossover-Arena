import icons

class Char:
    def __init__(self):
        self.name = "I AM ERROR."
        self.hp = 10
        self.sp = 10
        self.atk = 0
        self.mag = 0
        self.dfn = 0
        self.res = 0
        self.spd = 0
        self.eva = 0
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
        self.image = icons.QUESTION

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
        self.image = icons.QUESTION
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
        base(self)

class Aya(Char):
    def __init__(self):
        super().__init__()
        self.name = "Aya"
        self.hp = 5
        self.sp = 6
        self.dfn = 1
        self.res = 0
        self.spd = 9
        self.eva = 6
        self.image = icons.AYA
        base(self)

class Saitama(Char):
    def __init__(self):
        super().__init__()
        self.name = "Saitama"
        self.hp = 99
        self.sp = 99
        self.dfn = 30
        self.res = 30
        self.spd = 20
        self.eva = 20
        base(self)

class Momiji(Char):
    def __init__(self):
        super().__init__()
        self.name = "Momiji"
        self.hp = 8
        self.sp = 4
        self.dfn = 4
        self.res = 2
        self.spd = 6
        self.eva = 2
        self.image = icons.QUESTION
        base(self)