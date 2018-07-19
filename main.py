from classes.game import Person
from classes.magic import Spell
from classes.inventory import Item

# B Magic
blaze = Spell("Blaze", 10, 100, "BM")
freeze = Spell("Freeze", 10, 100, "BM")
spark = Spell("Spark", 10, 100, "BM")

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

player_magic = [blaze, freeze, spark, heal, medica]
player_items = [{"item": potion, "quantity": 5},
                {"item": hipotion, "quantity": 2},
                {"item": xpotion, "quantity": 1},
                {"item": elixir, "quantity": 1},
                {"item": elixirbomb, "quantity": 1},
                {"item": grenade, "quantity": 5}]

# instantiate player
player = Person(500, 100, 40, 30, player_magic, player_items)
# instantiate enemy
enemy = Person(1200, 40, 40, 10, [], [])

running = True

print("\n\nAn enemy spawned before you!")

while running:
    print("\n=============================\n")
    player.choose_action()
    choice = input("Choose action:\n")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("\nYou attacked for", dmg)
    elif index == 1:
        player.choose_magic()
        choice = int(input("Choose magic:\n")) - 1

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
            enemy.take_damage(magic_dmg)
            print(spell.name, "deals", magic_dmg, "damage")
    elif index == 2:
        player.choose_item()
        choice = int(input("Choose item:\n")) - 1

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
            player.hp = player.maxhp
            player.mp = player.maxmp
            print("\n" + item.name, "fully restored your HP/MP")
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print("\n" + item.name, "deals", str(item.prop), "damage to the enemy!")

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "damage")

    print("\n*****************************\n")
    print("Player HP:", str(player.get_hp()) + "/" + str(player.get_max_hp()) + " | Player MP: " + str(player.get_mp()) + "/" + str(player.get_max_mp()))
    print("Enemy HP:", str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()))

    if enemy.get_hp() <= 0:
        print("\nYou defeated the enemy!")
        running = False
    elif player.get_hp() <= 0:
        print("\nYou have been defeated")
        running = False
