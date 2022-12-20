from definitions import *
import os
import logging
from loggingConfig import initLogger
from ast import literal_eval
initLogger(filePath)
class PlayerClass: # has all of the stats for the player
    def __init__(self, 
                 name="", 
                 race={},
                 health=20,
                 level=0,
                 xp=0,
                 sparePoints=0,
                 gold=0,
                 stats={"dexterity":1,
                        "agility":1,
                        "vitality":1,
                        "awareness":1,
                        "charisma":1,
                        "intelligence":1,
                        "strength":1},
                 traits = [],
                 profs = [],
                 storyLocation = [],
                 inventory = []
                 ):

        self.name = name
        self.race = race
        self.health = health
        self.level = level
        self.xp = xp
        self.sparePoints = sparePoints
        self.gold = gold
        self.stats = stats
        self.traits = traits
        self.profs = profs
        self.storyLocation = storyLocation
        self.inventory = inventory
    def __str__(self): # allows printing of a data sheet
        bs = "\n\t\t"
        return f"""
\t\tName: {self.name}
\t\tHealth: {self.health}
\t\tRace: {self.race['name'].capitalize()}
\t\tLevel: {self.level}
\t\tXP: {self.xp}
\t\tGold: {self.gold}
\t\tSP: {self.sparePoints}
\t\t{bs.join((statName + ": " + str(self.stats[statName])) for statName in self.stats)}"""
    def statAssign(self):
        bs = "\n\t\t"
        enumeratedStatNames = enumerate(list(self.stats.keys()))
        StatValues = list(self.stats.values())
        navigate = sanInput(f"""\t\t--Choose a stat--
\t\t{bs.join((f"{ind+1}. "+statName.capitalize()+ " - " + str(self.stats[statName])) for ind,statName in enumeratedStatNames)}
\t\t8.Exit
\t\tYou have {self.sparePoints} to spend.
\t\t> """, int, 1, 8, Clear=True) - 1
        if navigate == 7:
            clear("i")
            print(self)
            input("\t\tPress enter to continue")
            return
        statUp = list(self.stats.keys())[navigate]        
        clear("i")
        increment = sanInput(f"""
\t\tYou have {self.sparePoints} points to spend.
\t\tHow much would you like to increase {statUp.capitalize()} by?\n\t\t> """, int, 0, self.sparePoints, Clear=True) # gets the variable for the stat that wants increasing
        newValue = increment + self.stats[statUp]  
        confirm = sanInput(f"\t\tConfirm you want to increase {statUp} from {self.stats[statUp]} to {newValue} (y/n)\n\t\t> ", str, values=["y","n"],Clear=True)
        if confirm == "y":
            self.stats[statUp] = newValue
            self.sparePoints -= increment
            print(f"\t\tIncreased {statUp} to {newValue}")
            clear("d")
        elif confirm == "n":
            print("\t\tChanges aborted")
            clear("d")
        return self.statAssign()
    def assignRace(self,davacis,racesDict):
        races = ["human","elf","lizardman","dwarf"]
        raceRaw = sanInput("""
\t\tWhat race are you?
\t\t1.Human
\t\t2.Elf
\t\t3.Lizardman
\t\t4.Dwarf
\t\t> """, int, 1, 4, Clear=True)
        match raceRaw:
            case 1:
                print("""
\t\t--------Human--------
\t\t-----Stat Changes----
\t\tIntelligence + 2
\t\tStarting Gold + 10
\t\t-Intrinsic Abilities-
\t\tAdaptive Mind - 15% more XP gain
\t\t----Proficiencies----
\t\tAdaptable
\t\tTactics
\t\tAmbitous""")
            case 2:
                print("""
\t\t---------Elf---------
\t\t-----Stat Changes----
\t\tAgility + 2
\t\tDexterity + 2
\t\tAwareness + 1
\t\tStrength - 2
\t\t-Intrinsic Abilities-
\t\tSharp Vision - +2 to perception checks
\t\tDarkvision - Unimpeded by darkness
\t\t----Proficiencies---
\t\tArchery
\t\tLight Armour
\t\tForaging""") 
            case 3:
                print("""
\t\t------Lizardman------
\t\t-----Stat Changes----
\t\tBase Health + 3
\t\tDexterity + 1
\t\tIntelligence - 1
\t\tDisadvantage in Dry Biomes
\t\t-Intrinsic Abilities-
\t\tScales - +2 defence against 'sharp' attacks
\t\t-----Proficiencies----
\t\tSpears""")            
            case 4:
                print("""
\t\t--------Dwarf---------
\t\t-----Stat Changes-----
\t\tStrength + 2
\t\tAwareness + 1
\t\tSpeed - 1
\t\t-Intrinsic Abilities--
\t\tDarkvision - Unimpeded by darkness
\t\t-----Proficiencies----
\t\tHeavy Armour
\t\tBlunt""")
        raceRaw = raceRaw - 1
        self.race = racesDict[f"{races[raceRaw]}"]
        self.raceDavacisLoad()
    def raceDavacisLoad(self):
        confirm = sanInput("\t\tAre you sure you want to choose this race? (y/n)\n\t\t>", str, values=["y", "n"])
        if confirm == "y":
            davacisList = self.race["davacis"]
            for i in range(len(davacisList)):
                self.stats[davacis[i]] += davacisList[i]
        elif confirm == "n":
            clear("i")
            self.assignRace(davacis,racesDict)
            return
    def makeSaveSlot(self,savePath):
        saveSlot = input("\t\tWhat would you like to name the save slot?\n\t\t> ").strip().replace(' ', '_')
        if "\\" in saveSlot or "/" in saveSlot:
            print("\t\tSave slot cannot contain slashes")
            clear("d")
            self.makeSaveSlot(savePath)
            return
        elif saveSlot == "":
            print("\t\tSlot name cannot be empty")
            clear("d")
            self.makeSaveSlot(savePath)
            return
        slotPath = f"{savePath}\\{saveSlot}"
        try:
            os.mkdir(f"{slotPath}")
        except(FileExistsError):

            if len(os.listdir(f"{slotPath}")) == 0:
                logging.warning("Slot creation failed due to empty slot taking name.")
                navigate = sanInput("Slot name is taken by an (appearingly) empty slot. Override? (y/n)\n> ",str,values=["y","n"], Clear=True)
                if navigate == "y":
                    os.rmdir(slotPath)
                elif navigate == "n":
                    print("Returning to start of slot naming.")
                    return self.makeSaveSlot(savePath)
                    

            logging.warning("Slot name taken.")
            override = sanInput("Would you like to override the slot? (y/n)\n> ", str, values=["y","n"], Clear=True)
            if override == "y":
                with open(f"{savePath}\\{saveSlot}\\player.txt","w"):pass
            elif override == "n":
                clear("i")
                self.makeSaveSlot(savePath)
                print("Returning to main menu")
                return
            clear("d")    
        return slotPath
    def newGame(self,savePath):
        clear("i")
        self.nameSelf()
        self.assignRace(davacis,racesDict)
        self.statAssign()
        slotPath = self.makeSaveSlot(savePath)
        self.saveGame(slotPath)
    def saveGame(self,slotPath):
        slotContent = os.listdir(f"{slotPath}")
        quote = '\''
        if "player.txt" in slotContent:
            print("Saving...")
            for attribute, value in self.__dict__.items():    
                with open(f"{slotPath}/player.txt","a") as f:
                    f.write(f"{attribute}={(value if (not type(value) == str) else (quote + value + quote))}\n")
        else:
            with open(f"{slotPath}/player.txt","x") as f:
                self.saveGame(slotPath)
        clear("d")    
    def loadGame(self,savePath):
            slots = os.listdir(savePath)
            message = "\t\tWhat slot would you like to load?\n"
            for i in range(len(slots)):
                message+=f"\t\t{i + 1}.{slots[i]}\n"
            message+=f"\t\t{len(slots) + 1}.Exit\n> "
            choice = sanInput(message, int, 1, len(slots) + 1, Clear=True)
            if choice == len(slots) + 1:
                return "CONTINUE"

            saveSlot = slots[choice-1]
            slotPath = f"{savePath}/{saveSlot}"
            if len(os.listdir(f"{slotPath}")) == 0:
                logging.warning(f"\t\t{saveSlot} appears empty, this indicates a broken save.")
                delete = sanInput("\t\tWould you like to delete the file? (y/n)\n> ", str, values=["y", "n"],Clear=True)
                if delete == "y":
                    os.rmdir(slotPath)
                    logging.debug(f"{saveSlot} deleted")
                else:
                    clear("d")
                    self.loadGame(savePath)
                    return

            with open(f"{slotPath}/player.txt") as f:    
                lines = f.read().split("\n")
                for lineNum in range(len(lines)):
                    content = lines[lineNum].split("=")
                    key = content[0];value = content[1] if len(content) >= 2 else None
                    if key.replace(" ","") != "":
                        setattr(self, key, literal_eval(value))
                bs = "\n"
                navigate = sanInput(f"{self}\n\t\tIs this the correct file?(y/n)\n\t\t> ",str, values=["y", "n"], Clear=True)
                if navigate == "n":
                    print("Returning to slot selection...")
                    clear("d")
                    self.loadGame(savePath)

                return
    def nameSelf(self):
        self.name = input("\t\tWhat is your name?\n\t\t> ")