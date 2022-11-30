from definitions import iClear # instant clear
from definitions import dClear
class PlayerClass: # has all of the stats for the player
    def __init__(self):
        self.name = ""
        self.race = {}
        self.health = 20
        self.level = 0
        self.xp = 0
        self.sparePoints = 0
        self.gold = 0
        self.dexterity = 1
        self.agility = 1
        self.vitality = 1
        self.awareness = 1
        self.charisma = 1
        self.intelligence = 1
        self.strength = 1
        self.traits = [""]
        self.profs = [""]
        self.storyLocation = [""]
        self.inventory = [""]
    def __str__(self): # allows printing of a data sheet
        return f"""
        Name: {self.name}
        Health: {self.health}
        Race: {self.race.get("name").capitalize()}
        Level: {self.level}
        XP: {self.xp}
        Gold: {self.gold}
        SP: {self.sparePoints}
        Dexterity: {self.dexterity}
        Agility: {self.agility}
        Vitality: {self.vitality}
        Awareness: {self.awareness}
        Charisma: {self.charisma}
        Intelligence: {self.intelligence}
        Strength: {self.strength}"""
    def statAssign(self):
        stats = ["dexterity","agility","vitality","awareness","charisma","intelligence","strength"] # list of stats
        try:
            navigate = int(input(f"""
            1.Dexterity - {self.dexterity}
            2.Agility - {self.agility}
            3.Vitality - {self.vitality}
            4.Awareness - {self.awareness}
            5.Charisma - {self.charisma}
            6.Intelligence - {self.intelligence}
            7.Strength - {self.strength}
            8.Exit
            You have {self.sparePoints} to spend.
            """)) - 1
            if navigate == 7:
                iClear()
                print(self)
                input("Input any key to continue\n>")
                return
            elif navigate < 0:
                raise ValueError
            global statUp
            statUp = stats[navigate]        
        except(ValueError,IndexError): # catches unexpected values
            print("Enter a number between 1-6")
            dClear()
            self.statAssign()
            return
        iClear()
        increment = input(f"""You have {self.sparePoints} points to spend.
How much would you like to increase {statUp} by?\n>""") # gets the variable for the stat that wants increasing
        try:
            increment = int(increment)
        except(ValueError):
            print("Enter an integer between 1-7")
        if increment > self.sparePoints:
            print(f"Not enough stat points! You have {self.sparePoints} points not {increment}")    
            self.statAssign()
        global newValue
        newValue = increment + self.__dict__[statUp]  
        loop = True
        while loop == True:
            confirm = str(input(f"Confirm you want to increase {statUp} from {self.__dict__[statUp]} to {newValue} (y/n)\n>")).lower()
            if confirm == "y":
                self.__dict__[statUp] = newValue
                self.sparePoints -= increment
                print(f"Increased {statUp} to {newValue}")
                del newValue
                dClear()
                loop = False
            elif confirm == "n":
                print("Changes aborted")
                dClear()
                self.statAssign()
            else:
                print("Invalid Input, please enter Y or N")
                dClear()
                loop = False
        self.statAssign()  
    def assignRace(self,davacis):
        races = ["human","elf","lizardman","dwarf"]
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
            case other:
                print("Unable to find race, please enter an integer between 1-4")
                dClear()
                self.assignRace()
                return 
        valid = False
        while not valid:
            confirm = input("Are you sure you want to choose this race? (y/n)\n>").lower()
            if confirm == "y":
                self.race = races[playerRace]
                for i in range(len(self.race["davacis"])):
                    self.__dict__[davacis[i]] += races[playerRace]["davacis"][i]
            elif confirm == "n":
                iClear()
                self.assignRace(races,davacis)
                return
            else:
                print("Invalid input")
                dClear()
        return self
    def makeSaveSlot(self,savesPath,saveSlot):
        import os
        saveSlot = str(input("What would you like to name the save slot? >")).strip().replace(' ', '_')
        if "\\" in saveSlot or "/" in saveSlot:
            print("Save slot cannot contain slashes")
            dClear()
            self.makeSaveSlot()
            return
        elif saveSlot == "":
            print("Slot name cannot be empty")
            dClear()
            self.makeSaveSlot()
            return
        try:
            os.mkdir(f"{savesPath}\\{saveSlot}")
        except(FileExistsError):
            if len(os.listdir(f"{savesPath}\\{saveSlot}")) == 0:
                logging.warning("Slot creation failed due to empty slot taking name.")
                navigate = str(input("Slot name is taken by an empty slot. Override? (y/n)\n>")).lower()
                if navigate == "y":
                    os.rmdir(saveSlot)
                else:
                    print("Invalid Input")
            logging.warning("Slot name taken.")
            override = str(input("Would you like to override the slot? (y/n)\n>")).lower()
            if override == "y":
                with open(f"{savesPath}\\{saveSlot}\\player.txt","w"):pass
            elif override == "n":
                iClear()
                self.makeSaveSlot(self,savesPath,saveSlot)
                return
                print("Returning to main menu")
            dClear()    
    def saveGame(self,saveSlot,savesPath):
        import os
        slotContent = os.listdir(f"{savesPath}/{saveSlot}")
        slotPath = f"{savesPath}/{saveSlot}"
        if "player.txt" in slotContent:
            print("Saving...")
            for attribute, value in self.__dict__.items():    
                with open(f"{slotPath}/player.txt","a") as f:
                    f.write(f"{attribute}={value}\n")
        else:
            f = open(f"{slotPath}/player.txt","x")
            f.close()
            self.saveGame(saveSlot,self,savesPath)
        dClear()    
    def loadFromDict(self,playerLoading):
        for key in playerLoading:
            setattr(self, key, playerLoading[key])
