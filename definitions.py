import os
from time import sleep
from loggingConfig import initLogger
filePath = os.path.dirname(os.path.realpath(__file__))
logging = initLogger(filePath)
def clear(mode="i"):
    if mode == "d":
        sleep(1)
    os.system('cls')
racesDict = {
    "human":{
        "name":"human",
        "davacis":(0,0,0,0,0,2,0),
        "traits":("Adaptive Mind"),
        "profs":("Adaptable","Tactics","Ambitous"),
        "biomeDrawback":("")},
    "elf":{
        "name":"elf",
        "davacis":(2,2,0,1,0,0,-2),
        "traits":("Sharp Vision","Darkvision"),
        "profs":("Archery","Light Armour","Foraging"),
        "biomeDrawback":("")},
    "lizardman":{
        "name":"lizardman",
        "davacis":(1,0,0,0,0,-1,0),
        "traits":("Sturdy"),
        "profs":("Spear Mastery"),
        "biomeDrawback":("Dry")},
    "dwarf":{
        "name":"dwarf",
        "davacis":(0,0,0,1,0,0,2),
        "traits":("Darkvision","Slow"),
        "profs":("Heavy Armour","Blunt"),
        "biomeDrawback":("Water")}}
davacis = ["dexterity","agility","vitality","awareness","charisma","intelligence","strength"]
def defineSavePath(filePath):
    try:
        with open("saveslocation.txt","r") as f:
            savePath = f.read()
    except(FileNotFoundError):
        savePath = f"{filePath}/saves"
        logging.warning(f"'saveslocation.txt' missing, creating at {savePath}.")
        with open("saveslocation.txt","w") as f:
            f.write(savePath)
        input("Enter any key to acknowledge >")
    if os.path.exists(savePath) == False:
        logging.warning(f"Save folder missing, creating at {savePath} ")
        os.mkdir(savePath)    
        input("Enter any key to acknowledge >")
    return savePath
def sanInput(message,desiredType=None,valMin=None,valMax=None,values=[],Clear=False):
    while True:
        if Clear:clear("d")
        userInput = input(message)
        if desiredType != None:
                try:
                    userInput = desiredType(userInput)
                except ValueError:
                    match desiredType.__name__:
                        case "int":
                            hrData = "an integer"
                        case "str":
                            hrData = "a character"
                        case "float":
                            hrData = "a number" 
                        case "bool":
                            hrData = "'1' or '0'"
                        case other:
                            raise SyntaxError(f"\t\t{desiredType} is not a handled type")
                    print(f"\t\tInvalid data, please enter {hrData}.")
                    continue
        if valMin != None:
            if isinstance(userInput,int) or isinstance(userInput,float):
                if valMin > userInput: 
                    print(f"\t\tPlease enter a value greater than {valMin-1}.")
                    continue
            elif isinstance(userInput,str):
                if valMin > len(userInput):
                    print(f"\t\tPlease enter a value longer than {valMin-1 if valMin > 0 else 0} characters.")
                    continue
        if valMax != None:
            if isinstance(userInput,int) or isinstance(userInput,float):
                if valMax < userInput: 
                    print(f"\t\tPlease enter a value less than {valMax+1}.")
                    continue
            elif isinstance(userInput,str):
                if valMax < len(userInput):
                    print(f"\t\tPlease enter a value shorter than {valMax+1} characters.")
                    continue
        if values != []:
            if userInput not in values:
                print(f"\t\tPlease enter one of the following values ({','.join(map(str, values))})")
                continue
        return userInput