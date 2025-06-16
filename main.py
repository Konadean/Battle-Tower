import player as p
import enemy as e
import random
import battle

# TO DO
# Item Bank
# Enemy AI
#   attacks
#   skills

def startup():
    n = input("Enter your name! : ")
    return p.Player(n,20,5,2,15,10)

def main():
    p1 = startup()
    battleCount = 1
    while True:
        e1 = e.Enemy(battleCount)
        p1.get_stats()
        print("~"*(16+len(str(battleCount))))
        print("Entering Floor #" + str(battleCount) + "\nEnemy : " + e1.name)
        print("~"*(16+len(str(battleCount))))
        # Create and start battle instance
        b = battle.Battle(p1, e1)
        if b.battle_cycle() == -1:
            break
        else:
            battleCount += 1
        # print("exited battle cycle")

if __name__=="__main__":
    main()