import os

mapNaam = input()

for roots, dirs, files in os.walk(mapNaam):
    for file in files:
        if file.endswith(".flac") == True or file.endswith(".mp3") == True:
            bestandNaam = str(mapNaam + "\\\\" + file)
            print(bestandNaam)