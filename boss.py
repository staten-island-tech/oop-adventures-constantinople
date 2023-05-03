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
       Player_HP = po.HP - Player_Hit
       print('The Arcane Mage has hit you. You are now at ' , Player_HP , 'HP')
    def Block(self):
        return



Arcane = boss(350 , 'Mace of the undead' , 150)
Arcane.regualr_attack()
