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
                print(A)
            elif class1 == "WHISPERER":
                user_class = C
            else:
                print("Iagnime not bineg albe to selpl...")
                start.beginning()
        elif everything == "CHAOTIC":
            class2 = input("What class would you like to progress in?: 'Oni' or 'Faceless' ").upper()
            if class2 == "ONI":
                user_class = op
            elif class2 == "FACELESS":
                user_class = po
            else:
                print("Iagnime not bineg albe to selpl...")
                start.beginning()
        elif everything == "NEUTRAL":
            class3 = input("What class would you like to progress in?: 'Chef' or 'Blacksmith' ").upper()
            if class3 == "CHEF":
                user_class = g
            elif class3 == "BLACKSMITH":
                user_class = y
            else:
                print("Iagnime not bineg albe to selpl...")
                start.beginning()
        else:
            print("Iagnime not bineg albe to selpl...")
            start.beginning()
start.beginning()


