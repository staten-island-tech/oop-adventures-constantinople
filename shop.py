silver = int(0)
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
        sell = input("Would you like to sell your items? 'Yes' or 'No'. If you select 'No' you will be transported back to your looting area. ").upper()
        money = 0
        if sell == "YES":
                while ring['name'] in inventory:
                    money = money + ring['price']
                    inventory.remove(ring['name'])
                    sell == "Yes"
                while goblet['name'] in inventory:
                    money = money + goblet['price']
                    inventory.remove(goblet['name'])
                    sell == "Yes"
                while emerald['name'] in inventory:
                    money = money + emerald['price']
                    inventory.remove(emerald['name'])
                    sell == "Yes"
                while pearl['name'] in inventory:
                    money = money + pearl['price']
                    inventory.remove(pearl['name'])
                    sell == "Yes"
                while spell_book['name'] in inventory:
                    money = money + spell_book['price']
                    inventory.remove(spell_book['name'])
                    sell == "Yes"
                while crown['name'] in inventory:
                    money = money + crown['price']
                    inventory.remove(crown['name'])
                    sell == "Yes"
                while amulet['name'] in inventory:
                    money = money + amulet['price']
                    inventory.remove(amulet['name'])
                    sell == "Yes"
                while goblet['name'] in inventory:
                    money = money + goblet['price']
                    inventory.remove(goblet['name'])
                    sell == "Yes"
                global silvers
                global silver
                silvers = []
                silvers.append(money)
                for ele in range(0, len(silvers)):
                    silver = silver + silvers[ele]
                print(f"You have {silver} silver. You make your way back to the town you started at.")
                
        else:
            trinket.new()
            Merchant.sell()
Merchant.sell()





