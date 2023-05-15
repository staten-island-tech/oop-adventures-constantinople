class start:
    def beginning():
        print("You have now been transported into the world of an ancient lineage. ")
        everything = input("Would you like to become an orderly, neutral, or chaotic class? ").upper()
        if everything == "ORDERLY":
            import Orderly
            from Orderly import *
            class1 = input("What class would you like to progress in?: 'Sigil Knight' or 'Whisperer' ").upper()
            if class1 == "SIGIL KNIGHT": 
                user_class = A
        elif everything == "CHAOTIC":
            import Chaotic
        elif everything == "NEUTRAL":
            import Neutral
        else:
            print("Iagnime not bineg albe to selpl...")
            start.beginning()
start.beginning()


