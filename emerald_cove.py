import random
inventory1 = []
class cove_loot():
    def loot():
        trinkets = [1,2,2.5,3,4,5,6,7,7.5,8,9,10]
        pearl = {'name': 'Pearl', 'price': 25, 'chance':[1,2,2.5]}
        spell_book = {'name': 'Spellbook', 'price': 40, 'chance':[3,4,5,6]}
        emerald = {'name': 'Emerald', 'price': 75, 'chance':[7,7.5]}
        nothing = {'chance':[8,9,10]}
        would = input("Would you like to start looting? 'Yes' or 'No' ")
        while would == "Yes":
            x = random.choice(trinkets)
            if x in pearl['chance']:
                print("You got a pearl")
                inventory1.append('Pearl')
                would2 = input("Would you like to continue looting? ")
                if would2 == "Yes":
                    would = "Yes"
                else:
                    print(f"Here is your inventory : {inventory1}")
                    break
            elif x in spell_book['chance']:
                print("You got a spellbook")
                inventory1.append('Spellbook')
                would2 = input("Would you like to continue looting? ")
                if would2 == "Yes":
                    would ="Yes"
                else:
                    print(f"Here is your inventory : {inventory1}")
                    break
            elif x in emerald['chance']:
                print("You got an emerald")
                inventory1.append('Emerald')
                would2 = input("Would you like to continue looting? ")
                if would2 == "Yes":
                    would = "Yes"
                else:
                    print(f"Here is your inventory : {inventory1}")
                    break
            elif x in nothing['chance']:
                print("You got nothing")
                would2 = input("Would you like to continue looting? ")
                if would2 == "Yes":
                    would = "Yes"
                else:
                    print(f"Here is your inventory : {inventory1}")
                    break
        else:
            return


