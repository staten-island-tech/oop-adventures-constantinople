<<<<<<< HEAD
import random
import base_file
from base_file import Base_class, B



=======
class Base_class:
    def __init__(self, HP , Weapon , Money , XP):
        self.HP = HP
        self.Weapon = Weapon
        self.Money = int(Money)
        self.XP = int(XP)
>>>>>>> 5fe998b6f23fc1467866454b3576706a3f458a96

class Oni(Base_class):
    def __init__(self, HP, Weapon, Money, kills,):
        super().__init__(HP, Weapon, Money)
        self.kills = int(kills)
    

class Faceless(Base_class):
<<<<<<< HEAD
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



class oni(Base_class):
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


op = oni(115 , 'something' , 0)
=======
    def __init__(self, HP, Weapon, Money, kills):
        super().__init__(HP, Weapon, Money)
        self.kills = int(kills)
Mathew = Oni(100,"Sword",1000,1)
>>>>>>> 5fe998b6f23fc1467866454b3576706a3f458a96
