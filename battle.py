from random import randint
from random import choice
from os import listdir
class enemyClass:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.race = {}
        self.health = 20
        self.level = 0
        self.dexterity = 1
        self.agility = 1
        self.vitality = 1
        self.awareness = 1
        self.charisma = 1
        self.intelligence = 1
        self.strength = 1
        self.traits = [""]
        self.profs = [""]
        self.drops = [""]
    def chooseSelf(self,spawnList,filePath,secCond = False,diffScale = False):
        self.rarity = randint(1,101)
        if diffScale != False:
         self.rarity = self.rarity * diffScale
        if self.rarity < 58: # 58%
            self.rarity = "common"
        elif self.rarity < 83: # 25%
            self.rarity = "uncommon"
        elif self.rarity < 93: # 10%
            self.rarity = "epic"  
        elif self.rarity < 98: # 5%
            self.rarity = "legendary"
        elif self.rarity < 100: # 2%
            self.rarity = "mythical"
        if secCond != False:
            if self.rarity == 101 and secCond == True: # 1% and a condition must be true
                self.rarity = "secret"
        enemyPath = f"{filePath}\\entities\\enemies\\{self.rarity}\\{choice(listdir('enemyPath'))}"
    def loadSelf(self):
        pass
        
    