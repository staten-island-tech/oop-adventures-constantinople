class level:
    def __init__(self) -> None:
        pass
    def level_print(self):
        level = user.xp
        if level >=0 or level <=50:
            current_level = 'Tier_1'
        if level >=51 or level <=100:
            current_level = 'Tier_2'
        if level >=101 or level <=200:
            current_level = 'Tier_3'
        if level >=201 or level <=400:
            current_level = 'Tier_4'
        if level >=401 or level <=1000000:
            current_level = 'Tier_5'
        print(current_level)
        