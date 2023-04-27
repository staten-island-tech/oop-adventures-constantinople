import random
inventory = []
def loot():
    trinkets = [1,2,3,4,5,6,7,8,9,10]
    goblet = [1,2,3,4,5]
    ring = [6,7]
    nothing = [8,9,10]
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
        if x in ring:
            print("You got a ring")
            inventory.append("Ring")
            would2 = input("Would you like to continue looting? ")
            if would2 == "Yes":
                would ="Yes"
            else:
                print(f"Here is your inventory : {inventory}")
                break
        if x in nothing:
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