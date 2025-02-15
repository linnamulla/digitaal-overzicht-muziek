import os

oorsprongMap = input()

def getBestandNaam(oorsprongMap):
    for roots, dirs, files in os.walk(oorsprongMap):
        bestandMap = roots
        for file in files:
            if file.endswith(".flac") == True or file.endswith(".mp3") == True:
                bestandNaam = str(bestandMap + "\\" + file)
                print(bestandNaam)

getBestandNaam(oorsprongMap)