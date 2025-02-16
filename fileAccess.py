import os
from fileMetadata import fileMetadata

def fileAccess(source22Folder):
    for roots, dirs, files in os.walk(source22Folder):
        for file in files:
            if file.endswith(".flac") == True or file.endswith(".mp3") == True:
                fileName = str(roots + "\\" + file)
                result = fileMetadata(fileName)
                print(result)

if __name__ == "__main__":
    source22Folder = input()
    fileAccess(source22Folder)