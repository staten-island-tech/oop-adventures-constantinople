import random
import base_file
from base_file import Base_class , B




class GRAH(Base_class):
    def __init__(self, HP, Weapon, XP):
        super().__init__(HP, Weapon, XP)
    def regualr_attack(x):
       damage = int(10)
       Hits = random.randint(1, 3)
       Player_Hit = damage*Hits
       if Player_Hit ==  int(0):
            print('You have escaped the Mages attack!')
            return
       Player_HP = x.HP - Player_Hit
       print('The Arcane Mage has hit you. You are now at ' , Player_HP , 'HP')
    def Special_Move(x):
        damage = int(8)
        multiplier = random.randint(0,6)
        Attack = damage*multiplier
        if Attack ==  int(0):
            print('You have escaped the Mages morri turret')
            return
        Player_HP = x.HP - Attack
        print('You have been hit by the Arcane Mages morri turret.')
        print('You now have' , Player_HP , 'HP' )
    def fimbul(x):
        damage = int(110)
        attack = damage
        Player_HP = x.HP - attack
        if Player_HP == 0 or Player_HP < 0:
            print('You hear the sound, kbobawidfhjvab, and a giant portal looms above you.')
            print('A giant ice chain dives onto you.')
            print('---------------------------------------------------------')
            print('You are now dead sucker')
            exit()
        elif Player_HP != 0:
            print('You now have' , Player_HP , 'HP')

GRAH(300, 'Tome' , 185)





