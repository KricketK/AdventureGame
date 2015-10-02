__author__ = 'KRISTINE'


import random
from Weapon import *
from Character import *
from Special import *
from Item import *


def fight(character1, character2):
    character1.defend(character2.attack())

def rollClass(character_type, name):
    return character_type(name, health=random.randint(1, 15), defense=random.randint(1, 7))

begin = True
print("Welcome to the arena!")

print("Here is your opponent!")

Hickory = Alchemist('Hickory', 13, 8, 3, 'poison')
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
            user = Fighter(raw_input("What's your name?"), raw_input("Choose your weapon."))
            begin = False
        elif path == 2:
            print "I'm watching you, magic user."
            user = Wizard(raw_input("What's your name?"), raw_input("Choose your weapon."))
            begin = False
        elif path == 3:
            print "You're rather scrawny. Are you lost?"
            user = Scholar(raw_input("What's your name?"), raw_input("Choose your weapon."))
            begin = False
        elif 0 > path > 3:
            print "Oh a special snowflake, eh? \n"





#read up on types - stryder