import Orderly
from Orderly import *
import Chaotic
from Chaotic import *
import Neutral
from Neutral import *
user_class = []
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
                print("Iagnime not bineg albe to selpl...")
                start.beginning()
        else:
            print("Iagnime not bineg albe to selpl...")
            start.beginning()
start.beginning()
import shop
from shop import *
class we():
    def choices():
        if A in user_class:
            print("Hmmmm... Very interesting.... Your class is capable of purchasing a bronze, silver, or mythril sword. ")
            which = input("Which one would you like? 'bronze' 'silver' or 'mythril' ").upper()
            if which == "BRONZE":
                from shop import silver
                new = silver - 15
                print(new)
        elif C in user_class:
            print("Hmmmm... Very interesting.... Your class is capable of purchasing a bronze dagger, silver dagger or mythril dagger. ")
            which = input("Which one would you like? 'bronze' 'silver' or 'mythril' ").upper()
        elif op in user_class:
            print("Ah HA, I have nothing in store for you, except for A CESTUS. ")
            which = input("Would you like to purchase it? ").upper()
        elif po in user_class:
            print("AHHH!! Your face, ITS GONE! BUY YOUR WEAPON AND GET OUTTT! -- He presents three daggers to you -- ")
            which = input("Which dagger would you like to buy? 'bronze' 'silver' or 'mythril'? ").upper()
        elif g in user_class:
            print("Ahh, a lovely chef. After you finish you should make me some food sometime. ")
            which = input("What would you like to buy? 'bronze_pan' 'silver_pan' or 'mythril_pan'? ").upper()
        elif y in user_class:
            print("A blacksmith? Just like me! Here, take this hammer free of charge!! ")

class weaponsmith():
    def weapon():
        colorado = input("Would you like to go to the shop?" ).upper()
        if colorado == "YES":
            lol = input("Hello traveler, I am the weaponsmith of this town and have some lovely options for you. Would you like to see?").upper()
            if lol == "YES":
                we.choices()
            else:
                weaponsmith.weapon()
        else:
            print("YOU MUST GO TO THE SHOP TO CONINTUEEEEEE")
            weaponsmith.weapon()

weaponsmith.weapon()

