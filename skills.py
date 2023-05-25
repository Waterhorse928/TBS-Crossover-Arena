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
        self.inflict = []

def base(self):
    pass

class Temp(Skill):
    def __init__(self,name,display,id,skillType,costType,cost,target,damageType,damage,inflict):
        super().__init__()
        self.name = name
        self.display = display
        self.id = id
        self.skillType = skillType
        self.costType = costType
        self.cost = cost
        self.target = target
        self.damageType = damageType
        self.damage = damage
        self.inflict = inflict
        base(self)