import os
from os import system, name
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
clear()
packagefolder = os.getenv('LOCALAPPDATA') + '/Packages'
HasBedrock = False
HasJava = False
for file in os.listdir(packagefolder):
    filename = os.fsdecode(file)
    if filename.startswith("Microsoft.MinecraftUWP_"):
        HasBedrock = True
        print("Minecraft Bedrock Worlds: ")
        print(" ")
        gamefolder = packagefolder + '/' + filename + '/LocalState/games/com.mojang'
        mapsfolder = gamefolder + '/minecraftWorlds'
        os.chdir(gamefolder)
        if os.path.exists(mapsfolder):

            os.chdir(mapsfolder)
            print('World ID             Name of the world')
            print(" ")
            BWorldAmount = 0
            for file in os.listdir(mapsfolder):
                mapfoldername = os.fsdecode(file)
                if os.path.isdir(mapfoldername):
                    os.chdir(mapfoldername)
                    with open('levelname.txt') as f:
                        lines = f.read()
                        worldname = lines.split('\n', 1)[0]
                    print(mapfoldername + '         ' + worldname)
                    BWorldAmount += 1
                    os.chdir(mapsfolder)
            BWorldStr = str(BWorldAmount)
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print('Found ' + BWorldStr + ' worlds')
                    
            if BWorldAmount == 0:
                clear()
                print("Minecraft Bedrock Worlds: ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print("You dont currently have any worlds.")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print("Found 0 worlds")
                #if os.path.exists(mapsfolder + mapfoldername + '/levelname.txt'):
                #    print(mapfoldername)
            print(" ")
            print(" ")
            print(" ")
            print(" ")
        else:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("You dont currently have any worlds.")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("Found 0 worlds")
appdatafolder = os.getenv("APPDATA")
os.chdir(appdatafolder)
if os.path.exists(".minecraft"):
    HasJava = True
    if HasBedrock == True:
        print(" ")
        print("-----------------------------------------------------------------------------")
        print(" ")
    JWorldAmount = 0
    print('Minecraft Java Worlds:')
    print(" ")
    for file in os.listdir(appdatafolder + '/.minecraft/saves'):
        os.chdir(appdatafolder + '/.minecraft/saves')
        if os.path.isdir(file):
            print(file)
            JWorldAmount += 1
    JWorldStr = str(JWorldAmount)
    if JWorldAmount == 0:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("You dont currently have any worlds.")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("Found 0 worlds")
    else:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("Found " + JWorldStr + ' worlds')
    print(" ")
    print(" ")
    print(" ")
    print(" ")
if HasBedrock == False and HasJava == False:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("You dont own minecraft.")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
elif HasBedrock == True and HasJava == False:
    print("You own Minecraft Bedrock Edition")
    print(" ")
    print(" ")
elif HasBedrock == False and HasJava == True:
    print("You own Minecraft Java Edition")
    print(" ")
    print(" ")
elif HasBedrock == True and HasJava == True:
    print("You own both Minecraft Bedrock Edition and Minecraft Java Edition")
    print(" ")
    print(" ")
input('Press enter to exit.')