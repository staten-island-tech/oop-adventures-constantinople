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

class Merchant():
    def __init__(self, crown, ring, goblet, amulet, spell_book, emerald, pearl):
        self.crown = crown
        self.ring = ring
        self.goblet = goblet
        self.amulet = amulet
        self.spell_book = spell_book
        self.emerald = emerald 
        self.pearl = pearl
    def sell():
        merchant = Merchant(50, 20, 15, 25, 40, 75, 35)
        print("Hello traveler, I am the traveling merchant and would like to buy your trinkets off of you. ")
        sell = input("Would you like to sell your items? 'Yes' or 'No'. If you select 'No' you will be transported back to your looting area. ")
        if sell == "Yes":
            for crown in inventory:
                inventory.append(merchant.crown)
                inventory.remove("crown")
                print(inventory)

Merchant.sell()

