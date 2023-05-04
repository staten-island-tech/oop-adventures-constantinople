import Classes
import random
from Classes import Base_class, Enemy1 
import Chaotic
from Chaotic import po


""" 105 hp  """

class boss(Base_class):
    def __init__(self, HP, Weapon, XP):
        super().__init__(HP, Weapon, XP)
    def regualr_attack(self):
       damage = int(10)
       Hits = random.randint(1, 3)
       Player_Hit = damage*Hits
       if Player_Hit ==  int(0):
            print('You have escaped the Mages attack!')
            return
       Player_HP = po.HP - Player_Hit
       print('The Arcane Mage has hit you. You are now at ' , Player_HP , 'HP')
    def Special_Move(self):
        damage = int(40)
        multiplier = random.randint(0,4)
        Attack = damage*multiplier
        if Attack ==  int(0):
            print('You have escaped the Mages attack!')
            return
        Player_HP = po.HP - Attack
        print('You have been hit by the Arcane Mages morri turret.')
        print('You now have' , Player_HP , 'HP' )



Arcane = boss(350 , 'Mace of the undead' , 150)
po.Boss_Attack1

