import random
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
                print("You got a goblet")
                inventory2.append('Goblet')
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would = "YES"
                else:
                    print(f"Here is your inventory : {inventory2}")
                    break
            elif x in crown['chance']:
                print("You got a crown")
                inventory2.append('Crown')
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would ="YES"
                else:
                    print(f"Here is your inventory : {inventory2}")
                    break
            elif x in amulet['chance']:
                print("You got an amulet")
                inventory2.append('Amulet')
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would ="YES"
                else:
                    print(f"Here is your inventory : {inventory2}")
                    break
            elif x in nothing['chance']:
                print("You got nothing")
                would2 = input("Would you like to continue looting? ").upper()
                if would2 == "YES":
                    would = "YES"
                else:
                    print(f"Here is your inventory : {inventory2}")
                    break
        else:
            return
