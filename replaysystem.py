
import sys, time
def sprint(str):
    for c in str  + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./250)

class replay1():
    def replay(x,y,z):
        y.HP = int(160)
        x.Attack(y,z)
        ask = input('Another one enemy approachs. Attack or run?').upper()
        while ask == 'ATTACK':
            y.HP = int(160)
            x.Attack(y,z)
            ask = input('Another one enemy approachs. Attack or run?').upper()
        if ask == 'RUN':
             sprint("The zombie scroom is catching UP!")
             sprint("No matter how hard u run it continues...")
             sprint("You utilize your 'Last Wind' given to you by your mentor, whoever that may be.")
             please = input("You turn around, WOULD YOU LIKE TO FIGHT?").upper()
             while please == "YES":
                y.HP = int(160)
                x.Attack(y,z)
                please = input('Another one enemy approachs. Attack or run?').upper()
             if please != "YES":
                sprint("You lay down your weapon and die. ")
             else:
                sprint("grraH, THE ZOMBIE SCROOM EATS YOU AND YOU DIE")




