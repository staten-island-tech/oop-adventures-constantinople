import random

class Base_class:
    def __init__(self, HP , Weapon , XP):
        self.HP = int(HP)
        self.Weapon = Weapon
        self.XP = int(XP)
    def info(self):
        print(self.HP , self.Weapon , self.XP)

class Enemy1:
    def __init__(self, HP , XP):
        self.HP = HP
        self.XP = XP

