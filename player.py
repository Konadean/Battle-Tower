import skillBank as sb
import itemBank as ib
class Player:
    def __init__(self, name, max_hp, atk, dfs, crit, max_sp):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.dfs = dfs
        self.crit = crit
        self.max_sp = max_sp
        self.sp = max_sp
        self.lvl = 1
        self.xp = 0
        self.xp2next = 20
        self.inventory = {"Health Potion" : 1, "Stamina Potion" : 1, "Bomb" : 1}
        self.skills = {"Big Hit" : 2}
        self.ib = ib.ItemBank()
        self.sb = sb.SkillBank()

#=======================INVENTORY METHODS=======================
    def add_item(self, item):
        try:
            self.inventory[item] += 1
        except KeyError:
            self.inventory[item] = 1
    # Player Inventory Handles the stock; IB handles the ID's
    def use_item(self, target) -> bool:
        while True:
            self.show_inv()
            choice  = input("Type Number of the Item You Want To Use or 'q' to return to Action Menu\nCHOICE: ")
            try:
                if choice == 'q':
                    return
                elif int(choice) > 0:
                    item = list(self.inventory.keys())[int(choice)-1]
                    print("Used a(n) " + item + "!")
                    self.ib.use_item(self, target, item)
                    # --===Stock Handling==--
                    if self.inventory[item]-1 == 0:
                        del self.inventory[item]
                    else:
                        self.inventory[item] -= 1
                    # --===================--
                    return True
                else:
                    print("\nChoose a valid item!")
            except ValueError:
                print("\nChoose a valid item!")
#===============================================================

#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓=LEVEL UP METHODS=↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    def _skill_check(self):
        if self.sb.can_learn_new_skills(self.lvl):
            try:
                next_skill = list(self.sb.skills.items())[self.lvl]
                self.skills[next_skill[0]] = next_skill[1]
                print("Learned a new skill: [" + next_skill[0] + "]!")
            except IndexError:
                pass

    def lvlup(self, extraXP:int) -> None:
        # print("Entered lvlup method")
        self._skill_check()
        self.max_hp += 1
        self.hp = self.max_hp
        self.atk += 1
        self.dfs += 1
        self.crit += 1
        self.max_sp += 1
        self.sp = self.max_sp
        self.lvl += 1
        self.xp = extraXP
        self.xp2next += 10
#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑=LEVEL UP METHODS=↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

#=======================SKILL USAGE METHODS=======================
    def enough_sp(self, choice, curr_sp):
        return list(self.skills.items())[choice-1][1] <= curr_sp
   
    def use_skill(self, enemy) -> list[int]:
        while True:
            self.show_skills()
            choice  = input("Type Number of the Skill You Want To Use or 'q' to return to Action Menu\nCHOICE : ")
            try:
                if choice == 'q':
                    return [-1]
                elif int(choice) > 0:
                    choice = int(choice)
                    try:
                        sp_cost = list(self.skills.items())[choice-1][1]
                        enough_sp = sp_cost <= self.sp
                        if enough_sp:
                            self.sp -= sp_cost
                            return self.sb.use_skill(self, enemy, choice)
                        else:
                            print("Not enough SP to use that skill!")
                    except IndexError:
                        print("\nChoose a valid skill!")
                else:
                    print("\nChoose a valid skill!")
            except ValueError:
                print("\nChoose a valid skill!")
#=======================SKILL USAGE METHODS=======================


#=======================PRINTER METHODS=======================
    def get_stats(self) -> None:
        l = len(self.name)
        t = l + 10
        print("\n========" + self.name + "========")
        print("LVL--" + '-'*(t-len(str(self.lvl))) + str(self.lvl))
        print("EXP--" + '-'*(t-(1+len(str(self.xp))+len(str(self.xp2next)))) + str(self.xp) + '/' + str(self.xp2next))
        print("HP---" + '-'*(t-(1+len(str(self.hp))+len(str(self.max_hp)))) + str(self.hp) + '/' + str(self.max_hp))
        print("ATK--" + '-'*(t-len(str(self.atk))) + str(self.atk))
        print("DEF--" + '-'*(t-len(str(self.dfs))) + str(self.dfs))
        print("CRIT-" + '-'*(t-1-len(str(self.crit))) + str(self.crit) + '%')
        print("SP---" + '-'*(t-(1+len(str(self.sp))+len(str(self.max_sp)))) + str(self.sp) + '/' + str(self.max_sp))
        print("========" + "="*l + "========\n")

    def show_skills(self):
        i = 1
        print("\n=========SKILLS=========")
        for key, val in self.skills.items():
            print(str(i) + ". " + key + ' '*(23 - len(str(i)) - 2 - len(key) - len(str(val)) - 4 - len(str(val))) + "SP: " + str(val))
            i += 1
        print("========================\n")
    
    def show_inv(self) -> None:
        i = 1
        print("========INVENTORY========")
        for key, val in self.inventory.items():
            print(str(i) + ". " + key + ' '*(23 - len(str(i)) - 2 - len(key) - len(str(val)) - 1 - len(str(val))) + "x" + str(val))
            i += 1
        print("=========================")
#=======================PRINTER METHODS=======================
