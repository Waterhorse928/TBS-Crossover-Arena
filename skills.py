class Skill:
    def __init__(self):
        self.name = "WHOOPS"
        self.display = "WHOOPS\n[ATK] Cost 0\nOne Enemy : [Impact 2]"
        self.id = 0
        self.skillType = "ATK"
        self.costType = "SP"
        self.cost = "0"
        self.target = "One Enemy"
        self.damageType = "Impact"
        self.damage = "2"
        self.inflict = {}
        self.accuracy = "0"

def base(self):
    pass

class Temp(Skill):
    def __init__(self,name,display,id,skillType,cost,target,damageType,damage,inflict,accuracy):
        super().__init__()
        self.name = name
        self.display = display
        self.id = id
        self.skillType = skillType
        self.cost = cost
        self.target = target
        self.damageType = damageType
        self.damage = damage
        self.inflict = inflict
        self.accuracy = accuracy
        base(self)