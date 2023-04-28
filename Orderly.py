import random
class Base_class:
    def __init__(self, HP , Weapon , Money , XP):
        self.HP = int(HP)
        self.Weapon = Weapon
        self.Money = int(Money)
        self.XP = int(XP)
    def info(self):
        print(self.HP , self.Weapon , self.Money , self.XP)
    def Attack(self):
        while B.HP > 0:
            if B.HP < 0:
                break  
            OL = input('Would you like to attack?').upper()
            if OL == 'YES':
                Number_of_hits = random.randint(0 , 5)
                Damage = int(25)
                Total_DMG = Number_of_hits*Damage
                Remaing_enemy_HP = B.HP - Total_DMG
                if Remaing_enemy_HP < 0:
                    print('You defeated this enemy')
                    Added_XP = B.XP + A.XP
                    A.XP = Added_XP
                    print('You now have,' , Added_XP , 'XP')
                    break
                B.HP = Remaing_enemy_HP
                print(Remaing_enemy_HP)




class Enemy1:
    def __init__(self, HP , XP):
        self.HP = HP
        self.XP = XP
B = Enemy1(150 , 25 )

class sigil_Knight(Base_class):
    def __init__(self, HP, Weapon, Money, XP):
        super().__init__(HP, Weapon, Money, XP)
    def Attack(self):
        while B.HP > 0:
            if B.HP < 0:
                break  
            OL = input('Would you like to attack?').upper()
            if OL == 'YES':
                Number_of_hits = random.randint(0 , 5)
                Damage = int(25)
                Total_DMG = Number_of_hits*Damage
                Remaing_enemy_HP = B.HP - Total_DMG
                if Remaing_enemy_HP < 0:
                    print('You defeated this enemy')
                    Added_XP = B.XP + A.XP
                    A.XP = Added_XP
                    print('You now have,' , Added_XP , 'XP')
                    break
                B.HP = Remaing_enemy_HP
                print(Remaing_enemy_HP)
                
class Whisperer(Base_class):
    def __init__(self, HP, Weapon, Money, XP):
        super().__init__(HP, Weapon, Money, XP)             
def Attack(self):
        while C.HP > 0:
            if C.HP < 0:
                break  
            OL = input('Would you like to attack?').upper()
            if OL == 'YES':
                Number_of_hits = random.randint(0 , 3)
                Damage = int(15)
                Total_DMG = Number_of_hits*Damage
                Remaing_enemy_HP = C.HP - Total_DMG
                if Remaing_enemy_HP < 0:
                    print('You defeated this enemy')
                    Added_XP = B.XP + C.XP
                    C.XP = Added_XP
                    print('You now have,' , Added_XP , 'XP')
                    break
                B.HP = Remaing_enemy_HP
                print(Remaing_enemy_HP)


A = sigil_Knight(100, 'x', 0 , 0)
C = Whisperer(125, 'somthing' , 0 , 0)
A.Attack
C.Attack()
print(A.XP)
