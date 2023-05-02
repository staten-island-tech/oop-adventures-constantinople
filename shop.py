
class trinket():
    def new():
        print("You arrive on the map and must find money to progress. ")
        question = input("Where would you like to loot? Choose from 'Emerald Cove' 'Sentinel Castle' or 'Deepforest' ")
        if question == "Emerald Cove":
            import emerald_cove
            from emerald_cove import cove_loot
            cove_loot.loot()
        elif question == "Sentinel Castle":
            import sentinel_castle
            from sentinel_castle import castle_loot
            castle_loot.loot()
        elif question == "Deepforest":
            import deepforest
            from deepforest import deep_loot
            deep_loot.loot()
trinket.new()

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
        print("Hello traveler, I am the traveling merchant and would like to buy your trinkets off of you. ")
        ask = input("Where did you obtain this loot from? 'Emerald Cove' 'Sentinel Castle' or 'Deepforest' ")
        if ask == "Emerald Cove":
            import emerald_cove
            from emerald_cove import inventory1
            inventory = inventory1
        elif ask == "Sentinel Castle":
            import sentinel_castle
            from sentinel_castle import inventory2
            inventory = inventory2
        elif ask == "Deepforest":
            import deepforest
            from deepforest import inventory3
            inventory = inventory3
        merchant = Merchant(50, 20, 15, 25, 40, 75, 35)
        sell = input("Would you like to sell your items? 'Yes' or 'No'. If you select 'No' you will be transported back to your looting area. ")
        if sell == "Yes":
            for crown in inventory:
                inventory.append(merchant.crown)
                inventory.remove("Crown")
                print(inventory)
            for ring in inventory:
                inventory.append(merchant.ring)
                inventory.remove("Ring")
                print(inventory)
            for goblet in inventory:
                inventory.append(merchant.goblet)
                inventory.remove("Goblet")
                print(inventory)
            for emerald in inventory:
                inventory.append(merchant.emerald)
                inventory.remove("Emerald")
                print(inventory)
            for pearl in inventory:
                inventory.append(merchant.pearl)
                inventory.remove("Pearl")
                print(inventory)
            for spell_book in inventory:
                inventory.append(merchant.spell_book)
                inventory.remove("Spellbook")
                print(inventory)
            for amulet in inventory:
                inventory.append(merchant.amulet)
                inventory.remove("Amulet")
                print(inventory)
Merchant.sell()

