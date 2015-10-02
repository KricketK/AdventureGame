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
character = True
print("Welcome to the arena!")

print("Here is your opponent!")

Hickory = Alchemist('Hickory', 'Poison', 13, 8, 3)
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
            user = Fighter(raw_input("What's your name?"), raw_input("Pick your weapon: 1. Sword \n 2. Axe \n 3. Knife"
                                                " \n 4. Club \n 5. Dart \n 6. Poison \n""7. WarAxe \n 8. GreatSword"))

            try:
                user.weapon = int(user.weapon)
            except ValueError:
                    print "You need a weapon before you may enter."
            if user.weapon == 1:
                user.weapon = Sword
            elif user.weapon == 2:
                user.weapon = Axe
            elif user.weapon == 3:
                user.weapon = Knife
            elif user.weapon == 4:
                user.weapon = Club
            elif user.weapon == 5:
                user.weapon = Dart
            elif user.weapon == 6:
                user.weapon = Poison
            elif user.weapon == 7:
                user.weapon = WarAxe
            elif user.weapon == 8:
                user.weapon = GreatSword
            elif 0 > user.weapon > 8:
                character = False
                print "You need a weapon before you may enter."
            if character:
                begin = False

        elif path == 2:
            print "I'm watching you, magic user."
            user = Wizard(raw_input("What's your name?"), raw_input("Pick your weapon: 1. Wand \n 2. Staff \n "
                                                        "3. Broomstick \n 4. Sword \n 5. Familiar \n 6. Knife"))
        if user.weapon == 1:
            user.weapon = Wand
        elif user.weapon == 2:
            user.weapon = Staff
        elif user.weapon == 3:
            user.weapon = Broomstick
        elif user.weapon == 4:
            user.weapon = Sword
        elif user.weapon == 5:
            user.weapon = Familiar
        elif user.weapon == 6:
            user.weapon = Knife
        elif 0 > user.weapon > 6:
            character = False
            print "You need a weapon before you may enter."
        if character:
            begin = False

        elif path == 3:
            print "You're rather scrawny. Are you lost?"
            user = Scholar(raw_input("What's your name?"), raw_input("Pick your weapon: 1. Knife \n 2. Pen \n "
                                                            "3. Bombs \n 4. Elixirs \n 5. Poison \n 6. Hyde"))
        try:
            user.weapon = int(user.weapon)
        except ValueError:
            print "You need a weapon before you may enter."
        if user.weapon == 1:
            user.weapon = Knife
        elif user.weapon == 2:
            user.weapon = Pen
        elif user.weapon == 3:
            user.weapon = Bombs
        elif user.weapon == 4:
            user.weapon = Elixirs
        elif user.weapon == 5:
            user.weapon = Poison
        elif user.weapon == 6:
            user.weapon = Hyde
        elif 0 > user.weapon > 6:
            character = False
            print "You need a weapon before you may enter."
        if character:
            begin = False

        elif 0 > path > 3:
            print "Oh a special snowflake, eh? \n"





#read up on types - stryder