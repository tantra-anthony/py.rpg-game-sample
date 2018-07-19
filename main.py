from classes.game import Person
from classes.magic import Spell
from classes.inventory import Item
import random

# B Magic
blaze = Spell("Blaze", 10, 100, "BM")
freeze = Spell("Freeze", 10, 100, "BM")
spark = Spell("Spark", 10, 100, "BM")
alterna = Spell("Alterna", 90, random.randrange(1, 1999), "BM")

# W Magic
heal = Spell("Heal", 10, 50, "WM")
medica = Spell("Medica", 20, 100, "WM")

# Items
potion = Item("Potion", "potion", "Heals 30 HP", 30)
hipotion = Item("Hi-Potion", "potion", "Heals 60 HP", 60)
xpotion = Item("X-Potion", "potion", "Heals 100 HP", 100)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
elixirbomb = Item("Elixir Bomb", "elixir", "Fully restores HP/MP of everyone in the party", 9999)

grenade = Item("Grenade", "attack", "Deals 70 damage", 70)

player_magic = [blaze, freeze, spark, alterna, heal, medica]
player_items = [{"item": potion, "quantity": 5},
                {"item": hipotion, "quantity": 2},
                {"item": xpotion, "quantity": 1},
                {"item": elixir, "quantity": 1},
                {"item": elixirbomb, "quantity": 1},
                {"item": grenade, "quantity": 5}]

# instantiate player
player1 = Person("Blooper:", 500, 90, 40, 30, player_magic, player_items)
player2 = Person("Dooper :", 500, 90, 40, 30, player_magic, player_items)
player3 = Person("Clooper:", 500, 90, 40, 30, player_magic, player_items)

# instantiate enemy
enemy1 = Person("Garuda", 4500, 40, 100, 10, [], [])
enemy2 = Person("Birb", 1200, 90, 60, 20, [], [])
enemy3 = Person("Birb", 1200, 90, 60, 20, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True

print("\n\nAn enemy spawned before you!")

while running:
    print("\n=============================\n")

    print("NAME        HP                                      MP")

    for player in players:
        player.get_stats()

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy_chosen = player.choose_target(enemies)
            enemies[enemy_chosen].take_damage(dmg)
            print("\nYou attacked " + enemies[enemy_chosen].name + " for", dmg)

            if enemies[enemy_chosen].get_hp() == 0:
                print(enemies[enemy_chosen].name.replace(' ', '') + " has been defeated!")
                del enemies[enemy_chosen]

        elif index == 1:
            player.choose_magic()
            choice = int(input("    Choose magic: ")) - 1

            if choice == -1:
                continue

            spell = player.mag[choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print("\nNot enough MP!\n")
                continue

            if spell.type == "WM":
                player.heal(magic_dmg)
                print("\n" + spell.name + " heals for", str(magic_dmg), "HP\n")
            elif spell.type == "BM": 
                player.reduce_mp(spell.cost)
                enemy_chosen = player.choose_target(enemies)
                enemies[enemy_chosen].take_damage(magic_dmg)
                print(spell.name, "deals", magic_dmg, "damage to", enemies[enemy_chosen].name)
                
                if enemies[enemy_chosen].get_hp() == 0:
                    print(enemies[enemy_chosen].name.replace(" ", "") + " has been defeated!")
                    del enemies[enemy_chosen]
        elif index == 2:
            player.choose_item()
            choice = int(input("    Choose item: ")) - 1

            if choice == -1:
                continue

            item = player.items[choice]['item']

            if player.items[choice]["quantity"] == 0:
                print("You have none of this item")
                continue

            player.items[choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print("\n" + item.name, "heals for", str(item.prop), "HP")
            elif item.type == "elixir":
                if item.name == "Elixir Bomb":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                    print("\n" + "All members of the party are healed!")
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print("\n" + item.name, "fully restored your HP/MP")
            elif item.type == "attack":
                enemy_chosen = player.choose_target(enemies)

                enemies[enemy_chosen].take_damage(item.prop)
                print("\n" + item.name, "deals", str(item.prop), "damage to " + enemies[enemy_chosen].name)
                    
                if enemies[enemy_chosen].get_hp() == 0:
                    print(enemies[enemy_chosen].name.replace(" ", "") + " has been defeated!")
                    del enemies[enemy_chosen]

    enemy_choice = 1

    enemy_dmg = enemies[0].generate_damage()
    target = random.randrange(0, 3)
    players[target].take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "damage")

    print("\n*****************************\n")

    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    if defeated_enemies == 2:
        print("\nYou defeated the enemy!")
        running = False
    elif defeated_players == 2:
        print("\nYou have been defeated")
        running = False
