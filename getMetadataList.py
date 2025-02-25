import os
from getFileMetadata import getFileMetadata
from tinytag import TinyTag

def getMetadataList(sourceFolder: str) -> list[dict]:
    metadataList: list = []

    for roots, _, files in os.walk(sourceFolder):
        for file in files:
            if file.endswith(TinyTag.SUPPORTED_FILE_EXTENSIONS) == True:
                fileName: str = str(roots + "\\\\" + file)

                print(f"Currently retrieving metadata for: {file}")
                metadataList.append(getFileMetadata(fileName))

    return metadataList

if __name__ == "__main__":
    sourceFolder: str = input("")
    metadataList: list[dict] = getMetadataList(sourceFolder)