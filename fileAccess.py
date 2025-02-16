import os
from fileMetadata import fileMetadata

def fileAccess(sourceFolder):
    for roots, _, files in os.walk(sourceFolder):
        for file in files:
            if file.endswith(".flac") == True or file.endswith(".mp3") == True:
                fileName = str(roots + "\\\\" + file)
                result = fileMetadata(fileName)
                print(result)

if __name__ == "__main__":
    fileAccess(sourceFolder = input(""))