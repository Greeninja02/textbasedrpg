import random
import time
import options
import enemies
import items


class Character:
    def __init__(self, name, hp, max_hp, inv):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.inv = inv


def start():
    name = input('What is your name\n>>').title()
    global char
    char = Character(name, 20, 20, [random.choice(list(items.item_list['lg weapons'])), random.choice(list(items.item_list['lg healing']))])


start()


# where the player is currently and where they are going
def player_choice(current, combat):

    clear = lambda: print('\n' * 150)
    clear()
    for l in options.choices:
        if current in options.choices[l]:
            option = options.choices[l][current]
            break
        else:
            continue

    # creates the options for the available locations
    loc_options = [random.choice(list(options.choices[option.option1])), random.choice(list(options.choices[option.option2]))]

    time.sleep(0.5)

    # gives user loot if current location has loot
    for loot in option.loot:
        if loot == None:
            continue
        char.inv.append(random.choice([loot, None]))
        if None in char.inv:
            char.inv.remove(None)
        else:
            print(f'You picked up {loot}.\n')

    time.sleep(1)

    print(option.desc)

    time.sleep(3)

    # let the player retype if they make a typing error
    def typing_error():
        print('You may have mistyped your destination.\n')
        retype_choice = input('Where does {} wish to go?\n{} or {}\n>>'.format(char.name, loc_options[0], loc_options[1])).title()
        if retype_choice not in loc_options:
            typing_error()
        player_choice(retype_choice, 1)

    # combat turns for the player and enemy
    def turns(enemy, e_hp, e_count, e_dmg):

        # ends combat if no enemies are left
        if e_count == 0:
            player_choice(current, 0)

        if e_count > 1:
            print('\nThere are {} {}s left!'.format(e_count, enemy))
        else:
            print('\nThere is {} {} left!'.format(e_count, enemy))

        for enemy_type in enemies.enemy_list:
            if enemy in enemy_type:
                break
            else:
                continue
        cur_enemy = enemies.enemy_list[enemy_type]

        # current enemy hp
        if e_hp == None:
            e_hp = random.randint(cur_enemy[option.enemies].hp_min, cur_enemy[option.enemies].hp_max)

        # for testing
        # print(e_dmg)
        # print(hp)

        time.sleep(2)

        combat_options = ['Inventory', 'Run']
        print('\n{}\'s Health - {}'.format(char.name, char.hp))
        combat_choice = input('What does {} want to do?\nInventory    Run\n>>'.format(char.name, str(char.inv))).title()

        # avoids errors if the user mistypes their combat decision
        while combat_choice not in combat_options:
            print('You may have mistyped your decision.')
            time.sleep(1)
            print('\n{}\'s Health - {}'.format(char.name, char.hp))
            combat_choice = input('What does {} want to do?\nInventory    Run\n>>'.format(char.name, str(char.inv))).title()

        # the player can choose to try and run away from combat, if they fail they will be attacked
        if combat_choice == 'Run':
            run = random.randint(1, 3)
            if run == 1:
                time.sleep(1)
                print('\nyou succeed in running away')
                time.sleep(1)
                player_choice(current, 0)
            else:
                time.sleep(1)
                print('\nYou failed to run away.')
                time.sleep(1)
                while e_dmg < e_count:
                    enemy_attack = random.randint(cur_enemy[option.enemies].dmg_min, cur_enemy[option.enemies].dmg_max)
                    print('\n{} deals {} damage to {}!'.format(enemy, enemy_attack, char.name))
                    char.hp -= enemy_attack
                    e_dmg += 1
                    time.sleep(1)
                print('{} has {} hp left!'.format(char.name, char.hp))

                time.sleep(2)
                turns(enemy, e_hp, e_count, 0)

        # the player can choose to open their inventory to view the items they can use for combat
        elif combat_choice == 'Inventory':
            print(char.inv)
            item_choice = input('What item does {} want to use?\n>>'.format(char.name)).title()

            # avoids errors if the user mistypes an item name
            while item_choice not in char.inv:
                print('You may have mistyped the item name.')
                time.sleep(1)
                print(f'\n{char.inv}')
                item_choice = input('What item does {} want to use?\n>>'.format(char.name)).title()

            for item in items.item_list:
                if item_choice in items.item_list[item]:
                    break
                else:
                    continue

            # if the enemy is faster than the player, the enemy attacks first
            if cur_enemy[enemy].spd > items.item_list[item][item_choice].spd:

                # enemy attacks the player
                time.sleep(1)
                while e_dmg < e_count:
                    enemy_attack = random.randint(cur_enemy[option.enemies].dmgmin, cur_enemy[option.enemies].dmgmax)
                    print('\n{} deals {} damage to {}!'.format(enemy, enemy_attack, char.name))
                    char.hp -= enemy_attack
                    e_dmg += 1
                    time.sleep(1)
                print('{} has {} hp left!'.format(char.name, char.hp))

                # attacks the enemy if the player used a weapon
                if items.item_list[item][item_choice].type == 'attack':

                    # player attacks the enemy
                    time.sleep(2)
                    # gets a dmg number from the selected items range
                    player_attack = random.randint(items.item_list[item][item_choice].minvalue, items.item_list[item][item_choice].maxvalue)
                    print('\n{} deals {} damage to {}!'.format(char.name, player_attack, enemy))
                    time.sleep(1)

                    e_hp -= player_attack
                    print('{} has {} hp left!'.format(enemy, e_hp))
                    time.sleep(1)

                # heals the player if they used a healing item
                elif items.item_list[item][item_choice].type == 'heal':
                    time.sleep(1)
                    player_heal = random.randint(items.item_list[item][item_choice].min_value, items.item_list[item][item_choice].max_value)
                    while char.hp + player_heal > char.max_hp:
                        player_heal -= 1
                    char.hp += player_heal
                    print('{} healed themself for {} hp'.format(char.name, player_heal))
                    char.inv.remove(item_choice)

                    # if the enemy has no hp, get a new target
                    if e_hp < 1:
                        print('\n{} has defeated {}!'.format(char.name, enemy))
                        e_hp = random.randint(cur_enemy[option.enemies].hp_min, cur_enemy[option.enemies].hp_max)
                        e_count -= 1
                        time.sleep(1)
                        turns(enemy, e_hp, e_count, 0)

                    time.sleep(2)
                    turns(enemy, e_hp, e_count, 0)

            # if the player is faster than the enemy, the player attacks first
            else:
                # attacks the enemy if the player used a weapon
                if items.item_list[item][item_choice].type == 'attack':
                    # player attacks the enemy
                    time.sleep(1)
                    # gets a dmg number from the selected items range
                    player_attack = random.randint(items.item_list[item][item_choice].min_value, items.item_list[item][item_choice].max_value)
                    print('\n{} deals {} damage to {}!'.format(char.name, player_attack, enemy))
                    time.sleep(1)

                    e_hp -= player_attack
                    print('{} has {} hp left!'.format(enemy, e_hp))
                    time.sleep(1)

                    # if the enemy has no hp, get a new target
                    if e_hp < 1:
                        print('\n{} has defeated {}!'.format(char.name, enemy))
                        e_hp = random.randint(cur_enemy[option.enemies].hp_min, cur_enemy[option.enemies].hp_max)
                        e_count -= 1
                        time.sleep(1)

                # heals the player if they used a healing item
                elif items.item_list[item][item_choice].type == 'heal':
                    time.sleep(1)
                    player_heal = random.randint(items.item_list[item][item_choice].min_value, items.item_list[item][item_choice].max_value)
                    while char.hp + player_heal > char.max_hp:
                        player_heal -= 1
                    char.hp += player_heal
                    print('{} healed themself for {} hp'.format(char.name, player_heal))
                    char.inv.remove(item_choice)

                # enemy attacks the player
                time.sleep(1)
                while e_dmg < e_count:
                    enemy_attack = random.randint(cur_enemy[option.enemies].dmg_min, cur_enemy[option.enemies].dmg_max)
                    print('\n{} deals {} damage to {}!'.format(enemy, enemy_attack, char.name))
                    char.hp -= enemy_attack
                    e_dmg += 1
                    time.sleep(1)
                if e_count > 0:
                    print('{} has {} hp left!'.format(char.name, char.hp))

                time.sleep(2)
                turns(enemy, e_hp, e_count, 0)


    #starts combat if there are enemies in the location, otherwise you choose a new location to go to
    loc_enemy_count = random.randint(0, option.count)
    if loc_enemy_count > 0 and combat == 1:
        if loc_enemy_count > 1:
            print('\n{} has been attacked by a group of {} {}s!'.format(char.name, loc_enemy_count, option.enemies))
        else:
            print('\n{} has been attacked by {}!'.format(char.name, option.enemies))
        time.sleep(1)
        turns(option.enemies, 0, loc_enemy_count, 0)
    else:
        choice = input('\nWhere does {} wish to go?\n{} or {}\n>>'.format(char.name, loc_options[0], loc_options[1])).title()
        if choice not in loc_options:
            typing_error()
        if char.hp < char.max_hp:
            char.hp += 1
        player_choice(choice, 1)


player_choice(random.choice(list(options.choices['start'])), 1)
