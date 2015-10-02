__author__ = 'KRISTINE'


import random
from Weapon import *
from Special import *

class Character(object):

    def __init__(self, name, weapon, health=15, power=10, defense=10, special=Special()):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.power = power
        self.defense = defense
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
        self.proficiencies = ['Wand', 'Staff', 'Broomstick']
        self.special = Pureblood
        self.weapon = raw_input("Pick your weapon: 1. Wand \n 2. Staff \n 3. Broomstick \n 4. Sword \n 5. Familiar"
                                " \n 6. Knife")
        if self.weapon == 1:
            self.weapon = Wand
        elif self.weapon == 2:
            self.weapon = Staff
        elif self.weapon == 3:
            self.weapon = Broomstick
        elif self.weapon == 4:
            self.weapon = Sword
        elif self.weapon == 5:
            self.weapon = Familiar
        elif self.weapon == 6:
            self.weapon = Knife


class Mage(Wizard):
    def __init__(self, *args, **kwargs):
        super(Mage, self).__init__(*args, **kwargs)
        self.proficiencies.append('Sword')


class Shaman(Wizard):
    def __init__(self, *args, **kwargs):
        super(Shaman, self).__init__(*args, **kwargs)
        self.proficiencies.extend(['Familiar', 'Knife'])
        self.proficiencies.remove('Broomstick')

class Fighter(Character):
    def __init__(self, *args, **kwargs):
        super(Fighter, self).__init__(*args, **kwargs)
        self.health = 15 + random.randint(-2, 2)
        self.attack = 10 + random.randint(1, 4)
        self.defense = 10 + random.randint(1, 4)
        self.proficiencies = ['Sword', 'Axe', 'Knife']
        self.special = Thickskin
        self.weapon = raw_input("Pick your weapon: 1. Sword \n 2. Axe \n 3. Knife \n 4. Club \n 5. Dart \n 6. Poison \n"
                                "7. WarAxe \n 8. GreatSword")
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
        elif self.weapon == 7:
            self.weapon = WarAxe
        elif self.weapon == 8
            self.weapon = GreatSword


class Barbarian(Fighter):
    def __init__(self, *args, **kwargs):
        super(Barbarian, self).__init__(*args, **kwargs)
        self.proficiencies.extend(['Club', 'WarAxe'])


class Assassin(Fighter):
    def __init__(self, *args, **kwargs):
        super(Assassin, self).__init__(*args, **kwargs)
        self.proficiencies.extend(['Dart', 'Poison'])
        self.proficiencies.remove('Axe')


class Scholar(Character):
    def __init__(self, *args, **kwargs):
        super(Scholar,self).__init__(*args, **kwargs)
        self.health = 15 + random.randint(-3, 3)
        self.attack = 10 + random.randint(-3, 3)
        self.defense = 10 + random.randint(-3,3)
        self.proficiencies = ['Knife', 'Pen']
        self.special = Cunning
        self.weapon = raw_input("Pick your weapon: 1. Knife \n 2. Pen \n 3. Bombs \n 4. Elixirs \n 5. Poison \n "
                                "6. Hyde")
        try:
            self.weapon = int(self.weapon)
        except ValueError:
            print "You need a weapon before you may enter."
        if self.weapon == 1:
            self.weapon = Knife
        elif self.weapon == 2:
            self.weapon = Pen
        elif self.weapon == 3:
            self.weapon = Bombs
        elif self.weapon == 4:
            self.weapon = Elixirs
        elif self.weapon == 5:
            self.weapon = Poison
        elif self.weapon == 6:
            self.weapon = Hyde
        elif 0 > self.weapon > 6:
            print "You need a weapon before you may enter."

class Alchemist(Scholar):
    def __init__(self, *args, **kwargs):
        super(Alchemist, self).__init__(*args, **kwargs)
        self.proficiencies.extend(['Bombs', 'Elixirs', 'Poison', 'Hyde'])