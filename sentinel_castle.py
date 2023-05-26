import random
import random
import sys, time
def sprint(str):
    for c in str  + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./250)
inventory2 = []
class castle_loot():
    def loot():
        trinkets = [1,2,3,4]
        goblet = {'name': 'Goblet', 'price': 15, 'chance':[1]}
        crown = {'name': 'Crown', 'price': 50, 'chance':[2]}
        nothing = {'chance':[3]}
        amulet = {'name': 'Amulet', 'price':25, 'chance':[4]}
        would = input("Would you like to start looting? 'Yes' or 'No' ").upper()
        while would == "YES":
            x = random.choice(trinkets)
            if x in goblet['chance']:
                sprint("You got a goblet")
                inventory2.append('Goblet')
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would = "YES"
                else:
                    sprint(f"Here is your inventory : {inventory2}")
                    break
            elif x in crown['chance']:
                sprint("You got a crown")
                inventory2.append('Crown')
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would ="YES"
                else:
                    sprint(f"Here is your inventory : {inventory2}")
                    break
            elif x in amulet['chance']:
                sprint("You got an amulet")
                inventory2.append('Amulet')
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would ="YES"
                else:
                    sprint(f"Here is your inventory : {inventory2}")
                    break
            elif x in nothing['chance']:
                sprint("You got nothing")
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would = "YES"
                else:
                    sprint(f"Here is your inventory : {inventory2}")
                    break
        else:
            sprint("You MUST loot to coninue... ")
            castle_loot.loot()

