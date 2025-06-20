import time
import random
class ItemBank:
    def __init__(self):
        self.items = [
            "Health Potion",
            "Stamina Potion",
            "Bomb",
            "Power Pill",
            "Fabric Softener",
            "Cursed Nail"
        ]

    def use_item(self, user, target, item):
        match item:
            case "Health Potion":
                self._health_potion(user)
            case "Stamina Potion":
                self._stamina_potion(user)
            case "Bomb":
                self._bomb(user, target)
            case "Power Pill":
                self._power_pill(user)
            case "Fabric Softener":
                self._fabric_softener(user, target)
            case "Cursed Nail":
                self._cursed_nail(user, target)

    def _health_potion(self, user):
        print(user.name + "'s HP has been fully restored!")
        user.hp = user.max_hp

    def _stamina_potion(self, user):
        print(user.name + "'s SP has been fully restored!")
        user.sp = user.max_sp

    def _bomb(self, user, target):
        print(user.name + " threw a bomb at " + target.name + "!")
        print('...\n')
        time.sleep(1.5)
        boom = random.random()
        if 0 <= boom and boom <= 0.70:
            print("     _.-^^---....,,--      ")
            print(" _--                  --_  ")
            print("<                        >)")
            print("|                         |")
            print(" \\._                   _./ ")
            print("    ```--. . , ; .--'''    ")
            print("          | |   |          ")
            print("       .-=||  | |=-.       ")
            print("       `-=#$%&%$#=-'       ")
            print("          | ;  :|          ")
            print(" _____.,-#%&$@%#&#~,._____ ")
            print("\nKABOOM!! " + target.name + " is completely annihilated!\n")
            target.hp = 0
        else:
            print("Fuse didn't light... Nothing happened.")

    def _power_pill(self, user):
        print(user.name + "'s ATK has been permanently increased by 3!!!")
        user.atk += 3

    def _fabric_softener(self,user,target):
        print(target.name+ "'s DEF has been permenantly reduced by 3!")
        user.atk = user.atk - 3 if user.atk - 3 > 0 else 0
    
    def _cursed_nail(self,user,target):
        print("""
     .-.
   .'   `.
   :g g   :
   : o    `.
  :         ``.
 :             `.
:  :         .   `.
:   :          ` . `.
 `.. :            `. ``;
    `:;             `:'
       :              `.
        `.              `.     .
          `'`'`'`---..,___`;.-'
            """)
        print("OOoooOOOooOOooo!! A ghost drains both " + user.name + "'s and " + target.name + "'s life to 1 HP!")
        user.hp = 1
        target.hp = 1
