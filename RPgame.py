__author__ = 'KRISTINE'

import random
from Weapon import *
from Character import *
from Special import *
from Item import *


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

maxhealth = player.health

print raw_input("Now that you are outfitted, take stock of your abilities. To access your abilities type in 'Myself' "
                "at any time.")
print "Name: " + player.name
print "Class: " + player.archetype
print "Your health is, " + str(player.health)
print "Your attack power is " + str(player.power)
print "Your defense is " + str(player.defense)
print "Your weapon is a " + str(player.weapon) + "\n"

raw_input("Are you ready? \n")


opponent1 = Barbarian("Hux", health=8, power=5, defense=5)
opponent1.weapon = pickweapon()

print "Opponent: " + opponent1.name
print "Class: " + opponent1.archetype
print opponent1.name + "'s health is, " + str(opponent1.health)
print opponent1.name + "'s attack power is " + str(opponent1.power)
print opponent1.name + "'s defense is " + str(opponent1.defense)
print opponent1.name + "'s weapon is a " + str(opponent1.weapon) + "\n"

raw_input("Let the battle begin!")

Fight = True


def playerattack(user, enemy):
    userhit = user.attack()
    enemydamage = enemy.defend(userhit)
    return enemydamage


def enemyattack(user, enemy):
    enemyhit = enemy.attack()
    userdamage = user.defend(enemyhit)
    return userdamage

while Fight:

    player.health = maxhealth

    if player.health > 0:
        givedamage = playerattack(player, opponent1)
        raw_input(player.name + " deals " + str(givedamage) + " against " + opponent1.name + ". " + opponent1.name +
               "'s health is now " + str(opponent1.health))

    if opponent1.health > 0:
        takedamage = enemyattack(player, opponent1)
        raw_input(opponent1.name + " deals " + str(takedamage) + " against " + player.name + ". " + player.name +
               "'s health is now " + str(player.health))

    if player.health <= 0:
        Fight = False
        print "Oh dear. Lost another newbie. Sorry, friend."

    if opponent1.health <= 0:
        Fight = False
        raw_input("Hah. You made it. I'm a mite surprised. Onto the next round with you!")



print "hello friend"
