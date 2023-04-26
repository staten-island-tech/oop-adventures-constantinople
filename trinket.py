def trinket():
    print("You arrive on the map and must find money to progress. ")
    question = input("Where would you like to loot? Choose from 'Emerald Cove' 'Sentinel Castle' or 'Deepforest' ")
    if question == "Emerald Cove":
        from emerald_cove import loot()
        loot()
trinket()
