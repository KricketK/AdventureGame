__author__ = 'KRISTINE'

import random


class Weapon(object):
    def __init__(self):
        self.attack_power = 0
        self.attack_penalty = 0


class Club(Weapon):
    def __init__(self):
        super(Club, self).__init__()
        self.attack_power = 4
        self.attack_penalty = 0


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__()
        self.attack_power = 5
        self.attack_penalty = 1


class Axe(Weapon):
    def __init__(self):
        super(Axe, self).__init__()
        self.attack_power = 4
        self.attack_penalty = 1


class Knife(Weapon):
    def __init__(self):
        super(Knife, self).__init__()
        self.attack_power = 3
        self.attack_penalty = 1


class Dart(Weapon):
    def __init__(self):
        super(Dart, self).__init__()
        self.attack_power = 2
        self.attack_penalty = 1


class Poison(Weapon):
    def __init__(self):
        super(Poison, self).__init__()
        self.attack_power = random.randint(1, 5)
        self.attack_penalty = 3


class Pen(Weapon):
    def __init__(self):
        super(Pen, self).__init__()
        self.attack_power = 1
        self.attack_penalty = 0


class Staff(Weapon):
    def __init__(self):
        super(Staff, self).__init__()
        self.attack_power = 3
        self.attack_penalty = 0


class Wand(Weapon):
    def __init__(self):
        super(Wand, self).__init__()
        self.attack_power = 2
        self.attack_penalty = 1


class Bombs(Weapon):
    def __init__(self):
        super(Bombs, self).__init__()
        self.attack_power = 7
        self.attack_penalty = 4


class Elixirs(Weapon):
    def __init__(self):
        super(Elixirs, self).__init__()
        self.attack_power = 4
        self.attack_penalty = 2


class Hyde(Weapon):
    def __init__(self):
        super(Hyde, self).__init__()
        self.attack_power = 7
        self.attack_penalty = 4


class Familiar(Weapon):
    def __init__(self):
        super(Familiar, self).__init__()
        self.attack_power = 7
        self.attack_penalty = 3


class Broomstick(Weapon):
    def __init__(self):
        super(Broomstick, self).__init__()
        self.attack_power = 3
        self.attack_penalty = 1


class GreatSword(Weapon):
    def __init__(self):
        super(GreatSword, self).__init__()
        self.attack_power = 8
        self.attack_penalty = 4


class WarAxe(Weapon):
    def __init__(self):
        super(WarAxe, self).__init__()
        self.attack_power = 8
        self.attack_penalty = 3