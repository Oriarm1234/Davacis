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
    def loadFromDict(self,playerLoading):
        for key in playerLoading:
            setattr(self, key, playerLoading[key])