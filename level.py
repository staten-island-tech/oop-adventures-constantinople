
x = 324


class level:
    def __init__(self) -> None:
        pass
    def level_print(self):
        if x  >= 0 and x <= 100:
            tag = 'Tier_1'
            print(tag)
        elif x  >= 101 and x <= 200:
            tag = 'Tier_2'
            print(tag)
        elif x >= 201 and x <= 300:
            tag = 'Tier_3'
            print(tag)
        elif x >= 301 and x <= 500:
            tag = 'Tier_4'
            print(tag)
        elif x >= 501 and x <= 100000:
            tag = 'Tier_5'
            print(tag)




TEST = level()
TEST.level_print()



