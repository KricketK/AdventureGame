__author__ = 'KRISTINE'


import random
from RPgame import *


class Item(object):
    def __init__(self, effect):
        self.effect = effect


class UserItem(Item):
    def __init__(self, *args, **kwargs):
        super(UserItem, self).__init__(*args, **kwargs)
        harm = random.randrange(user.health, user.attack, user.defense) - random.randint(1, 3)
        aid = random.randrange(user.health, user.attack, user.defense) + random.randint(1, 3)
        self.effect = random.randrange(harm, aid)


class EnemyItem(Item):
    def __init__(self, *args, **kwargs):
        super(EnemyItem, self).__init__(*args, **kwargs)
        harm = random.randrange(Hickory.health, Hickory.attack, Hickory.defense) - random.randint(1, 3)
        aid = random.randrange(Hickory.health, Hickory.attack, Hickory.defense) + random.randint(1, 3)
        self.effect = random.randrange(harm, aid)