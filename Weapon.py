__author__ = 'KRISTINE'

import random


class Weapon(object):
    def __init__(self, written):
        self.written = written
        self.attack_power = 0
        self.attack_penalty = 0


class OpenHand(Weapon):
    def __init__(self, *args, **kwargs):
        super(OpenHand, self).__init__(*args, **kwargs)
        self.attack_power = -5
        self.attack_penalty = 0

    def __str__(self):
        return 'None'


class Club(Weapon):
    def __init__(self, *args, **kwargs):
        super(Club, self).__init__(*args, **kwargs)
        self.attack_power = 4
        self.attack_penalty = 0

    def __str__(self):
        return 'Club'


class Sword(Weapon):
    def __init__(self, *args, **kwargs):
        super(Sword, self).__init__(*args, **kwargs)
        self.attack_power = 5
        self.attack_penalty = 1

    def __str__(self):
        return 'Sword'


class Axe(Weapon):
    def __init__(self, *args, **kwargs):
        super(Axe, self).__init__(*args, **kwargs)
        self.attack_power = 4
        self.attack_penalty = 1

    def __str__(self):
        return 'Axe'


class Knife(Weapon):
    def __init__(self, *args, **kwargs):
        super(Knife, self).__init__(*args, **kwargs)
        self.attack_power = 3
        self.attack_penalty = 1

    def __str__(self):
        return 'Knife'


class Dart(Weapon):
    def __init__(self, *args, **kwargs):
        super(Dart, self).__init__(*args, **kwargs)
        self.attack_power = 2
        self.attack_penalty = 1

    def __str__(self):
        return 'Dart'


class Poison(Weapon):
    def __init__(self, *args, **kwargs):
        super(Poison, self).__init__(*args, **kwargs)
        self.attack_power = random.randint(1, 5)
        self.attack_penalty = 3

    def __str__(self):
        return 'Poison'


class Pen(Weapon):
    def __init__(self, *args, **kwargs):
        super(Pen, self).__init__(*args, **kwargs)
        self.attack_power = 1
        self.attack_penalty = 0

    def __str__(self):
        return 'Pen'


class Staff(Weapon):
    def __init__(self, *args, **kwargs):
        super(Staff, self).__init__(*args, **kwargs)
        self.attack_power = 3
        self.attack_penalty = 0

    def __str__(self):
        return 'Staff'


class Wand(Weapon):
    def __init__(self, *args, **kwargs):
        super(Wand, self).__init__(*args, **kwargs)
        self.attack_power = 2
        self.attack_penalty = 1

    def __str__(self):
        return 'Wand'


class Bombs(Weapon):
    def __init__(self, *args, **kwargs):
        super(Bombs, self).__init__(*args, **kwargs)
        self.attack_power = 7
        self.attack_penalty = 4

    def __str__(self):
        return 'Bombs'


class Elixirs(Weapon):
    def __init__(self, *args, **kwargs):
        super(Elixirs, self).__init__(*args, **kwargs)
        self.attack_power = 4
        self.attack_penalty = 2

    def __str__(self):
        return 'Elixirs'


class Hyde(Weapon):
    def __init__(self, *args, **kwargs):
        super(Hyde, self).__init__(*args, **kwargs)
        self.attack_power = 7
        self.attack_penalty = 4

    def __str__(self):
        return 'Hyde'


class Familiar(Weapon):
    def __init__(self, *args, **kwargs):
        super(Familiar, self).__init__(*args, **kwargs)
        self.attack_power = 7
        self.attack_penalty = 3

    def __str__(self):
        return 'Familiar'


class Broomstick(Weapon):
    def __init__(self, *args, **kwargs):
        super(Broomstick, self).__init__(*args, **kwargs)
        self.attack_power = 3
        self.attack_penalty = 1

    def __str__(self):
        return 'Broomstick'


class GreatSword(Weapon):
    def __init__(self, *args, **kwargs):
        super(GreatSword, self).__init__(*args, **kwargs)
        self.attack_power = 8
        self.attack_penalty = 4

    def __str__(self):
        return 'Great Sword'


class WarAxe(Weapon):
    def __init__(self, *args, **kwargs):
        super(WarAxe, self).__init__(*args, **kwargs)
        self.attack_power = 8
        self.attack_penalty = 3

    def __str__(self):
        return 'War Axe'
