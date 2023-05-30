import Chaotic
from Chaotic import po
import base_file
from base_file import B
import weapons
from weapons import mythril_sword


class replay1():
    def replay(x,y):
        print("before function")
        y.HP = int(160)
        x.Attack(y,mythril_sword)
        ask = input('Another one enemy approachs. Attack or run?').upper()
        while ask == 'ATTACK':
            y.HP = int(160)
            print('test1')
            x.Attack(y,mythril_sword)
            print('test2')
            ask = input('Another one enemy approachs. Attack or run?').upper()
replay1.replay(po,B)



""" 


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
                break     """