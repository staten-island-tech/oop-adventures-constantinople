import sys, time
import Orderly
from Orderly import *
import Chaotic
from Chaotic import *
import Neutral
from Neutral import *
import replaysystem
from replaysystem import *


user_class = []
user_weapon = []

def sprint(str):
    for c in str  + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5./250)

class start:
    def beginning():
        sprint("You have now been transported into the world of an ancient lineage. ")
        everything = input("Would you like to become an orderly, neutral, or chaotic class? ").upper()
        if everything == "ORDERLY":
            class1 = input("What class would you like to progress in?: 'Sigil Knight' or 'Whisperer' ").upper()
            if class1 == "SIGIL KNIGHT": 
                sprint("You are a Sigil Knight, a humble warrior of Solan. ")
                user_class.append("sigil")
            elif class1 == "WHISPERER":
                sprint("You are a Whisperer, a wisdom possessing child of the mother. ")
                user_class.append("whisperer")
            else:
                sprint("Iagnime not bineg albe to selpl...")
                start.beginning()
        elif everything == "CHAOTIC":
            class2 = input("What class would you like to progress in?: 'Oni' or 'Faceless' ").upper()
            if class2 == "ONI":
                sprint("You are an Oni, a humble servant of Big Hoss. ")
                user_class.append("oni")
            elif class2 == "FACELESS":
                sprint("You are a Facelss, a catestrophic apprentice of the snowman. ")
                user_class.append("faceless")
            else:
                sprint("Iagnime not bineg albe to selpl...")
                start.beginning()
        elif everything == "NEUTRAL":
            class3 = input("What class would you like to progress in?: 'Chef' or 'Blacksmith' ").upper()
            if class3 == "CHEF":
                sprint("You are a Chef, a skilled cook of Sentinel. ")
                user_class.append("chef")
            elif class3 == "BLACKSMITH":
                sprint("You are a Blacksmith, a skilled craftsman of Castle Sanctuary. ")
                user_class.append("blacksmith")
            else:
                sprint("Iagnime not bineg albe to selpl..." )
                start.beginning()
        else:
            sprint("Iagnime not bineg albe to selpl..." )
            start.beginning()
start.beginning()
import shop
from shop import *

class not_enough_money:
    def bruh():
        sprint("You must go loot to get more silver to afford this item. ")
        trinket.new()
        Merchant.sell()
        weaponsmith.weapon()
class we():
    def choices():
        from shop import silver 
        if "sigil" in user_class:
            sprint("Hmmmm... Very interesting.... Your class is capable of purchasing a bronze, silver, or mythril sword. ")
            which = input("Which one would you like? 'bronze -> 180' 'silver -> 300' or 'mythril -> 450' ").upper()
            if which == "BRONZE":
                new = silver
                if new >= 180:
                    new = new - 180
                    user_weapon.clear()
                    user_weapon.append("bronze_sword")
                    sprint(f"You have {new} silver left." )
                    return
                else:
                    not_enough_money.bruh()
            elif which == "SILVER":
                new = silver - 300
                if new < 0:
                    not_enough_money.bruh()
                else:
                    user_weapon.clear()
                    user_weapon.append("silver_sword")
                    sprint(f"You have {new} silver left." )
            elif which == "MYTHRIL":
                new = silver - 450
                if new < 0:
                    not_enough_money.bruh()
                else:
                    user_weapon.clear()
                    user_weapon.append("mythril_sword")
                    sprint(f"You have {new} silver left." )
            else:
                sprint("Iagnime not bineg albe to selpl..." )
                we.choices()
        elif "Whisperer" in user_class:
            sprint("Hmmmm... Very interesting.... Your class is capable of purchasing a bronze dagger, silver dagger or rapier. ")
            which = input("Which one would you like? 'bronze' -> 100 'silver' -> 200  or 'rapier' -> 575 ").upper()
            if which == "BRONZE":
                new = silver - 100
                if new < 0:
                    not_enough_money.bruh()
                else:
                    user_weapon.clear()
                    user_weapon.append("bronze_dagger")
                    sprint(f"You have {new} silver left." )
            elif which == "SILVER":
                new = silver - 200
                if new < 0:
                    not_enough_money.bruh()
                else:
                    user_weapon.clear()
                    user_weapon.append("silver_dagger")
                    sprint(f"You have {new} silver left." )
            elif which == "RAPIER":
                new = silver - 575
                if new < 0:
                    not_enough_money.bruh()
                else:
                    user_weapon.clear()
                    user_weapon.append("rapier")
                    sprint(f"You have {new} silver left." )
            else:
                sprint("Iagnime not bineg albe to selpl..." )
                we.choices()
        elif "oni" in user_class:
            sprint("Ah HA, I have nothing in store for you, except for A CESTUS. ")
            which = input("What would you like to buy? 'cestus' -> 600 ").upper()
            if which == "CESTUS":
                new = silver - 600
                if new < 0:
                    not_enough_money.bruh()
                else:
                    user_weapon.clear()
                    user_weapon.append("cestus")
                    sprint(f"You have {new} silver left." )
            else:
                sprint("Iagnime not bineg albe to selpl..." )
                we.choices()
        elif "faceless" in user_class:
            sprint("AHHH!! Your face, ITS GONE! BUY YOUR WEAPON AND GET OUTTT! -- He presents three daggers to you -- ")
            which = input("Which dagger would you like to buy? 'bronze' -> 100 'silver' -> 200  or 'mythril' -> 300 ").upper()
            if which == "BRONZE":
                new = silver - 100
                if new < 0:
                    not_enough_money.bruh()
                else:
                    user_weapon.clear()
                    user_weapon.append("bronze_dagger")
                    sprint(f"You have {new} silver left." )
            elif which == "SILVER":
                new = silver - 200
                if new < 0:
                    not_enough_money.bruh()
                else:
                    user_weapon.clear()
                    user_weapon.append("silver_dagger")
                    sprint(f"You have {new} silver left." )
            elif which == "MYTHRIL":
                new = silver - 300
                if new < 0:
                    not_enough_money.bruh()
                else:
                    user_weapon.clear()
                    user_weapon.append("mythril_dagger")
                    sprint(f"You have {new} silver left." )
            else:
                sprint("Iagnime not bineg albe to selpl..." )
                we.choices()
        elif "chef" in user_class:
            sprint("Ahh, a lovely chef. After you finish you should make me some food sometime. ")
            which = input("What would you like to buy? 'bronze_pan' -> 75 'silver_pan' -> 175 or 'mythril_pan'? -> 275 ").upper()
            if which == "BRONZE_PAN":
                new = silver - 75
                if new < 0:
                    not_enough_money.bruh()
                else:
                    user_weapon.clear()
                    user_weapon.append("bronze_pan")
                    sprint(f"You have {new} silver left." )
            elif which == "SILVER_PAN":
                new = silver - 175
                if new < 0:
                    not_enough_money.bruh()
                else:
                    user_weapon.clear()
                    user_weapon.append("silver_pan")
                    sprint(f"You have {new} silver left." )
            elif which == "MYTHRIL_PAN":
                new = silver - 275
                if new < 0:
                    not_enough_money.bruh()
                else:
                    user_weapon.clear()
                    user_weapon.append("mythril_pan")
                    sprint(f"You have {new} silver left." )
            else:
                sprint("Iagnime not bineg albe to selpl..." )
                we.choices()
        elif "blacksmith" in user_class:
            sprint("A blacksmith? Just like me! Here, take this hammer free of charge!! ")
            user_weapon.clear()
            user_weapon.append("hammer")
            new = silver - 0 
            sprint(f"You still have {new} silver. LOL ")

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
            sprint("YOU MUST GO TO THE SHOP TO CONINTUEEEEEE ")
            weaponsmith.weapon()

