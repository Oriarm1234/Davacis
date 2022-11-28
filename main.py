################################################################################
# Imports
# Files
# Modules
import json
import logging
from logging.config import fileConfig
from definitions import iClear, dClear
from definitions import races, davacis
from raceSelection import raceSelect
import os
import sys
import time
from itemMaker import openItemDesigner
################################################################################
# Paths
filePath = os.path.dirname(os.path.realpath(__file__))
try:
    with open("saveslocation.txt","r") as f:
        savesPath = f.read()
except(FileNotFoundError):
    savesPath = f"{filePath}/saves"
    logging.warning(f"'saveslocation.txt' missing, creating at {savesPath}.")
    with open("saveslocation.txt","w") as f:
        f.write(savesPath)
    input("Enter any key to acknowledge >")
if os.path.exists(savesPath) == False:
    logging.warning(f"Save folder missing, creating at {savesPath} ")
    os.mkdir(savesPath)    
    input("Enter any key to acknowledge >")
################################################################################
# Savings
def saveGame(saveSlot,player,savesPath):
    slotContent = os.listdir(f"{savesPath}/{saveSlot}")
    slotPath = f"{savesPath}/{saveSlot}"
    if "player.txt" in slotContent:
        print("Saving...")
        for attribute, value in player.__dict__.items():    
            with open(f"{slotPath}/player.txt","a") as f:
                f.write(f"{attribute}={value}\n")
    else:
        f = open(f"{slotPath}/player.txt","x")
        f.close()
        saveGame(saveSlot,player,savesPath)
    dClear()    
################################################################################
# Logging
logPath = f"{filePath}/logs"
logger = logging.getLogger()
if "debug_old_old.log" in os.listdir(logPath):
    os.remove(f"{logPath}/debug_old_old.log")
if "debug_old.log" in os.listdir(logPath):
    os.rename(f"{logPath}/debug_old.log",f"{logPath}/debug_old_old.log")
if "debug.log" in os.listdir(logPath):
    os.rename(f"{logPath}/debug.log",f"{logPath}/debug_old.log")
try:
    fileConfig('logging.ini')
except(KeyError):
    logging.basicConfig(filename='%(filePath)s/logs',level=logging.DEBUG,format='%(levelname)s:%(message)s',)
    logging.warning("'logging.ini' missing or corrupted. Logging will not function correctly and will revert to basic settings.")
    input("Enter any key to acknowledge >")
except(FileNotFoundError):
    os.mkdir(f"{logPath}")
    fileConfig('logging.ini')
    logging.debug(f"Logging directory missing, creating at {logPath}")
if not "debug.log" in os.listdir(f"{logPath}/"):
    f = open(f"{logPath}/debug.log","x")
    f.close()
    logging.debug("Created debug.log")
