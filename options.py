import random
import items
import enemies


class Option:
    def __init__(self, description, option1, option2, enemy, count, loot):
        self.desc = description
        self.option1 = option1
        self.option2 = option2
        self.enemy = enemy
        self.count = count
        self.loot = loot


randomEnemy = lambda: random.choice(list(enemies.enemy_list[random.choice(list(enemies.enemy_list))]))

lg_weapons = random.choice(list(items.itemlist['lg weapons']))
mg_weapons = random.choice(list(items.itemlist['mg weapons']))
hg_weapons = random.choice(list(items.itemlist['hg weapons']))

lg_healing = random.choice(list(items.itemlist['lg healing']))
mg_healing = random.choice(list(items.itemlist['mg healing']))
hg_healing = random.choice(list(items.itemlist['hg healing']))

#  lg_general = random.choice(list(items.item_list['lg general']))
#  mg_general = random.choice(list(items.item_list['mg general']))
#  hg_general = random.choice(list(items.item_list['hg general']))


town = random.choice(list(['towns', 'location']))
castle = random.choice(list(['castles', 'castles']))

choices = {
    'start': {
        'Old Cabin': Option('You wake up in a dusty old cabin filled with cobwebs.', 'location', 'location', None, 0, []),
        #  'Destroyed Camp': Option('You awake to the sound of thunder in your ransacked camp.', 'towns', 'location', None, 0, []),
        #  'Cathedral': Option('You wake up in a bed inside of a cathedral within a castle.', 'castles', 'location', None, 0, []),
    },
    'location': {
        'Grassy Plains': Option('Mostly flat grassy plains all around.', town, 'location', None, 0, []),
        'Flower Field': Option('Open grassy field with colorful flowers dotting the land.', 'location', 'location', None, 0, []),
        'Grassy Hills': Option('Grassy hills as far as the eye can see.', town, 'location', None, 0, []),
        'Large River': Option('A large river in terms of both depth, and length.', castle, 'location', None, 0, []),
        'Sparse Oak Forest': Option('A sparse forest containing mostly oak trees.', castle, 'location', None, 0, []),
        'Dense Oak Forest': Option('A dense forest containing mostly oak trees.', town, 'location', None, 0, []),
        'Sparse Birch Forest': Option('A sparse forest containing mostly birch trees.', castle, 'location', None, 0, []),
        'Dense Birch Forest': Option('A dense forest containing mostly birch trees.', town, 'location', None, 0, []),
    },
    'castles': {
        'Ruined Castle Gate': Option('An old castle gate with crumbling mossy bricks.', 'ruinedcastle', 'location', None, 0, []),
        #'Abandoned Castle Gate': Option('A seemingly empty castle, it doesnt look too old.', 'abandoncastle', 'location', None, 0, []),
    },
    'ruinedcastle': {
        'Ruined Castle Hall': Option('A long old hall with armor stands to the sides', 'ruinedcastle', 'location', randomEnemy(), 1, []),
    },
    'abandoncastle': {

    },
    'populatedcastle': {

    },
    'towns': {
        'Mining Town': Option('A mining town with smoke clouding the sky above.', 'miningtown', 'location', None, 0, []),
    },
    'miningtown': {

    },
    'livestocktown': {

    },
    'farmingtown': {

    }
}