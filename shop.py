class question():
    one = input("You arrive on the map and must loot to find money. Where would you like to loot? Choose from 'Emerald Cove' 'Sentinel Castle' or 'Deepforest' ").upper()
question.one
class trinket():
    def new():
        if question.one == "EMERALD COVE":
            import emerald_cove
            from emerald_cove import cove_loot
            cove_loot.loot()
        elif question.one == "SENTINEL CASTLE":
            import sentinel_castle
            from sentinel_castle import castle_loot
            castle_loot.loot()
        elif question.one == "DEEPFOREST":
            import deepforest
            from deepforest import deep_loot
            deep_loot.loot()
trinket.new()

class Merchant():
    def sell():
        if question.one == "EMERALD COVE":
            import emerald_cove
            from emerald_cove import inventory1
            inventory = inventory1
        elif question.one == "SENTINEL CASTLE":
            import sentinel_castle
            from sentinel_castle import inventory2
            inventory = inventory2
        elif question.one == "DEEPFOREST":
            import deepforest
            from deepforest import inventory3
            inventory = inventory3
        print("Hello traveler, I am the traveling merchant and would like to buy your trinkets off of you. ")
        goblet = {'name': 'Goblet', 'price':15, 'chance':[1,2,3,4,5]}
        ring = {'name': 'Ring', 'price': 20, 'chance':[6,7]}
        crown = {'name': 'Crown', 'price': 50, 'chance':[2]}
        amulet = {'name': 'Amulet', 'price':25, 'chance':[4]}
        pearl = {'name': 'Pearl', 'price': 25, 'chance':[1,2,2.5]}
        spell_book = {'name': 'Spellbook', 'price': 40, 'chance':[3,4,5,6]}
        emerald = {'name': 'Emerald', 'price': 75, 'chance':[7,7.5]}
        sell = input("Would you like to sell your items? 'Yes' or 'No'. If you select 'No' you will be transported back to your looting area. ")
        if sell == "Yes":
            for crown['name'] in inventory:
                inventory.append(crown['price'])
                inventory.remove(crown['name'])
            for ring['name'] in inventory:
                inventory.append(ring['price'])
                inventory.remove(ring['name'])
            for goblet['name'] in inventory:
                inventory.append(goblet['price'])
                inventory.remove(goblet['name'])
            for emerald['name'] in inventory:
                inventory.append(emerald['price'])
                inventory.remove(emerald['name'])
            for pearl['name'] in inventory:
                inventory.append(pearl['price'])
                inventory.remove(pearl['name'])
            for spell_book['name'] in inventory:
                inventory.append(spell_book['price'])
                inventory.remove(spell_book['name'])
            for amulet['name'] in inventory:
                inventory.append(amulet['price'])
                inventory.remove(amulet['name'])
            print(inventory)
Merchant.sell()




