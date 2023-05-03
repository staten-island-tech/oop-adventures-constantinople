import Classes
import random
from Classes import Base_class, Enemy1


B = Enemy1(160 ,30)


class Faceless(Base_class):
    def __init__(self, HP, Weapon, XP):
        super().__init__(HP, Weapon, XP)
    def Attack(self):
        while B.HP > 0:
            if B.HP < 0:
                break  
            OL = input('Damage the enemy?').upper()
            if OL == 'YES':
                Number_of_hits = random.randint(0 , 4)
                Damage = int(30)
                Total_DMG = Number_of_hits*Damage
                Remaing_enemy_HP = B.HP - Total_DMG
                if Remaing_enemy_HP < 0:
                    print('You defeated this enemy')
                    Added_XP = B.XP + po.XP
                    po.XP = Added_XP
                    print('You now have,' , Added_XP , 'XP')
                    break
                B.HP = Remaing_enemy_HP
                print(Remaing_enemy_HP)
            if OL != 'YES':
                print('You dont attack')
                break    

po = Faceless(105 , 'something' , 0)

class oni(Base_class):
    def __init__(self, HP, Weapon, XP):
        super().__init__(HP, Weapon, XP)
    def Attack(self):
        while B.HP > 0:
            if B.HP < 0:
                break  
            OL = input('Damage the enemy?').upper()
            if OL == 'YES':
                Number_of_hits = random.randint(0 , 8)
                Damage = int(10)
                Total_DMG = Number_of_hits*Damage
                Remaing_enemy_HP = B.HP - Total_DMG
                if Remaing_enemy_HP < 0:
                    print('You defeated this enemy')
                    Added_XP = B.XP + op.XP
                    op.XP = Added_XP
                    print('You now have,' , Added_XP , 'XP')
                    break
                B.HP = Remaing_enemy_HP
                print(Remaing_enemy_HP)
            if OL != 'YES':
                print('You dont attack')
                break    

op = oni(115 , 'something' , 0)

class replay1():
    def replay(x):
        x.Attack()
        lol = input('Would you like to go again ').upper()
        while lol == 'YES':
            B.HP = 160
            x.Attack()
            lol = input('Would you like to go again ').upper()
            if lol != 'YES':
                print('You dont attack')
                break
""" replay1.replay(op) """