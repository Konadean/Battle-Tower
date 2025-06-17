import skillBank as sb
import random
class Enemy:
    # Enemies will have no sp
    # They will have only 3 skills to choose from + a basic attack
    # They will also have a chance to drop items
    def __init__(self, battleCount):
        self.name = self.nameler()
        self.max_hp = 5 + random.randint(1+battleCount,5+battleCount)
        self.hp = self.max_hp
        self.atk = battleCount + random.randint(1,5)
        self.dfs = random.randint(1+battleCount,5+battleCount)
        self.crit = 10 + battleCount if (10 + battleCount < 100) else 100
        self.xp_reward = 5 + battleCount + random.randint(1,5) if battleCount < 20 else battleCount + random.randint(5,10)
        self.item_drop = 1
        self.sb = sb.SkillBank()
        self.skills = self.acquire_skills()

    def nameler(self):
        partA = ["Petulant","Eager","Foolish","Chance the","Tyler the","Suspicious","Meticulous","Strange","Foreign","Giddy","Genius","Bored","Wacko","X-treme","Motion","Arrogant"]
        partB = ["Dog","Swindler","Dummy","Man","Rapper","Porter","Waggler","Enforcer","Acedemic","Practitioner","Slumlord","Gambler","Child","Ambassador","Crocodile","Padewon","Creator"]
        return partA[random.randint(0,len(partA)-1)] + " " + partB[random.randint(0,len(partB)-1)]
    
    def acquire_skills(self):
        ls = list(self.sb.skills.items())
        skills = []
        while len(skills) < 3:
            skills.append(random.randint(1, len(ls)))
        return skills

