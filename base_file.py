import random



class Base_class:
    def __init__(self, HP , Weapon , XP):
        self.HP = int(HP)
        self.Weapon = Weapon
        self.XP = int(XP)
    def info(self):
        print(self.HP , self.Weapon , self.XP)
    def level_print(self):
        tag = ''
        if self.XP  >= 0 and self.XP <= 100:
            tag = 'Tier_1'
            print(tag)
        elif self.XP  >= 101 and self.XP <= 200:
            tag = 'Tier_2'
            print(tag)
        elif self.XP >= 201 and self.XP <= 300:
            tag = 'Tier_3'
            print(tag)
        elif self.XP >= 301 and self.XP <= 500:
            tag = 'Tier_4'
            print(tag)
        elif self.XP >= 501 and self.XP <= 100000:
            tag = 'Tier_5'
            print(tag)    


class Bossattack():
    def Boss_Attack1(t,y):
        multiplier = random.randint(0,4)
        total = t*multiplier
        Boss_HP = y.HP - total
        if total > 0:
            print('You have hit the arcane for' , total , 'damage')
            print('------------------------------')
            print('Hes now at' , Boss_HP , 'HP')
        elif total == int(0):
            print('You have failed to hit the Arcane')
            return
    



class Enemy1:
    def __init__(self, HP , XP):
        self.HP = HP
        self.XP = XP

B = Enemy1(160 ,30)

B.HP
