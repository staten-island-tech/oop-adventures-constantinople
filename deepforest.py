import random
import sys, time
def sprint(str):
    for c in str  + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./250)
inventory3 = []
class deep_loot():
    def loot():
        trinkets = [1,2,3,4,5,6,7,8,9,10]
        goblet = {'name': 'Goblet', 'price':15, 'chance':[1,2,3,4,5]}
        ring = {'name': 'Ring', 'price':20, 'chance':[6,7]}
        nothing = {'chance':[8,9,10]}
        would = input("Would you like to start looting? 'Yes' or 'No' ").upper()
        while would == "YES":
            x = random.choice(trinkets)
            if x in goblet['chance']:
                sprint("You got a goblet")
                inventory3.append("Goblet")
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would = "YES"
                else:
                    sprint(f"Here is your inventory : {inventory3}")
                    break
            elif x in ring['chance']:
                sprint("You got a ring")
                inventory3.append("Ring")
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would ="YES"
                else:
                    sprint(f"Here is your inventory : {inventory3}")
                    break
            elif x in nothing:
                sprint("You got nothing")
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would = "YES"
                else:
                    sprint(f"Here is your inventory : {inventory3}")
                    break
        else:
            sprint("You MUST LOOT to coninue...")
            deep_loot.loot()