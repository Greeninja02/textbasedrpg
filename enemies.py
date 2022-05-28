import items


class Enemy:
    def __init__(self, hp_min, hp_max, dmg_min, dmg_max, spd, inv):
        self.hp_min = hp_min
        self.hp_max = hp_max
        self.dmg_min = dmg_min
        self.dmg_max = dmg_max
        self.spd = spd
        self.inv = inv


enemy_list = {
    'undead': {
        'Skeleton': Enemy(4, 6, 1, 2, 3, ['Bone']),
    },
    'nature': {
        'Bear': Enemy(10, 20, 6, 12, 6, [])
    }
}
