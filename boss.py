import random
import Classes 
from Classes import Base_class , B


""" 105 hp  """

class boss(Base_class):
    def __init__(self, HP, Weapon, XP):
        super().__init__(HP, Weapon, XP)
    def regualr_attack(self, x):
       damage = int(10)
       Hits = random.randint(1, 3)
       Player_Hit = damage*Hits
       if Player_Hit ==  int(0):
            print('You have escaped the Mages attack!')
            return
       Player_HP = x.HP - Player_Hit
       print('The Arcane Mage has hit you. You are now at ' , Player_HP , 'HP')
    def Special_Move(self , x):
        damage = int(8)
        multiplier = random.randint(0,5)
        Attack = damage*multiplier
        if Attack ==  int(0):
            print('You have escaped the Mages attack!')
            return
        Player_HP = x.HP - Attack
        print('You have been hit by the Arcane Mages morri turret.')
        print('You now have' , Player_HP , 'HP' )





