import os
from getFileMetadata import getFileMetadata, checkFileTypeSupport

def getMetadataList(sourceFolder: str) -> list[dict]:
    metadataList: list = []

    for roots, _, files in os.walk(sourceFolder):
        for file in files:
            if file.endswith(checkFileTypeSupport()) == True:
                fileName: str = str(roots + "\\\\" + file)

                print(f"Currently retrieving metadata for: {file}")
                metadataList.append(getFileMetadata(fileName))

    return metadataList

if __name__ == "__main__":
    sourceFolder: str = input("")
    metadataList: list = getMetadataList(sourceFolder)