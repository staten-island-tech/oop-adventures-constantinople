import random
import random
import sys, time
def sprint(str):
    for c in str  + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./250)
inventory1 = []
class cove_loot():
    def loot():
        trinkets = [1,2,2.5,3,4,5,6,7,7.5,8,9,10]
        pearl = {'name': 'Pearl', 'price': 25, 'chance':[1,2,2.5]}
        spell_book = {'name': 'Spellbook', 'price': 40, 'chance':[3,4,5,6]}
        emerald = {'name': 'Emerald', 'price': 75, 'chance':[7,7.5]}
        nothing = {'chance':[8,9,10]}
        would = input("Would you like to start looting? 'Yes' or 'No' ").upper()
        while would == "YES":
            x = random.choice(trinkets)
            if x in pearl['chance']:
                sprint("You got a pearl")
                inventory1.append('Pearl')
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would = "YES"
                else:
                    sprint(f"Here is your inventory : {inventory1}")
                    break
            elif x in spell_book['chance']:
                sprint("You got a spellbook")
                inventory1.append('Spellbook')
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would ="YES"
                else:
                    sprint(f"Here is your inventory : {inventory1}")
                    break
            elif x in emerald['chance']:
                sprint("You got an emerald")
                inventory1.append('Emerald')
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would = "YES"
                else:
                    sprint(f"Here is your inventory : {inventory1}")
                    break
            elif x in nothing['chance']:
                sprint("You got nothing")
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would = "YES"
                else:
                    sprint(f"Here is your inventory : {inventory1}")
                    break
        else:
            sprint("You MUST loot to coninue... ")
            cove_loot.loot()


