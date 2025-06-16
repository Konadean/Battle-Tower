# Creates a battle instance and controls the combat flow
import random as rand
import player as p
import enemy as e

class Battle:
    def __init__(self, player:p, enemy:e):
        self.player = player
        self.enemy = enemy

    def _is_crit(self, attacker) -> bool:
        crt = rand.random()
        return 0 <= crt and crt <= attacker.crit/100

    def _calc_dmg(self, raw_dmg, defense):
        # Every 10 pts of defense reduces 1 pt of dmg
        return raw_dmg - round(defense/10)

    # Keep Attack function generic for both basic attack and dmg dealing skills
    def _attack(self, attacker, defender, dmg) -> bool:
        # print("Entered attack method")
        if self._is_crit(attacker):
            dmg *= 2
            print("CRIT!")
        dmg = self._calc_dmg(round(dmg), defender.dfs)
        print(defender.name + " took [" + str(dmg) + "] DMG!")
        defender.hp -= dmg
        return True

    def _draw_health_bars(self) -> None:
        print("\nPLAYER HP: " + str(self.player.hp) + " [" + '+'*round(self.player.hp/5) + "] ENEMEY HP: " + str(self.enemy.hp) + " [" + '+'*round(self.enemy.hp/5) + ']')

    def _end_battle(self, winner) -> None:
        if winner:
            print("\n<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>")
            print("You Have Won! You Have Gained " + str(self.enemy.xp_reward) + " EXP!")
            # Lvlup check
            if self.player.xp + self.enemy.xp_reward >= self.player.xp2next:
                print("You have leveled up! All stats increased by 1")
                print("HP and SP have been fully restored!")
                self.player.lvlup(self.player.xp + self.enemy.xp_reward - self.player.xp2next)
            #No lvl up -> add exp to exp stat
            else:
                self.player.xp += self.enemy.xp_reward
            print("<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>\n")
        else:
            print("YOU DIED. EXITING GAME.")
            return -1

    def battle_cycle(self) -> None:
        turn = True
        while True:
            # Draw battle status
            self._draw_health_bars()
            # \/ \/ \/ \/ \/ PLAYER TURN \/ \/ \/ \/ \/
            if turn:
                turn_end = False
                while not turn_end:
                    print("\n====================")
                    action = input("What will you do?\nType `1` to Attack!\nType `2` to use a skill!\nType `3` to use an item!\nCHOICE : ")
                    print("====================\n")
                    if action == '1':
                        turn_end = self._attack(self.player, self.enemy, self.player.atk)
                    elif action == '2':
                        dmg = self.player.use_skill(self.enemy)
                        # 0 = buff/debuff / -1 = 'q' was pressed
                        if dmg[0] == -1:
                            pass
                        elif dmg[0] == 0:
                            turn_end = True
                        else:
                            for dmg_instance in dmg:
                                turn_end = self._attack(self.player, self.enemy, dmg_instance)
                    elif action == '3':
                        turn_end = self.player.use_item()
                # Kill Check
                if self.enemy.hp <= 0:
                    self._end_battle(True)
                    break
            # \/ \/ \/ \/ \/ ENEMY TURN \/ \/ \/ \/ \/
            else:
                print("\n" + self.enemy.name + "'s turn!")
                # Mimic Player Call Enemy Decision Making
                e_decision = rand.randint(0,3)
                if e_decision == 3:
                    print(self.enemy.name + " attacks!")
                    self._attack(self.enemy, self.player, self.enemy.atk)
                else:
                    dmg = self.enemy.sb.use_skill(self.enemy, self.player, self.enemy.skills[e_decision])
                    if dmg[0] == 0:
                        pass
                    else:
                        for dmg_instance in dmg:
                            self._attack(self.enemy, self.player, dmg_instance)
                # Kill Check
                if self.player.hp <= 0:
                    return self._end_battle(False)
            turn = not turn
            
        
        
                
