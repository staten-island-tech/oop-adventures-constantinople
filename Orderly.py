class Base_class:
    def __init__(self, HP , Weapon , Money , XP):
        self.HP = int(HP)
        self.Weapon = Weapon
        self.Money = int(Money)
        self.XP = int(XP)
    def info(self):
        print(self.HP , self.Weapon , self.Money , self.XP)

enemy = int(150)

class sigil_Knight(Base_class):
    def __init__(self, HP, Weapon, Money, XP):
        super().__init__(HP, Weapon, Money, XP)
    def Attack(self):
        Damage = int(75)
        Remaing_enemy_HP = enemy - Damage
        print(Remaing_enemy_HP)
A = sigil_Knight(100, "longsword" , 0 , 0)
A.info()
A.Attack()



