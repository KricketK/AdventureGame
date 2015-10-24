__author__ = 'KRISTINE'

import random
from Weapon import *
from Character import *
from Special import *
from Item import *


def fight(character1, character2):
    character1.defend(character2.attack())


def rollclass(character_type, name):
    return character_type(name, health=random.randint(1, 15), defense=random.randint(1, 7))


begin = True
character = False

print("Welcome to the arena!")

while begin:
    path = raw_input('What path number do you choose? \n 1. Fighter \n 2. Wizard \n 3. Scholar')

    try:
        path = int(path)
    except ValueError:
        print "Try using the designating number. \n"

    else:

        if int(path) == 1:
            print "So you're a tough-guy, huh?"
            player = Fighter(raw_input("What's your name?"))
            begin = False
            character = True

        if int(path) == 2:
            print "I'm watching you, magic user."
            player = Wizard(raw_input("What's your name?"))
            begin = False
            character = True

        if int(path) == 3:
            print "You're rather scrawny. Are you lost?"
            player = Scholar(raw_input("What's your name?"))
            begin = False
            character = True

        if 0 > int(path) > 3:
            print "Oh a special snowflake, eh? \n"

print "Good luck, " + player.name + " the " + player.archetype + ". You will need it."

while character:
    print "You are proficient in: " + str(player.proficiencies)
    weapon_choice = raw_input("Pick your weapon:\n1. Sword\n2. Axe\n3. Knife\n4. Wand\n5. Staff\n6. Broomstick\n"
                              "7. Pen\n")
    try:
        weapon_choice = int(weapon_choice)
    except ValueError:
        print "You need a weapon before you may enter"

    if weapon_choice == 1:
        player.weapon = Sword()
    elif weapon_choice == 2:
        player.weapon = Axe()
    elif weapon_choice == 3:
        player.weapon = Knife()
    elif weapon_choice == 4:
        player.weapon = Wand()
    elif weapon_choice == 5:
        player.weapon = Staff()
    elif weapon_choice == 6:
        player.weapon = Broomstick()
    elif weapon_choice == 7:
        player.weapon = Pen()
    if 0 < weapon_choice < 8:
        print "You have chosen to carry a " + str(player.weapon) + " into battle."
        character = False
    elif 0 > weapon_choice > 7:
        print "You need a weapon before you may enter."

print raw_input("Now that you are outfitted, take stock of your abilities. To access your abilities type in 'Myself' "
                "at any time.")
print "Name: " + player.name
print "Class: " + player.archetype
print "Your health is, " + str(player.health)
print "Your attack power is " + str(player.power)
print "Your defense is " + str(player.defense)
print "Your weapon is a " + str(player.weapon)

print "hello friend"
