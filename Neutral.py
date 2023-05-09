import random
import Classes 
from Classes import Base_class, B



class chef(Base_class):
    def __init__(self, HP, Weapon, XP):
        super().__init__(HP, Weapon, XP)
    def Attack(self):
        while B.HP > 0:
            if B.HP < 0:
                break  
            OL = input('Would you like to attack?').upper()
            if OL == 'YES':
                Number_of_hits = random.randint(0 , 4)
                Damage = int(20)
                Total_DMG = Number_of_hits*Damage
                Remaing_enemy_HP = B.HP - Total_DMG
                if Remaing_enemy_HP < 0 or Remaing_enemy_HP == 0:
                    print('You defeated this enemy')
                    Added_XP = B.XP + g.XP
                    g.XP = Added_XP
                    print('You now have,' , Added_XP , 'XP')
                    break
                B.HP = Remaing_enemy_HP
                print(Remaing_enemy_HP)
            if OL != 'YES':
                print('You dont attack')
                break
g = chef(100, 'pan' , 0)

class BlackSmith(Base_class):
    def __init__(self, HP, Weapon, XP):
        super().__init__(HP, Weapon, XP)
    def Attack(self):
        while B.HP > 0:
            if B.HP < 0:
                break  
            OL = input('Would you like to attack?').upper()
            if OL == 'YES':
                Number_of_hits = random.randint(0 , 3)
                Damage = int(25)
                Total_DMG = Number_of_hits*Damage
                Remaing_enemy_HP = B.HP - Total_DMG
                if Remaing_enemy_HP < 0 or Remaing_enemy_HP == 0:
                    print('You defeated this enemy')
                    Added_XP = B.XP + y.XP
                    y.XP = Added_XP
                    print('You now have,' , Added_XP , 'XP')
                    break
                B.HP = Remaing_enemy_HP
                print(Remaing_enemy_HP)
            if OL != 'YES':
                print('You dont attack')
                break    
y = BlackSmith(110 , 'hammer' , 0)

