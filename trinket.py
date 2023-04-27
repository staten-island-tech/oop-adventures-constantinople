def trinket():
    print("You arrive on the map and must find money to progress. ")
    question = input("Where would you like to loot? Choose from 'Emerald Cove' 'Sentinel Castle' or 'Deepforest' ")
    if question == "Emerald Cove":
        import emerald_cove
    elif question == "Sentinel Castle":
        import sentinel_castle
    elif question == "Deepforest":
        import deepforest
trinket()
