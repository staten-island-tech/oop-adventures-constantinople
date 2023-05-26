import Chaotic
from Chaotic import po
import base_file
from base_file import B
import weapons
from weapons import bronze_Dagger



class replay1(x):
    def replay(self,x,y):
        print("before function")
        y.HP = int(160)
        
        ask = input('Another one enemy approachs. Attack or run?').upper()
        if ask == 'ATTACK':
            print('test1')
            x
            print('not working')
test1 = replay1(po.Attack)           
            
    
test1.replay("test",B)

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