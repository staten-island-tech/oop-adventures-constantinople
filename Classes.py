import random


class Base_class:
    def __init__(self, HP , Weapon , XP):
        self.HP = int(HP)
        self.Weapon = Weapon
        self.XP = int(XP)
    def info(self):
        print(self.HP , self.Weapon , self.XP)
    def Boss_Attack1(self , x):
        damage = int(30)
        multiplier = random.randint(0,4)
        total = damage*multiplier
        Boss_HP = x.HP - total
        if total > 0:
            print('You have hit the arcane for' , total , 'HP')
        elif total == int(0):
            print('You have failed to hit the Arcane')
            return
        

class Enemy1:
    def __init__(self, HP , XP):
        self.HP = HP
        self.XP = XP

B = Enemy1(160 ,30)

class replay1():
    def replay(x):
       l = input('Would you like to fight ').upper()
       if l == 'YES':
            x.Attack()
            lol = input('Would you like to attack again? ').upper()
            while lol == 'YES':
                B.HP = 160
                x.Attack()
                lol = input('Would you like to go again ').upper()
                if lol != 'YES':
                    print('You dont attack')
                    break

