class Base_class:
    def __init__(self, HP , Weapon , Money , XP):
        self.HP = HP
        self.Weapon = Weapon
        self.Money = int(Money)
        self.XP = int(XP)

class Oni(Base_class):
    def __init__(self, HP, Weapon, Money, kills,):
        super().__init__(HP, Weapon, Money)
        self.kills = int(kills)
    

class Faceless(Base_class):
    def __init__(self, HP, Weapon, Money, kills):
        super().__init__(HP, Weapon, Money)
        self.kills = int(kills)
Mathew = Oni(100,"Sword",1000,1)