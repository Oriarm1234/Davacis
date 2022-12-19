from random import randint
from random import choice
from os import listdir
import json
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
    def __str__(self):
        return f"""
        Name: {self.name}
        Health: {self.health}
        Level: {self.level}
        Dexterity: {self.dexterity}
        Agility: {self.agility}
        Vitality: {self.vitality}
        Awareness: {self.awareness}
        Charisma: {self.charisma}
        Intelligence: {self.intelligence}
        Strength: {self.strength}"""
    def chooseSelf(self,spawnList,filePath,secretCond = False,diffScale = False):
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
        if secretCond != False:
            if self.rarity == 101 and secretCond == True: # 1% and a condition must be true
                self.rarity = "secret"
        with open(f"{filePath}\\entities\\enemies\\{self.rarity}\\{choice(listdir(''))}") as f: # choice needs finishing
            entityLoading = json.loads(f.read())
            for key in entityLoading:
                setattr(self, key, entityLoading[key])
enemy = enemyClass()
print(enemy)
    