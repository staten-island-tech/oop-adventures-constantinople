import random
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
                print("You got a goblet")
                inventory3.append("Goblet")
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would = "YES"
                else:
                    print(f"Here is your inventory : {inventory3}")
                    break
            elif x in ring['chance']:
                print("You got a ring")
                inventory3.append("Ring")
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would ="YES"
                else:
                    print(f"Here is your inventory : {inventory3}")
                    break
            elif x in nothing:
                print("You got nothing")
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would = "YES"
                else:
                    print(f"Here is your inventory : {inventory3}")
                    break
        else:
            print("You MUST LOOT to coninue...")
            deep_loot.loot()