################################################################################
# Main Menu
iClear()
def mainMenu():
    dClear()
    correct = 0
    navigate = str(input(f"""
-------Main Menu-------
      1.New Game
      2.Load Game
      3.Help
      4.Settings
      5.Quit
    >"""))
    while correct != 1:
        match navigate:
            case "1":
                slotMade = 0
                while slotMade != 1:
                    validName = False
                    while not validName:
                        saveSlot = str(input("What would you like to name the save slot? >")).strip().replace(' ', '_')
                        if "\\" in saveSlot or "/" in saveSlot:
                            print("Save slot cannot contain slashes")
                        else:
                            validName = True    
                    if saveSlot == "":
                        print("Slot name cannot be empty")
                        dClear()
                    try:
                        os.mkdir(f"{savesPath}\\{saveSlot}")
                        slotMade = 1
                    except(FileExistsError):
                        if len(os.listdir(f"{savesPath}\\{saveSlot}")) == 0:
                            logging.warning("Slot creation failed due to empty slot taking name.")
                            navigate = str(input("Slot name is taken by an empty slot. Override? (y/n)\n>")).lower()
                            if navigate == "y":
                                os.rmdir(saveSlot)
                                mainMenu()
                            else:
                                mainMenu()
                        logging.warning("Slot name taken.")
                        override = str(input("Would you like to override the slot? (y/n)")).lower()
                        if override == "y":
                            os.rmdir(f"{savesPath}\\{saveSlot}")
                            os.mkdir(f"{savesPath}\\{saveSlot}")
                        else:
                            print("Returning to main menu")
                        dClear()    
                try:
                    player = raceSelect(races,davacis)
                except(TypeError):
                    player = raceSelect(races,davacis)
                    logging.error
                    return
                player.sparePoints = 20
                iClear()
                player.statAssign()
                saveGame(saveSlot,player,savesPath)
            case "2":
                loaded = 0
                while loaded == 0:
                    print("What slot would you like to load")
                    slots = os.listdir(savesPath)
                    for i in range(len(slots)):
                        print(f"{i + 1}.{slots[i]}")
                    try:
                        saveSlot = slots[1 - int(input(">"))]
                        slotPath = f"{savesPath}/{saveSlot}"
                        if len(os.listdir(f"{slotPath}")) == 0:
                            logging.debug("User loaded empty directory, removing.")
                            print("File is empty, removing.")
                            os.rmdir(slotPath)
                    except(ValueError):
                        logging.debug("User entered non-integer")
                        print("Please enter an integer listed on the left.")
                        dClear()   
                        continue
                    except(IndexError):
                        logging.debug("User entered out-of-range integer.")
                        print("Please enter an integer within the range of the one on the left.")
                        continue
                    try:
                        with open(f"{slotPath}/player.txt") as f:    
                            lines = f.readlines()
                            playerLoading = {}
                            for lineNum in range(len(lines)):
                                content = lines[lineNum].split("=")
                                key = content[0];value = content[1]
                                playerLoading[key] = value
                            from stats import PlayerClass
                            player = PlayerClass()
                            player.loadFromDict(playerLoading)
                            player.race = dict(eval(player.race))
                            print(playerLoading,player)
                            valid = False
                            while not valid:
                                navigate = str(input(f"{player}\nIs this the correct file?(y/n)\n>"))
                                if navigate == "n":
                                    print("Returning to slot selection...")
                                    dClear()
                                    valid == True
                                elif navigate == "y":
                                    loaded = 1
                                    valid == True
                                else:
                                    print("Invalid input, input either 'Y' or 'N'")
                    except(FileNotFoundError):
                        navigate = str(input("Save slot is empty or corrupted. Delete? (y/n)"))
                        if navigate == "y":
                            os.rmdir(slotPath)
                            logging.debug(f"Removed {slotPath}")
                            mainMenu()
                        elif navigate == "n":
                            mainMenu()    
                        else:
                            print("Invalid input, returning to main menu.")
                            dClear()
            case "3":
                print("TBA")
                mainMenu()
            case "4":
                navigate = str(input("""
                ---------Settings---------
                1. Wipe Saves Folder
                2. Open Item Designer
                3. Exit
                >"""))          
                if navigate == "1":
                    confirm = str(input("Confirm you want ALL saves deleted. (y/n) \n>"))
                    if confirm == 1:
                        folders = os.listdir(f"{filePath}/saves")
                        for folder in folders:
                            os.rmdir(folder)
                    else:
                        mainMenu()
                        return
                if navigate == "2":
                    openItemDesigner(filePath)
                else:
                    mainMenu()
                    return
            case "5":
                confirm = str(input("Are you sure you want to exit? (y/n)")).lower()
                if confirm == "y":
                    raise SystemExit
                elif confirm == "n":
                    print("Returning to main menu...")
                    mainMenu()
                else:
                    print("Invalid input, returning to start of creation.")
                    mainMenu()
            case other:
                print("Incorrect value input. Please enter a number from 1-5.")     
                mainMenu()
        correct = 1
mainMenu()
################################################################################
# juandeez nuts in your mouth
def game():
    def test():
        prompt = str(input("""
        Test:
        1. Cont
        2. Die
        3. Fight"""))