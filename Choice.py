import Orderly
from Orderly import *
import Chaotic
from Chaotic import *
import Neutral
from Neutral import *
user_class = []
user_weapon = []
class not_enough_money:
    def bruh():
        print("You must go loot to get more silver to afford this item. ")
        trinket.new()
class start:
    def beginning():
        print("You have now been transported into the world of an ancient lineage. ")
        everything = input("Would you like to become an orderly, neutral, or chaotic class? ").upper()
        if everything == "ORDERLY":
            class1 = input("What class would you like to progress in?: 'Sigil Knight' or 'Whisperer' ").upper()
            if class1 == "SIGIL KNIGHT": 
                print("You are a Sigil Knight, a humble warrior of Solan. ")
                user_class.append(A)
            elif class1 == "WHISPERER":
                print("You are a Whisperer, a wisdom possessing child of the mother. ")
                user_class.append(C)
            else:
                print("Iagnime not bineg albe to selpl...")
                start.beginning()
        elif everything == "CHAOTIC":
            class2 = input("What class would you like to progress in?: 'Oni' or 'Faceless' ").upper()
            if class2 == "ONI":
                print("You are an Oni, a humble servant of Big Hoss. ")
                user_class.append(op)
            elif class2 == "FACELESS":
                print("You are a Facelss, a catestrophic apprentice of the snowman. ")
                user_class.append(po)
            else:
                print("Iagnime not bineg albe to selpl...")
                start.beginning()
        elif everything == "NEUTRAL":
            class3 = input("What class would you like to progress in?: 'Chef' or 'Blacksmith' ").upper()
            if class3 == "CHEF":
                print("You are a Chef, a skilled cook of Sentinel. ")
                user_class.append(g)
            elif class3 == "BLACKSMITH":
                print("You are a Blacksmith, a skilled craftsman of Castle Sanctuary. ")
                user_class.append(y)
            else:
                print("Iagnime not bineg albe to selpl..." )
                start.beginning()
        else:
            print("Iagnime not bineg albe to selpl..." )
            start.beginning()
start.beginning()
import shop
from shop import *
from shop import silver
class we():
    def choices():
        if A in user_class:
            print("Hmmmm... Very interesting.... Your class is capable of purchasing a bronze, silver, or mythril sword. ")
            which = input("Which one would you like? 'bronze -> 180' 'silver -> 300' or 'mythril -> 450' ").upper()
            if which == "BRONZE":
                user_class.append("bronze_sword")
                new = silver - 180
                if new < 0:
                    not_enough_money.bruh()
                else:
                    print(f"You have {new} silver left." )
            elif which == "SILVER":
                user_class.append("silver_sword")
                new = silver - 300
                if new < 0:
                    not_enough_money.bruh()
                else:
                    print(f"You have {new} silver left." )
            elif which == "MYTHRIL":
                user_class.append("mythril_sword")
                new = silver - 450
                if new < 0:
                    not_enough_money.bruh()
                else:
                    print(f"You have {new} silver left." )
            else:
                print("Iagnime not bineg albe to selpl..." )
                we.choices()
        elif C in user_class:
            print("Hmmmm... Very interesting.... Your class is capable of purchasing a bronze dagger, silver dagger or mythril dagger. ")
            which = input("Which one would you like? 'bronze' -> 100 'silver' -> 200  or 'rapier' -> 575 ").upper()
            if which == "BRONZE":
                user_class.append("bronze_dagger")
                new = silver - 100
                if new < 0:
                    not_enough_money.bruh()
                else:
                    print(f"You have {new} silver left." )
            elif which == "SILVER":
                user_class.append("silver_dagger")
                new = silver - 200
                if new < 0:
                    not_enough_money.bruh()
                else:
                    print(f"You have {new} silver left." )
            elif which == "RAPIER":
                user_class.append("rapier")
                new = silver - 575
                if new < 0:
                    not_enough_money.bruh()
                else:
                    print(f"You have {new} silver left." )
            else:
                print("Iagnime not bineg albe to selpl..." )
                we.choices()
        elif op in user_class:
            print("Ah HA, I have nothing in store for you, except for A CESTUS. ")
            which = input("What would you like to buy? 'cestus' -> 600 ").upper()
            if which == "CESTUS":
                user_class.append("cestus")
                new = silver - 600
                if new < 0:
                    not_enough_money.bruh()
                else:
                    print(f"You have {new} silver left." )
            else:
                print("Iagnime not bineg albe to selpl..." )
                we.choices()
        elif po in user_class:
            print("AHHH!! Your face, ITS GONE! BUY YOUR WEAPON AND GET OUTTT! -- He presents three daggers to you -- ")
            which = input("Which dagger would you like to buy? 'bronze' -> 100 'silver' -> 200  or 'mythril' -> 300 ").upper()
            if which == "BRONZE":
                user_class.append("bronze_dagger")
                new = silver - 100
                if new < 0:
                    not_enough_money.bruh()
                else:
                    print(f"You have {new} silver left." )
            elif which == "SILVER":
                user_class.append("silver_dagger")
                new = silver - 200
                if new < 0:
                    not_enough_money.bruh()
                else:
                    print(f"You have {new} silver left." )
            elif which == "MYTHRIL":
                user_class.append("mythril_dagger")
                new = silver - 300
                if new < 0:
                    not_enough_money.bruh()
                else:
                    print(f"You have {new} silver left." )
            else:
                print("Iagnime not bineg albe to selpl..." )
                we.choices()
        elif g in user_class:
            print("Ahh, a lovely chef. After you finish you should make me some food sometime. ")
            which = input("What would you like to buy? 'bronze_pan' -> 75 'silver_pan' -> 175 or 'mythril_pan'? -> 275 ").upper()
            if which == "BRONZE_PAN":
                user_class.append("bronze_pan")
                new = silver - 75
                if new < 0:
                    not_enough_money.bruh()
                else:
                    print(f"You have {new} silver left." )
            elif which == "SILVER_PAN":
                user_class.append("silver_pan")
                new = silver - 175
                if new < 0:
                    not_enough_money.bruh()
                else:
                    print(f"You have {new} silver left." )
            elif which == "MYTHRIL_PAN":
                user_class.append("mythril_pan")
                new = silver - 275
                if new < 0:
                    not_enough_money.bruh()
                else:
                    print(f"You have {new} silver left." )
            else:
                print("Iagnime not bineg albe to selpl..." )
                we.choices()
        elif y in user_class:
            print("A blacksmith? Just like me! Here, take this hammer free of charge!! ")
            user_weapon.append("hammer")
            new = silver - 0 
            print(f"You still have {new} silver. LOL ")

class weaponsmith():
    def weapon():
        colorado = input("Would you like to go to the shop? " ).upper()
        if colorado == "YES":
            lol = input("Hello traveler, I am the weaponsmith of this town and have some lovely options for you. Would you like to see? ").upper()
            if lol == "YES":
                we.choices()
            else:
                weaponsmith.weapon()
        else:
            print("YOU MUST GO TO THE SHOP TO CONINTUEEEEEE ")
            weaponsmith.weapon()

weaponsmith.weapon()
