import os
from fileMetadata import fileMetadata, fileTypeSupported

# Accesses the metadata for a track in a given file and appends it to a list as a dictionary.
def fileAccess(sourceFolder):
    trackMetadata = []
    fileTypes = (".aac", ".alac", ".flac", ".m4a", ".mp3", ".ogg", ".wav", ".wma")
    for roots, _, files in os.walk(sourceFolder):
        for file in files:
            if file.endswith(fileTypeSupported()) == True:
                fileName = str(roots + "\\\\" + file)
                print(f"Currently retrieving metadata for: {file}")
                trackMetadata.append(fileMetadata(fileName))
    return trackMetadata

if __name__ == "__main__":
    trackMetadata = fileAccess(sourceFolder = input(""))

    # To do: make variable names more descriptive