weaponsmith.weapon()



class grinding():
    def rewind_time():
        please_no = input("Would you like to shop again? If you say yes and buy a new item, your old item will be sold and you will obtain the new one that you choose. If you say no you will re-locate to the z'scoom pit to progress. ").upper()
        if please_no == "YES":
            weaponsmith.weapon()
            grinding.level_farm()
        else:
            grinding.level_farm()
    def level_farm():
        sprint("You exit the village and are approached by a zombie scroom! ")
        if "sigil" in user_class:
            if "bronze_sword" in user_class:
                from weapons import bronze_sword
                replay1.replay(sigil_Knight, B , bronze_sword)
            elif "silver_sword" in user_class:
                from weapons import silver_sword
                replay1.replay(sigil_Knight, B , silver_sword)
            elif "mythril_sword" in user_class:
                from weapons import mythril_sword
                replay1.replay(sigil_Knight, B , mythril_sword)
        elif "whisperer" in user_class:
            if "bronze_dagger" in user_weapon:
                from weapons import bronze_Dagger
                replay1.replay(Whisperer, B , bronze_Dagger)
            elif "silver_dagger" in user_weapon:
                from weapons import silver_Dagger
                replay1.replay(Whisperer, B , silver_Dagger)
            elif "rapier" in user_weapon:
                from weapons import rapier
                replay1.replay(Whisperer, B , rapier)
        elif "faceless" in user_class:
            if "bronze_dagger" in user_weapon:
                from weapons import bronze_Dagger
                replay1.replay(Faceless, B , bronze_Dagger)
            elif "silver_dagger" in user_weapon:
                from weapons import silver_Dagger
                replay1.replay(Faceless, B , silver_Dagger)
            elif "mythril_dagger" in user_weapon:
                from weapons import mythril_Dagger
                replay1.replay(Faceless, B , mythril_Dagger)
        elif "oni" in user_class:
            if "cestus" in user_weapon:
                from weapons import fists
                replay1.replay(oni, B , fists)
            else:
                print("something broke")
        elif "chef" in user_class:
            if "bronze_pan" in user_weapon:
                from weapons import bronze_Pan
                replay1.replay(chef, B , bronze_Pan)
            elif "silver_pan" in user_weapon:
                from weapons import silver_Pan
                replay1.replay(chef, B , silver_Pan)
            elif "mythril_pan" in user_weapon:
                from weapons import mythril_Pan
                replay1.replay(chef, B , mythril_Pan)
        elif "blacksmith" in user_class:
            if "hammer" in user_weapon:
                from weapons import Hammer
                replay1.replay(BlackSmith, B , Hammer)
            else: 
                print("something broke")
grinding.rewind_time()

