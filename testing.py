import Chaotic
from Chaotic import po
import base_file
from base_file import B
import weapons
from weapons import bronze_Dagger

test = po.Attack(B, bronze_Dagger)

class replay1():
    def replay(x,y):
        l = input('Would you like to fight ').upper()
        if l == 'YES':
            x
            ask = input("Attack another enemy?").upper()
            while ask == 'YES':
                y.HP = 160
                x
                ask
            if ask != 'YES':
                print('wduowhudhwauhdwauhdwa')
                
    
replay1.replay(test,B)