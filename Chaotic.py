import random
import base_file
from base_file import Base_class, B

bronze_sword = int(9)
silver_sword = int(10)
mythril_sword = int(14)
fists = int(6)
dagger = int(9)
rapier = int(11)
fists2 = int(11)
bronze_Dagger = int(7) 
silver_Dagger = int (10)
mythril_Dagger = int (13)
bronze_Pan = int(5)
silver_Pan = int(9)
mythril_Pan = int(12)
bronze_Hammer = int(8) 
silver_Hammer = int(10)
mythril_Hammer = int(13)



class Faceless(Base_class):
    def __init__(self, HP, Weapon, XP):
        super().__init__(HP, Weapon, XP)
    def Attack(self,x,y):
        while x.HP > 0:
            if x.HP < 0:
                break  
            OL = input('Swing your weapon at the enemy?').upper()
            if OL == 'YES':
                Number_of_hits = random.randint(0 , 4)
                Damage = y
                Total_DMG = Number_of_hits*Damage
                Remaing_enemy_HP = x.HP - Total_DMG
                if Remaing_enemy_HP < 0 or Remaing_enemy_HP == 0:
                    print('You defeated this enemy')
                    Added_XP = x.XP + po.XP
                    po.XP = Added_XP
                    print('You now have,' , Added_XP , 'XP')
                    break
                x.HP = Remaing_enemy_HP
                print(Remaing_enemy_HP)
            if OL != 'YES':
                print('You dont attack')
                break    

po = Faceless(105 , 'something' , 0)

po.Attack(B,silver_Dagger)

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
                if Remaing_enemy_HP < 0 or Remaing_enemy_HP == 0:
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
