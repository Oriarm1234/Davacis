import os
import logging
from definitions import dClear
from definitions import davacis 
def openItemDesigner(filePath):
    Valid = False
    weapon = {}
    itemPath = f"{filePath}/items"
    itemName = str(input("What do you want to call the item?\n>"))
    weapon.update("damage",chooseWeaponDamage(chooseItemType()))
    weapon.update("rarity",chooseItemRarity())
    weapon.update("statReqs",chooseStatReqs(davacis))
    weapon.update("value",chooseWeaponValue())
    weapon.update("allowTraits",chooseTraitAllow())    
    weapon.update("isUnique",chooseWeaponUnique())
    print(weapon)
def chooseItemType():
    types = ["weapons","armour","misc"]
    try:
        type = types[int(input("""
        What type of item do you want to make?
            1. Weapon
            2. Armour
            3. Misc\n>""")) - 1]
    except(TypeError,IndexError):
        invalidInput()
        chooseItemType()
        return
    return type
def chooseWeaponTypes():
    types = ["crush","slash","pierce","magic","projectile","etherial"]
    Finished = False
    while not Finished:
        try:
            weaponType = int(input("""
            What damage types should the weapon do?
            1. Crush
            2. Slash
            3. Pierce
            4. Magic
            5. Projectile
            6. Etherial
            7. Go Back
            """))
            if weaponType > 7 or weaponType < 1:
                raise IndexError
        except(TypeError,IndexError):
            print("Invalid Input")
            dClear()
            chooseItemType()
            return
        if weaponType == "7":
            Finished = True
            break
        finish = str(input("Do you want to add more damage types?\n1. Yes\n 2. No\n>"))
        if finish == "2":
            Finished = True    
            break
        else:
            pass
def chooseWeaponDamage(weaponType):
    Valid = False
    while not Valid:
        try:
            weaponDamageVal1 = int(input(f"What is the least {weaponType.capitalize()} damage should the weapon do?\n>"))
            weaponDamageVal2 = int(input(f"What is the most {weaponType.capitalize()} damage should the weapon do?\n>"))
            weaponDamageVals = [weaponDamageVal1,weaponDamageVal2]
            Valid = True
        except(TypeError):
            invalidInput()
            chooseItemType()
            return
        weaponDamageDict = {}   
        for i in len(weaponType):
            weaponDamageDict.update(weaponType[i],weaponDamageVals)
        return weaponDamageDict
def chooseItemRarity():
    raritys = ["common","uncommon","rare","epic","legendary","mythical","unobtainable"]
    try:
        itemRarity = raritys[int(input("""Choose a rarity:
        1. Common
        2. Uncommon
        3. Rare
        4. Epic
        5. Legendary
        6. Mythical
        7. Unobtainable
        >""")) - 1]
    except(TypeError,IndexError):
        invalidInput()
    return itemRarity    

def chooseStatReqs(davacis):
    statCat = [];statCatDict = {}
    statsReq = str(input("""
    What stat categories are needed? (input multiple numbers if needed)?
    1. Dexterity
    2. Agility
    3. Vitality
    4. Awareness
    5. Charisma
    6. Intellgience
    7. Strength"""))
    statsReq = statsReq.split
    for i in len(statsReq):
        try:
            statCat.append(davacis[statsReq[i]])
        except(IndexError,KeyError):
            print("Input values between 1 and 7")
    for i in len(statCat):
        try:
            statCatNum = int(input(f"How high should the player's {statCat[i]} be?"))  
            statCatDict.update(statCat[i],statCatNum)
        except(TypeError):
            invalidInput()
            chooseStatReqs(davacis)
            return
    return statCatDict
def chooseWeaponValue():
    try:
        weaponValue = int(input("What should the item be worth?\n>"))
    except(TypeError):
        invalidInput()
        chooseWeaponValue()
        return
    return weaponValue
def chooseTraitAllow():
    try:
        allowTraits = int(input("Should the weapon be allowed to have traits?\n1. Yes\n2. No"))
        allowTraits = bool(allowTraits)
    except(TypeError):
        invalidInput()
        chooseTraitAllow()
        return
    return allowTraits
def invalidInput():
    print("Invalid Input")
    logging.warning("User entered invalid value in editor.")
    dClear()
def chooseWeaponUnique():
    try:
        isUnique = int(input("Is the weapon unique (excluded from standardloot)?\n1. Yes\n2. No"))
        isUnique = bool(isUnique)
    except(TypeError):
        invalidInput()
        chooseWeaponUnique()
        return