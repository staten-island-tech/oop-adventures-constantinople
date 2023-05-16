import Orderly
from Orderly import *
import Chaotic
from Chaotic import *
import Neutral
from Neutral import *
class start:
    def beginning():
        print("You have now been transported into the world of an ancient lineage. ")
        everything = input("Would you like to become an orderly, neutral, or chaotic class? ").upper()
        if everything == "ORDERLY":
            class1 = input("What class would you like to progress in?: 'Sigil Knight' or 'Whisperer' ").upper()
            if class1 == "SIGIL KNIGHT": 
                print("You are a Sigil Knight, a humble warrior of Solan. Your class is capable of using a bronze, silver, or mythril sword. ")
                user_class = A
            elif class1 == "WHISPERER":
                print("You are a Whisperer, a wisdom possessing child of the mother. Your class is capable of using your fists, dagger, or rapier. ")
                user_class = C
            else:
                print("Iagnime not bineg albe to selpl...")
                start.beginning()
        elif everything == "CHAOTIC":
            class2 = input("What class would you like to progress in?: 'Oni' or 'Faceless' ").upper()
            if class2 == "ONI":
                print("You are an Oni, a humble servant of Big Hoss. Your class is capable of using your fists, to bash the skulls of your enemies. ")
                user_class = op
            elif class2 == "FACELESS":
                print("You are a Facelss, a catestrophic apprentice of the snowman. Your class is capable of using a bronze, silver, or mythril dagger.")
                user_class = po
            else:
                print("Iagnime not bineg albe to selpl...")
                start.beginning()
        elif everything == "NEUTRAL":
            class3 = input("What class would you like to progress in?: 'Chef' or 'Blacksmith' ").upper()
            if class3 == "CHEF":
                print("You are a Chef, a skilled cook of Sentinel. Your class is capable of using a bronze, silver, or mythril frying pan. ")
                user_class = g
            elif class3 == "BLACKSMITH":
                print("You are a Blacksmith, a skilled craftsman of Castle Sanctuary. Your class is capable of using a bronze, silver, or mythril hammer.")
                user_class = y
            else:
                print("Iagnime not bineg albe to selpl...")
                start.beginning()
        else:
            print("Iagnime not bineg albe to selpl...")
            start.beginning()
        Warning = print("You must buy these weapons later.")
        Warning
start.beginning()
import shop


