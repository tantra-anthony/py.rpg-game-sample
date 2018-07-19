import random
    
class Person:
    def __init__(self, hp, mp, atk, df, mag, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.mag = mag
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']
        
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)
    
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def heal(self, heal_amt):
        self.hp += heal_amt
        if self.hp > self.maxhp:
            self.hp = self.maxhp
    
    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ".", item)
            i += 1
        
    def choose_magic(self):
        i = 1
        print("Magic")
        for magic in self.mag:
            print ("    " + str(i) + ".", magic.name, "(cost:", str(magic.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("Items")
        for items in self.items:
            print("    " + str(i) + ".", items["item"].name, "(" + items["item"].description + ")", "x" + str(items["quantity"]))
            i += 1