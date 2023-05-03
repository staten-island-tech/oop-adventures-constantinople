class question():
    one = input("You arrive on the map and must loot to find money. Where would you like to loot? Choose from 'Emerald Cove' 'Sentinel Castle' or 'Deepforest' ")
question.one
class trinket():
    def new():
        if question.one == "Emerald Cove":
            import emerald_cove
            from emerald_cove import cove_loot
            cove_loot.loot()
        elif question.one == "Sentinel Castle":
            import sentinel_castle
            from sentinel_castle import castle_loot
            castle_loot.loot()
        elif question.one == "Deepforest":
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
        if question.one == "Emerald Cove":
            import emerald_cove
            from emerald_cove import inventory1
            inventory = inventory1
        elif question.one == "Sentinel Castle":
            import sentinel_castle
            from sentinel_castle import inventory2
            inventory = inventory2
        elif question.one == "Deepforest":
            import deepforest
            from deepforest import inventory3
            inventory = inventory3
        print("Hello traveler, I am the traveling merchant and would like to buy your trinkets off of you. ")
        merchant = Merchant(50, 20, 15, 25, 40, 75, 35)
        sell = input("Would you like to sell your items? 'Yes' or 'No'. If you select 'No' you will be transported back to your looting area. ")
        if sell == "Yes":
            if 'Crown' in inventory:
                crown1 = 'Crown'
                for crown1 in inventory:
                    inventory.append(merchant.crown)
                    inventory.remove(crown1)
                    print(inventory)
            elif 'Ring' in inventory:
                ring1 = 'Ring'
                for ring1 in inventory:
                    inventory.append(merchant.ring)
                    inventory.remove(ring1)
            elif 'Goblet' in inventory:
                goblet1 = 'Goblet'
                for goblet1 in inventory:
                    inventory.append(merchant.goblet)
                    inventory.remove(goblet1)
            elif 'Emerald' in inventory:
                emerald1 = 'Emerald'
                for emerald1 in inventory:
                    inventory.append(merchant.emerald)
                    inventory.remove(emerald1)
            elif 'Pearl' in inventory:
                pearl1 = 'Pearl'
                for pearl1 in inventory:
                    inventory.append(merchant.pearl)
                    inventory.remove(pearl1)
            elif 'Spellbook' in inventory:
                spellbook1 = 'Spellbook'
                for spell_book1 in inventory:
                    inventory.append(merchant.spell_book)
                    inventory.remove(spellbook1)
            elif 'Amulet' in inventory:
                amulet1 = 'Amulet'
                for amulet1 in inventory:
                    inventory.append(merchant.amulet)
                    inventory.remove(amulet1)
        else:
            print("BUT WHYYYYYYY")
Merchant.sell()

