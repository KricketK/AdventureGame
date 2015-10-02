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

    def __init__(self, name, special, health=10, power=5, defense=5, weapon=Weapon()):
        self.weapon = weapon
        self.name = name
        self.special = special
        self.health = health
        self.power = power
        self.defense = defense
        self.weapon = weapon
        self.proficiencies = []

    def __str__(self):
        return "My name is " + self.name + "Prepare yourself."

    def add(self, stat, other):
        print(str(stat) + " increased by " + str(other))
        self.stat += other

    def reduce(self, stat, other):
        print(str(stat) + " decreased by " + str(other))
        self.stat -= other

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
        self.proficiencies = ['wand', 'staff', 'broomstick']


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
        self.proficiencies = ['sword', 'axe', 'knife']


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
        self.proficiencies = ['knife', 'pen']
        self.special = self.damage + random.randint(1, 3)


class Alchemist(Scholar):
    def __init__(self, *args, **kwargs):
        super(Alchemist, self).__init__(*args, **kwargs)
        self.proficiencies.extend(['bombs', 'elixirs', 'poison', 'hyde'])
        self.special = self.damage

def rollClass(character_type, name):
    return character_type(name, health=random.randint(1, 15), defense=random.randint(1, 7))

begin = True
print("Welcome to the arena!")

print("Here is your opponent!")

Hickory = Barbarian('Hickory', 13, 8, 3, 'poison')
print Hickory

while begin:
    path = raw_input('What path number do you choose? \n 1. Fighter \n 2. Wizard \n 3. Scholar')
    try:
        path = int(path)
    except ValueError:
        print("Choose the number associated with the path.")
    else:
        if path == 1:
            print "So you're a tough-guy, huh?"
            begin = False
        elif path == 2:
            print "I'm watching you, magic user."
            begin = False
        elif path == 3:
            print "Are you lost?"
            begin = False
        elif path > 3:
            print "Oh a special snowflake, eh? \n"


#read up on types - stryder