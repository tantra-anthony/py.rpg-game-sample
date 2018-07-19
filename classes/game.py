import random
    
class Person:
    def __init__(self, name, hp, mp, atk, df, mag, items):
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
        self.name = name
        
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
        print("\n    " + self.name)
        print("    Actions")
        for item in self.actions:
            print("        " + str(i) + ".", item)
            i += 1
        
    def choose_magic(self):
        i = 1
        print("    Magic")
        for magic in self.mag:
            print ("        " + str(i) + ".", magic.name, "(cost:", str(magic.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("    Items")
        for items in self.items:
            print("        " + str(i) + ".", items["item"].name, "(" + items["item"].description + ")", "x" + str(items["quantity"]))
            i += 1

    def get_enemy_stats(self):
        hp_bar = ""
        hp_bar_length = (self.hp / self.maxhp) * 50

        while hp_bar_length > 0:
            hp_bar += "█"
            hp_bar_length -= 1
        
        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 7:
            decreased = 7 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string
        
        print(self.name + "    " + current_hp + " |" + hp_bar + "|")
        print("")

    def get_stats(self):
        hp_bar = ""
        mp_bar = ""
        hp_bar_length = (self.hp / self.maxhp) * 25
        mp_bar_length = (self.mp / self.maxmp) * 10
        
        while hp_bar_length > 0:
            hp_bar += "█"
            hp_bar_length -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_bar_length > 0:
            mp_bar += "█"
            mp_bar_length -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 7:
            decreased = 7 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 5:
            decreased = 5 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string

        print(self.name + "    " + current_hp + " |" + hp_bar + "|     " + current_mp + "  |" + mp_bar + "|")
        print("")

    def choose_target(self, enemies):
        i = 1
        print("    Target")
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        " + str(i) + ". " + enemy.name)
                i += 1
        choice = int(input("    Choose target:")) - 1
        return choice

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.mag))
        enemy_spell = self.mag[magic_choice]
        magic_dmg = enemy_spell.generate_damage()

        pct = self.hp / self.maxhp * 100

        if self.mp < enemy_spell.cost or enemy_spell.type == "WM" and pct > 50:
            self.choose_enemy_spell()
        else:
            return enemy_spell, magic_dmg

