

import random
import Classes 
from Classes import *
import Chaotic
from Chaotic import *
import boss 
from boss import *
import Neutral
from Neutral import *
import Orderly
from Orderly import *


""" Arcane = boss(450 , ' Mace', 100 )
Arcane.Special_Move(po)
 """
""" if you want to acces anything import it in and acces it all or whatever you need such as example above """


po.info()
print('Your Current level is:')
po.level_print()
replay1.replay(po)
print('Your Current level is:')
po.level_print()

""" make it so that you need tier 5 to fight the boss otherwise you cant """

if po.level_print == 'Tier_5':
    print('Checpoint_True')
elif po.level_print != 'Tier_5':
    print('Your not high level')
