import random
inventory = []
def loot():
    trinkets = [1,2,3,4]
    goblet = [1]
    crown = [2]
    nothing = [3]
    amulet = [4]
    would = input("Would you like to start looting? 'Yes' or 'No' ")
    while would == "Yes":
        x = random.choice(trinkets)
        if x in goblet:
            print("You got a goblet")
            inventory.append("Goblet")
            would2 = input("Would you like to continue looting? ")
            if would2 == "Yes":
                would = "Yes"
            else:
                print(f"Here is your inventory : {inventory}")
                break
        elif x in crown:
            print("You got a crown")
            inventory.append("Crown")
            would2 = input("Would you like to continue looting? ")
            if would2 == "Yes":
                would ="Yes"
            else:
                print(f"Here is your inventory : {inventory}")
                break
        elif x in amulet:
            print("You got an amulet")
            inventory.append("Amulet")
            would2 = input("Would you like to continue looting? ")
            if would2 == "Yes":
                would ="Yes"
            else:
                print(f"Here is your inventory : {inventory}")
                break
        elif x in nothing:
            print("You got nothing")
            would2 = input("Would you like to continue looting? ")
            if would2 == "Yes":
                would = "Yes"
            else:
                print(f"Here is your inventory : {inventory}")
                break
    else:
        return
loot()