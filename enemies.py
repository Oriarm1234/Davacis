class TestEnemy:
    def __init__(self):
        from definitions import races
        self.name = "TestEnemy"
        self.race = races["human"]
        self.level = 6
        self.dexterity = 1
        self.agility = 1
        self.vitality = 1
        self.awareness = 1
        self.charisma = 1
        self.intelligence = 1
        self.strength = 1
        self.traits = [""]
        self.profs = [""]
#        self.weapon = defines["weapons"]["ExampleWeapon"]
        self.health = (10 + (self.vitality * 1.5))
        self.initiative = (0.5 + (self.dexterity * 0.2))
        self.attack = ()
    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False
    def generateStats(self):
        pass
        