__author__ = 'KRISTINE'


import random
from Weapon import *
from Special import *

class Character(object):

    def __init__(self, name, health=15, power=10, defense=10, weapon=Weapon(), special=Special()):
        self.weapon = weapon
        self.name = name
        self.health = health
        self.power = power
        self.defense = defense
        self.weapon = ()
        self.proficiencies = []
        self.special = special

    def __str__(self):
        return "My name is " + self.name + ". Prepare yourself."

    def attack(self):
        hit_strength = random.randint(1, self.power)
        if self.weapon in self.proficiencies:
            hit_strength += self.weapon.attack_power
        else:
            hit_strength -= self.weapon.attack_penalty
            if hit_strength < 0:
                hit_strength = 0
        return hit_strength

    def defend(self, attackpwr):
        if attackpwr > self.defense:
            self.health -= attackpwr - self.defense


class Wizard(Character):
    def __init__(self, *args, **kwargs):
        super(Wizard, self).__init__(*args, **kwargs)
        self.health = 15 + random.randint(3, 4)
        self.attack = 10 + random.randint(-1, 3)
        self.defense = 10 + random.randint(-1, 3)
        self.proficiencies = ['wand', 'staff', 'broomstick']
        self.special = Pureblood


class Mage(Wizard):
    def __init__(self, *args, **kwargs):
        super(Mage, self).__init__(*args, **kwargs)
        self.proficiencies.append('sword')


class Shaman(Wizard):
    def __init__(self, *args, **kwargs):
        super(Shaman, self).__init__(*args, **kwargs)
        self.proficiencies.extend(['familiar', 'knife'])
        self.proficiencies.remove('broomstick')

class Fighter(Character):
    def __init__(self, *args, **kwargs):
        super(Fighter, self).__init__(*args, **kwargs)
        self.health = 15 + random.randint(-2, 2)
        self.attack = 10 + random.randint(1, 4)
        self.defense = 10 + random.randint(1, 4)
        self.proficiencies = ['sword', 'axe', 'knife']
        self.special = Thickskin
        self.weapon = raw_input("Pick your weapon: 1. Sword \n 2. Axe \n 3. Knife \n 4. Club \n 5. Dart \n 6. Poison")
        if self.weapon == 1:
            self.weapon = Sword
        elif self.weapon == 2:
            self.weapon = Axe
        elif self.weapon == 3:
            self.weapon = Knife
        elif self.weapon == 4:
            self.weapon = Club
        elif self.weapon == 5:
            self.weapon = Dart
        elif self.weapon == 6:
            self.weapon = Poison


class Barbarian(Fighter):
    def __init__(self, *args, **kwargs):
        super(Barbarian, self).__init__(*args, **kwargs)
        self.proficiencies.append('club')


class Assassin(Fighter):
    def __init__(self, *args, **kwargs):
        super(Assassin, self).__init__(*args, **kwargs)
        self.proficiencies.extend(['dart', 'poison'])
        self.proficiencies.remove('axe')


class Scholar(Character):
    def __init__(self, *args, **kwargs):
        super(Scholar,self).__init__(*args, **kwargs)
        self.health = 15 + random.randint(-3, 3)
        self.attack = 10 + random.randint(-3, 3)
        self.defense = 10 + random.randint(-3,3)
        self.proficiencies = ['knife', 'pen']
        self.special = Cunning


class Alchemist(Scholar):
    def __init__(self, *args, **kwargs):
        super(Alchemist, self).__init__(*args, **kwargs)
        self.proficiencies.extend(['bombs', 'elixirs', 'poison', 'hyde'])
        self.special = Cunning