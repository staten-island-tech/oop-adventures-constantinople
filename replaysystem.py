import Chaotic
from Chaotic import po
import base_file
from base_file import B
import weapons
from weapons import mythril_sword


class replay1():
    def replay(x,y,z):
        y.HP = int(160)
        x.Attack(y,z)
        ask = input('Another one enemy approachs. Attack or run?').upper()
        while ask == 'ATTACK':
            y.HP = int(160)
            x.Attack(y,z)
            ask = input('Another one enemy approachs. Attack or run?').upper()
""" 
replay1.replay(po,B, mythril_sword) """


""" 
class leveling():
    def something():
        while  """