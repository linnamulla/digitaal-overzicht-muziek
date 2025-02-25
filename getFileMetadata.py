from tinytag import TinyTag

def getFileMetadata(fileName: str) -> dict:
    tag: TinyTag = TinyTag.get(fileName)

    return {"bitdepth": tag.bitdepth,
            "bitrate": tag.bitrate,
            "duration": tag.duration,
            "filesize": tag.filesize,
            "samplerate": tag.samplerate,
            "album": tag.album,
            "albumartist": tag.albumartist,
            "artist": tag.artist,
            "genre": tag.genre,
            "title": tag.title,
            "track": tag.track,
            "year": tag.year}

def checkFileTypeSupport() -> tuple:
    return TinyTag.SUPPORTED_FILE_EXTENSIONS