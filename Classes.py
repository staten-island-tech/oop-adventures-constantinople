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
B = Enemy1(160 ,30)


class replay1():
    def replay(x):
        x.Attack()
        lol = input('Would you like to go again ').upper()
        while lol == 'YES':
            B.HP = 160
            x.Attack()
            lol = input('Would you like to go again ').upper()
            if lol != 'YES':
                print('You dont attack')
                break