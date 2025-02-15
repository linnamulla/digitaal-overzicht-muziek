import os

oorsprongMap = input()

def fooPseudo(bestandNaam):
    artiestLijst = []; albumartiestLijst = []
    #artiest = bestandNaam.artist(); albumartiest = bestandNaam.albumartist(); album = bestandNaam.album()
    #artiestLijst = artiestLijst.append(artiest)
    #albumartiestLijst = albumartiestLijst.append(albumartiest)
    print(bestandNaam)
    return artiestLijst, albumartiestLijst

for roots, dirs, files in os.walk(oorsprongMap):
    bestandMap = roots
    for file in files:
        if file.endswith(".flac") == True or file.endswith(".mp3") == True:
            bestandNaam = str(bestandMap + "\\" + file)
            fooPseudo(bestandNaam)
