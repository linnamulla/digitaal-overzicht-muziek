import os
from fileMetadata import fileMetadata

# Creates a dictionary containing the metadata for a given track.
class Track:
    def __init__(self, trackMetadata):
        self.bitdepth, self.bitrate, self.duration, self.filesize, self.samplerate, self.album, self.albumartist, self.artist, self.genre, self.title, self.track, self.year = trackMetadata
        
    def trackDictionaryFromClass(self):
        return {"bitdepth": self.bitdepth,
                "bitrate": self.bitrate,
                "duration": self.duration,
                "filesize": self.filesize,
                "samplerate": self.samplerate,
                "album": self.album,
                "albumartist": self.albumartist,
                "artist": self.artist,
                "genre": self.genre,
                "title": self.title,
                "track": self.track,
                "year": self.year}

# Accesses the metadata for a track in a given file and appends it to a list as a dictionary.
def fileAccess(sourceFolder):
    trackList = []
    for roots, _, files in os.walk(sourceFolder):
        for file in files:
            if file.endswith(".flac") == True or file.endswith(".mp3") == True:
                fileName = str(roots + "\\\\" + file)
                print(f"Currently retrieving metadata for: {file}")
                trackMetadata = fileMetadata(fileName)
                trackList.append(Track(trackMetadata).__dict__)
    return trackList

if __name__ == "__main__":
    trackList = fileAccess(sourceFolder = input(""))