class Base_class:
    def __init__(self, HP , Weapon , Money , XP):
        self.HP = int(HP)
        self.Weapon = Weapon
        self.Money = int(Money)
        self.XP = int(XP)
    def info(self):
        print(self.HP , self.Weapon , self.Money , self.XP)



class sigil_Knight(Base_class):
    def __init__(self, HP, Weapon, Money, XP):
        super().__init__(HP, Weapon, Money, XP)
    
A = sigil_Knight(100, "longsword" , 0 , 0)
A.info()


