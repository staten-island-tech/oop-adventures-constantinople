import random
import base_file
from base_file import Base_class, B , Bossattack
import weapons
from weapons import mythril_Dagger


class Faceless(base_file):
    def __init__(self, HP, Weapon, XP):
        super().__init__(HP, Weapon, XP)
    def Attack(x, y):
        while x.HP > 0:
            if x.HP < 0:
                break  
            OL = input('Swing your weapon at the enemy?').upper()
            if OL == 'YES':
                Number_of_hits = random.randint(0 , 4)
                Damage = y
                Total_DMG = Number_of_hits*Damage
                if Total_DMG == 0:
                    print('You Have seemed to miss the enemy...... How could you let this happen')
                Remaing_enemy_HP = x.HP - Total_DMG
                if Remaing_enemy_HP < 0 or Remaing_enemy_HP == 0:
                    print('You defeated this enemy')
                    Added_XP = x.XP + po.XP
                    po.XP = Added_XP
                    print('You now have,' , Added_XP , 'XP')
                    break
                x.HP = Remaing_enemy_HP
                print(f"The enemy now has {Remaing_enemy_HP} HP left")
            if OL != 'YES':
                print('You dont attack')
                break    

        



po = Faceless(105 , 'Weapon' , 0)
po

class oni(Base_class):
    def __init__(self, HP, Weapon, XP):
        super().__init__(HP, Weapon, XP)
    def Attack(x,y):
        while x.HP > 0:
            if x.HP < 0:
                break  
            OL = input('Swing your weapon at the enemy?').upper()
            if OL == 'YES':
                Number_of_hits = random.randint(0 , 4)
                Damage = y
                Total_DMG = Number_of_hits*Damage
                if Total_DMG == 0:
                    print('You Have seemed to miss the enemy...... How could you let this happen')
                Remaing_enemy_HP = x.HP - Total_DMG
                if Remaing_enemy_HP < 0 or Remaing_enemy_HP == 0:
                    print('You defeated this enemy')
                    Added_XP = x.XP + op.XP
                    op.XP = Added_XP
                    print('You now have,' , Added_XP , 'XP')
                    break
                x.HP = Remaing_enemy_HP
                print(f"The enemy now has {Remaing_enemy_HP} HP left")
            if OL != 'YES':
                print('You dont attack')
                break    


op = oni(115 , 'something' , 0)


