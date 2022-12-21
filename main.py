################################################################################
# Boujh Dawizard
# Imports
# Files
# Modules
import os
from definitions import *
from loggingConfig import initLogger
logging = initLogger(filePath)
######################################
from playerFile import PlayerClass
savePath = defineSavePath(filePath)
from itemMaker import openItemDesigner
################################################################################
# Main Menu
clear("i")
def mainMenu():
    while True:
        correct = 0
        navigate = sanInput(f"""
\t\t---Main Menu-------
\t\t  1.New Game
\t\t  2.Load Game
\t\t  3.Help
\t\t  4.Settings
\t\t  5.Quit
\t\t> """, int, 1, 5, Clear=True)

        match navigate:
            case 1:
                player = PlayerClass()
                player.newGame(savePath)
                return
            case 2:
                player = PlayerClass()
                if player.loadGame(savePath) == "CONTINUE":
                    continue
            case 3:
                clear("d")
                print("To Be Added")
                continue
            case 4:
                navigate = sanInput("""
\t\t---------Settings---------
\t\t1. Wipe Saves Folder
\t\t2. Open Item Designer
\t\t3. Exit
\t\t> """, int, 1, 3, Clear=True)
                if navigate == 1:
                    confirm = sanInput("\t\tConfirm you want ALL saves deleted. (y/n) \n\t\t> ", str, values=["y", "n"], Clear=True)
                    if confirm == "y":
                        folders = os.listdir(f"{filePath}\\saves")
                        for folder in folders:
                            for file in os.listdir(f"{filePath}\\saves\\{folder}"):
                                os.remove(f"{filePath}\\saves\\{folder}\\{file}")
                            os.rmdir(f"{filePath}\\saves\\{folder}")
                    else:
                        continue
                if navigate == 2:
                    openItemDesigner(filePath)
                continue
            case 5:
                confirm = sanInput("\t\tAre you sure you want to exit? (y/n)\n\t\t> ", str, values=["y", "n"], Clear=True)
                if confirm == "y":
                    raise SystemExit
                elif confirm == "n":
                    print("\t\tReturning to main menu...")
                    continue
mainMenu()