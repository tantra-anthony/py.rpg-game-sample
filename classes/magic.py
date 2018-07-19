import random

class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type
        
    def generate_damage(self):
        magl = self.dmg - 15
        magh = self.dmg + 15
        return random.randrange(magl, magh)