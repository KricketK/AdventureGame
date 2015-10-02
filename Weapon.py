__author__ = 'KRISTINE'

import random


class Weapon(object):
    def __init__(self, type):
        self.type = type
        self.attack_power = 0
        self.attack_penalty = 0

    def __str__(self):
        return self.type


class OpenHand(Weapon):
    def __init__(self, *args, **kwargs):
        super(OpenHand, self).__init__(*args, **kwargs)
        self.type = "None"
        self.attack_power = -5
        self.attack_penalty = 0


class Club(Weapon):
    def __init__(self, *args, **kwargs):
        super(Club, self).__init__(*args, **kwargs)
        self.type = "Club"
        self.attack_power = 4
        self.attack_penalty = 0


class Sword(Weapon):
    def __init__(self, *args, **kwargs):
        super(Sword, self).__init__(*args, **kwargs)
        self.type = "Sword"
        self.attack_power = 5
        self.attack_penalty = 1


class Axe(Weapon):
    def __init__(self, *args, **kwargs):
        super(Axe, self).__init__(*args, **kwargs)
        self.type = "Axe"
        self.attack_power = 4
        self.attack_penalty = 1


class Knife(Weapon):
    def __init__(self, *args, **kwargs):
        super(Knife, self).__init__(*args, **kwargs)
        self.type = "Knife"
        self.attack_power = 3
        self.attack_penalty = 1


class Dart(Weapon):
    def __init__(self, *args, **kwargs):
        super(Dart, self).__init__(*args, **kwargs)
        self.type = "Dart"
        self.attack_power = 2
        self.attack_penalty = 1


class Poison(Weapon):
    def __init__(self, *args, **kwargs):
        super(Poison, self).__init__(*args, **kwargs)
        self.type = "Poison"
        self.attack_power = random.randint(1, 5)
        self.attack_penalty = 3


class Pen(Weapon):
    def __init__(self, *args, **kwargs):
        super(Pen, self).__init__(*args, **kwargs)
        self.type = "Pen"
        self.attack_power = 1
        self.attack_penalty = 0


class Staff(Weapon):
    def __init__(self, *args, **kwargs):
        super(Staff, self).__init__(*args, **kwargs)
        self.type = "Staff"
        self.attack_power = 3
        self.attack_penalty = 0


class Wand(Weapon):
    def __init__(self, *args, **kwargs):
        super(Wand, self).__init__(*args, **kwargs)
        self.type = "Wand"
        self.attack_power = 2
        self.attack_penalty = 1


class Bombs(Weapon):
    def __init__(self, *args, **kwargs):
        super(Bombs, self).__init__(*args, **kwargs)
        self.type = "Bombs"
        self.attack_power = 7
        self.attack_penalty = 4


class Elixirs(Weapon):
    def __init__(self, *args, **kwargs):
        super(Elixirs, self).__init__(*args, **kwargs)
        self.type = "Elixirs"
        self.attack_power = 4
        self.attack_penalty = 2


class Hyde(Weapon):
    def __init__(self, *args, **kwargs):
        super(Hyde, self).__init__(*args, **kwargs)
        self.type = "Hyde"
        self.attack_power = 7
        self.attack_penalty = 4


class Familiar(Weapon):
    def __init__(self, *args, **kwargs):
        super(Familiar, self).__init__(*args, **kwargs)
        self.type = "Familiar"
        self.attack_power = 7
        self.attack_penalty = 3


class Broomstick(Weapon):
    def __init__(self, *args, **kwargs):
        super(Broomstick, self).__init__(*args, **kwargs)
        self.type = "Broomstick"
        self.attack_power = 3
        self.attack_penalty = 1


class GreatSword(Weapon):
    def __init__(self, *args, **kwargs):
        super(GreatSword, self).__init__(*args, **kwargs)
        self.type = "Great Sword"
        self.attack_power = 8
        self.attack_penalty = 4


class WarAxe(Weapon):
    def __init__(self, *args, **kwargs):
        super(WarAxe, self).__init__(*args, **kwargs)
        self.type = "War Axe"
        self.attack_power = 8
        self.attack_penalty = 3