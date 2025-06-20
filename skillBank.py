import random
import time
import ItemBank as ib
# Generic Skill Repository that both the Player and Enemy Classes can use
class SkillBank:
    def __init__(self):
        self.skills = {
            "Big Hit" : 2,
            "Heal" : 3,
            "Strenthening" : 4,
            "Double Hit" : 5,
            "Double Down" : 4,
            "Finger Punches" : 6,
            "Weaken" : 3,
            "Lucky Strikes" : 5,
            "Scavenge" : 1
        }
        self.ib = ib.ItemBank()

    def can_learn_new_skills(self, lvl):
        return lvl <= len(self.skills)

    def use_skill(self, user, target, choice):
        match choice:
            case 1:
                return self._Big_Hit(user)
            case 2:
                return self._Heal(user)
            case 3:
                return self._Strenthening(user)
            case 4:
                return self._Double_Hit(user)
            case 5:
                return self._Double_Down(user)
            case 6:
                return self._Finger_Punches(user)
            case 7:
                return self._Weaken(user, target)
            case 8:
                return self._Lucky_Strikes(user)
            case 9:
                return self._Scavenge(user, target)

    # ===============SKILLS===============
    # All skills must return an attack queue
    # Attack queues hold all damage instances that the skills has
    # Skills that don't damage but instead perform a status effect have singleton 0 attack queues
    # ===================================
    def _Big_Hit(self, user) -> list[int]:
        print("\n" + user.name + " has used skill [Big Hit]")
        # Deals 130% of atk
        return [round(user.atk*1.3)]
    
    def _Heal(self, user) -> list[int]:
        heal_amount = round(user.max_hp*.5)
        print("\n" + user.name + " has used skill [Heal]")
        print(user.name + " is Healed for " + str(heal_amount) + " HP!")
        if user.hp + heal_amount >= user.max_hp:
            user.hp = user.max_hp
        else:
            user.hp += heal_amount
        return [0]

    def _Strenthening(self, user) -> list[int]:
        print("\n" + user.name + " has used skill [Strenthening]")
        print(user.name +  "'s atk has permantly increased by [1]!")
        user.atk += 1
        return [0]

    def _Double_Down(self, user) -> list[int]:
        print("\n" + user.name + " has used skill [Double Down]")
        print(user.name + "'s Crit Chance has permantly increased by [1%]!")
        user.crit += 1
        return [0]

    def _Double_Hit(self, user) -> list[int]:
        print("\n" + user.name + " has used skill [Double Hit]")
        # Hits twice for 70% ATK each; acheived via called twice
        return [round(user.atk*.7),round(user.atk*.7)]
    
    def _Finger_Punches(self, user) -> list[int]:
        print("\n" + user.name + " has used skill [Finger Punches]")
        # Hits 5 times for 25% ATK each
        return [round(user.atk*.25),round(user.atk*.25),round(user.atk*.25),round(user.atk*.25),round(user.atk*.25)]
    
    def _Weaken(self, user, target) -> list[int]:
        print("\n" + user.name + " has used skill [Weaken]")
        # Reduces the target's ATK by 1
        print(target.name + "'s ATK has been permenantly reduced by 1")
        target.atk -= 1
        return [0]
    
    def _Lucky_Strikes(self, user) -> list[int]:
        # CRIT% chance each time to hit for (100-10*x)% of ATK where x is the amount of bonus strikes used
        print("\n" + user.name + " has used skill [Lucky Strikes]")
        count = 1
        modifier = 1
        atk_q = [round(user.atk*modifier)]
        while True:
            k = random.random()
            if 0 <= k and k < user.crit/100:
                count += 1
                modifier -= 0.10
                atk_q.append(round(user.atk*modifier) if round(user.atk*modifier) > 1 else 1)
            else:
                break
        print(user.name + " will hit " + str(count) + " time(s)!")
        return atk_q
    
    def _Scavenge(self, user, target):
        # Generates a random item and uses it!
        item = self.ib.items[random.randint(0,len(self.ib.items)-1)]
        print(user.name + " rummaged around .....")
        time.sleep(1)
        print(user.name + " used a(n) " + item + "!")
        self.ib.use_item(user, target, item)
        
    
    
