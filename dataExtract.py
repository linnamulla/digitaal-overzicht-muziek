import pandas as pd
from getMetadataList import getMetadataList

def dataTransform(metadataList: list[dict]) -> pd.DataFrame:
    df: pd.DataFrame = pd.DataFrame(metadataList)

    return df

sourceFolder: str = input("")
metadataList: list[dict] = getMetadataList(sourceFolder)
df = dataTransform(metadataList)
df.to_csv("data\\rawData.csv", sep = ";")