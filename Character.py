__author__ = 'KRISTINE'


import random
from Weapon import *
from Special import *


class Character(object):

    def __init__(self, name, weapon=Weapon(), health=15, power=10, defense=10):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.power = power
        self.defense = defense
        self.proficiencies = []

    def __str__(self):
        return "My name is " + self.name + ". Prepare yourself."

    def attack(self):
        if self.weapon in self.proficiencies:
            hit_strength = self.weapon.attack_power + self.power
        else:
            hit_strength = self.weapon.attack_penalty + self.power
            if hit_strength < 0:
                hit_strength = 0
        return hit_strength

    def defend(self, attackpwr):
        if attackpwr > self.defense:
            damage = attackpwr - self.defense
            self.health -= damage
        else:
            damage = 0
            self.health = self.health
        return damage



class Wizard(Character):
    def __init__(self, *args, **kwargs):
        super(Wizard, self).__init__(*args, **kwargs)
        self.health = 15 + random.randint(3, 4)
        self.power = 10 + random.randint(-1, 3)
        self.defense = 10 + random.randint(-2, 3)
        self.archetype = "Wizard"
        self.proficiencies = ['Wand', 'Staff', 'Broomstick']
        self.special = Pureblood()

    def apply(self):
        self.health += self.special.healbonus
        return self.health


class Mage(Wizard):
    def __init__(self, *args, **kwargs):
        super(Mage, self).__init__(*args, **kwargs)
        self.archetype = "Mage"
        self.proficiencies.append('Sword')


class Shaman(Wizard):
    def __init__(self, *args, **kwargs):
        super(Shaman, self).__init__(*args, **kwargs)
        self.archetype = "Shaman"
        self.proficiencies.extend(['Familiar', 'Knife'])
        self.proficiencies.remove('Broomstick')


class Fighter(Character):
    def __init__(self, *args, **kwargs):
        super(Fighter, self).__init__(*args, **kwargs)
        self.health = 15 + random.randint(-2, 2)
        self.power = 10 + random.randint(1, 4)
        self.defense = 10 + random.randint(1, 4)
        self.archetype = "Fighter"
        self.proficiencies = ['Sword', 'Axe', 'Knife']
        self.special = Thickskin()

    def apply(self):
        self.defense += self.special.defbonus
        return self.defense


class Barbarian(Fighter):
    def __init__(self, *args, **kwargs):
        super(Barbarian, self).__init__(*args, **kwargs)
        self.archetype = "Barbarian"
        self.proficiencies.extend(['Club', 'WarAxe'])


class Assassin(Fighter):
    def __init__(self, *args, **kwargs):
        super(Assassin, self).__init__(*args, **kwargs)
        self.archetype = "Assassin"
        self.proficiencies.extend(['Dart', 'Poison'])
        self.proficiencies.remove('Axe')


class Scholar(Character):
    def __init__(self, *args, **kwargs):
        super(Scholar, self).__init__(*args, **kwargs)
        self.health = 15 + random.randint(-1, 3)
        self.power = 10 + random.randint(-1, 3)
        self.defense = 10 + random.randint(-1, 3)
        self.archetype = "Scholar"
        self.proficiencies = ['Knife', 'Pen']
        self.special = Cunning()

    def apply(self):
        self.power += self.special.attbonus
        return self.power


class Alchemist(Scholar):
    def __init__(self, *args, **kwargs):
        super(Alchemist, self).__init__(*args, **kwargs)
        self.archetype = "Alchemist"
        self.proficiencies.extend(['Bombs', 'Elixirs', 'Poison', 'Hyde'])
