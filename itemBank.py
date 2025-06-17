import time
import random
class ItemBank:
    def __init__(self):
        self.items = [
            "Health Potion",
            "Stamina Potion",
            "Bomb"
        ]

    def use_item(self, user, target, item):
        match item:
            case "Health Potion":
                self._health_potion(user)
            case "Stamina Potion":
                self._stamina_potion(user)
            case "Bomb":
                self._bomb(user, target)

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
        if 0 <= boom and boom <= 0.75:
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
