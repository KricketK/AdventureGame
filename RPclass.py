__author__ = 'KRISTINE'

import random

#Character basic needs
#class basic needs
    #HP, Attack, Defense, (Special Abilities, Character Description)
#classes: Fighter, Barbarian, Assassin, Wizard, Mage, Shaman, Alchemist

def fight(character1, character2):
    character1.defend(character2.attack())



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

class Character(object):

    def __init__(self, name, health=10, power=5, defense=5, weapon=Weapon()):
        self.weapon = weapon
        self.name = name
        self.health = health
        self.power = power
        self.defense = defense
        self.weapon = weapon
        self.proficiencies = []

    def __str__(self):
        return "My name is " + self.name

    def add(self, other):
        print("Health increased by " + str(other))
        self.health += other

    def attack(self):
        hit_strength = random.randint(1, self.power)
        if self.weapon in self.proficiencies:
            hit_strength += self.weapon.attack_power
        else:
            hit_strength -= self.weapon.attack_penalty
            if hit_strength < 0:
                hit_strength = 0
        #do a check to make sure I'm not returning a negative number...
        return hit_strength

    def defend(self, attackpwr):
        if attackpwr > self.defense:
            self.health -= attackpwr - self.defense


class Wizard(Character):
    def __init__(self, *args, **kwargs):
        super(Wizard, self).__init__(*args, **kwargs)
        self.proficiencies = ['wand', 'staff', 'broomstick']


class Mage(Wizard):
    def __init__(self, *args, **kwargs):
        super(Mage, self).__init__(*args, **kwargs)
        self.proficiencies = ['wand', 'staff', 'broomstick', 'sword']


class Fighter(Character):
    def __init__(self, *args, **kwargs):
        super(Fighter, self).__init__(*args, **kwargs)
        self.proficiencies = ['sword', 'axe', 'knife']


class Barbarian(Fighter):
    def __init__(self, *args, **kwargs):
        super(Barbarian, self).__init__(*args, **kwargs)
        self.proficiencies.append('club')

def rollClass(character_type, name):
    return character_type(name, health=random.randint(1, 15), defense=random.randint(1, 7))

print("Welcome to the arena!")

print("Here is your opponent!")

Hickory = Mage('Hickory', 13, 8, 3, 'sword')




#read up on types - stryder