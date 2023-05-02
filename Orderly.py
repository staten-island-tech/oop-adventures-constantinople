import Classes
import random
from Classes import Base_class, Enemy1
B = Enemy1(160 ,30)

class sigil_Knight(Base_class):
    def __init__(self, HP, Weapon, XP):
        super().__init__(HP, Weapon, XP)
    def Attack(self):
        while B.HP > 0:
            if B.HP < 0:
                break  
            OL = input('Damage the enemy?').upper()
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
            if OL != 'YES':
                print('You dont attack')
                break
                
class Whisperer(Base_class):
    def __init__(self, HP, Weapon, XP):
        super().__init__(HP, Weapon, XP)             
    def Attack(self):
        while B.HP > 0:
            if B.HP < 0:
                break  
            OL = input('Damage the enemy?').upper()
            if OL == 'YES':
                Number_of_hits = random.randint(0 , 6)
                Damage = int(15)
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
            if OL != 'YES':
                print('You dont attack')
                break

A = sigil_Knight(100 , 'something' , 0)
C = Whisperer(150 , 'something' , 0)





