import os
import time
def iClear():
    os.system('cls')
def dClear(): # clear with cooldown
    time.sleep(1.5)
    iClear()
races = {
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
        "profs":("SpearMastery"),
        "biomeDrawback":("Dry")},
    "dwarf":{
        "name":"dwarf",
        "davacis":(0,0,0,1,0,0,2),
        "traits":("Darkvision","Slow"),
        "profs":("Heavy Armour","Blunt"),
        "biomeDrawback":("Water")}}
davacis = ["dexterity","agility","vitality","awareness","charisma","intelligence","strength"]