level = int(40)
current_level = ''

class level:
    def __init__(self) -> None:
        pass
    def level_print(self):
        global current_level 
        if level == range(0,51):
            current_level ='Tier 1'       
        elif level == range(51,101):
            current_level = 'Tier_2'
        elif level == range(101,251):
            current_level = 'Tier_3'
        elif level == range(251,351):
            current_level = 'Tier_4'
        elif level == range(351,1000000):
            current_level = 'Tier_5'
        print(current_level)
 
TEST = level()
TEST.level_print()
