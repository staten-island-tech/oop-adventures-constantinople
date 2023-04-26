import random
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
        Number_of_hits = random.randint(0 , 5)
        Damage = int(25)
        Total_DMG = Number_of_hits*Damage
        Remaing_enemy_HP = enemy - Total_DMG
        print(Remaing_enemy_HP)

A = sigil_Knight(100, "longsword" , 0 , 0)

OL = input('Would you like to attack?')
OL.upper()
print(OL)
if OL == 'YES':
    A.Attack()
elif OL:
    print('You backed away from the attack')







