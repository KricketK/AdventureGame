__author__ = 'KRISTINE'

import random

#Character basic needs
#class basic needs
    #HP, Attack, Defense, (Special Abilities, Character Description)
#classes: Fighter, Barbarian, Assassin, Wizard, Mage, Shaman, Alchemist


class Character(object):
    def __init__(self, name=raw_input("What is your name?"), health=10, attack=5, defense=5):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def fight(self, damage, inflict):
        self.damage = damage
            enemy_attack - self.defense
        self.inflict = inflict