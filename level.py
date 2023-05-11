f = 100

class level:
    def __init__(self) -> None:
        pass
    def level_print(f):
        if f  >= 0 and f <= 100:
            tag = 'Tier_1'
            print(tag)
        elif f  >= 101 and f <= 200:
            tag = 'Tier_2'
            print(tag)
        elif f >= 201 and f <= 300:
            tag = 'Tier_3'
            print(tag)
        elif f >= 301 and f <= 500:
            tag = 'Tier_4'
            print(tag)
        elif f >= 501 and f <= 100000:
            tag = 'Tier_5'
            print(tag)

""" put this code into the base class in classes file as another function so everyone can acces it no matter what """

TEST = level()
TEST.level_print(f)




