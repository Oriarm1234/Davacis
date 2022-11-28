from stats import PlayerClass
from definitions import dClear
from definitions import iClear
def raceSelect(races,davacis):
    player = PlayerClass()
    player.name = str(input("What is your name? >"))
    if player.name == "":
        print("Please enter a name.")
        raceSelect(races,davacis)
    iClear()
    playerRace = str(input("""
What race are you?
    1.Human
    2.Elf
    3.Lizardman
    4.Dwarf
    >"""))
    match playerRace:
        case "1":
            print("""
--------Human--------
-----Stat Changes----
 Intelligence + 2
 Starting Gold + 10
-Intrinsic Abilities-
 Adaptive Mind - 15% more XP gain
----Proficiencies----
 Adaptable
 Tactics
 Ambitous""")
            playerRace = "human"
        case "2":
            print("""
---------Elf---------
-----Stat Changes----
 Agility + 2
 Dexterity + 2
 Awareness + 1
 Strength - 2
-Intrinsic Abilities-
 Sharp Vision - +2 to perception checks
 Darkvision - Unimpeded by darkness
 ----Proficiencies---
  Archery
  Light Armour
  Foraging""") 
            playerRace = "elf"
        case "3":
            print("""
------Lizardman------
-----Stat Changes----
 Base Health + 3
 Dexterity + 1
 Intelligence - 1
 Disadvantage in Dry Biomes
-Intrinsic Abilities-
 Scales - +2 defence against 'sharp' attacks
-----Proficiencies----
 Spears""")            
            playerRace = "lizardman"
        case "4":
            print("""
--------Dwarf---------
-----Stat Changes-----
 Strength + 2
 Awareness + 1
 Speed - 1
-Intrinsic Abilities--
 Darkvision - Unimpeded by darkness
-----Proficiencies----
 Heavy Armour
 Blunt""")
            playerRace = "dwarf"
        case other:
            print("Unable to find race, please enter an integer between 1-4")
            dClear()
            raceSelect(races,davacis)
            return 
    confirm = input("Are you sure you want to choose this race? (y/n)\n>").lower()
    if confirm == "y":
        player.race = races[playerRace]
        for i in range(len(player.race["davacis"])):
            player.__dict__[davacis[i]] += races[playerRace]["davacis"][i]
    elif confirm == "n":
        iClear()
        raceSelect(races,davacis)
    else:
        print("Invalid input, returning to start of creation.")
        dClear()
        raceSelect(races,davacis)
    return player