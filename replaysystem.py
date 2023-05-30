
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
             sprint("grraH, THE ZOMBIE SCROOM EATS YOU AND YOU DIE")




