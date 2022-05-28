class item():
    def __init__(self, type, min_value, max_value, spd):
        self.type = type
        self.min_value = min_value
        self.max_value = max_value
        self.spd = spd

item_list = {
    'lg weapons': {
        'Damaged Shortsword': item('attack', 2, 4, 6),
        #'Cracked Broadsword': item('attack', 3, 5, 5),
        #'Broken Claymore': item('attack', 5, 7, 3)
    },
    'mg weapons': {
        'Shortsword': item('attack', 5, 7, 6),
        'Broadsword': item('attack', 7, 9, 5),
        'Claymore': item('attack', 10, 12, 3)
    },
    'hg weapons': {
        'Engraved Shortsword': item('attack', 8, 10, 6),
        'Royal Broadsword': item('attack', 11, 13, 5),
        'Highland Claymore': item('attack', 15, 17, 3)
    },
    'lg healing': {
        'Bandage': item('heal', 7, 9, 10)
    },
    'mg healing': {
        'Small Health Flask': item('heal', 11, 13, 10)
    },
    'hg healing': {
        'Health Potion': item('heal', 15, 17, 10)
    },
    'lg general': {

    },
    'mg general': {

    },
    'hg general': {

    },
}