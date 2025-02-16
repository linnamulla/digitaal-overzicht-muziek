from tinytag import TinyTag

def fileMetadata(fileName):
    # Returns a dictionary of metadata for a given file/track.
    tag: TinyTag = TinyTag.get(fileName)
    # Common metadata
    # File/audio properties
    metaBitdepth = tag.bitdepth
    metaBitrate = tag.bitrate
    metaDuration = tag.duration
    metaFilesize = tag.filesize
    metaSamplerate = tag.samplerate

    # Fields
    metaAlbum = tag.album
    metaAlbumartist = tag.albumartist
    metaArtist = tag.artist
    metaGenre = tag.genre
    metaTitle = tag.title
    metaTrack = tag.track
    metaYear = tag.year

    return {"bitdepth": metaBitdepth,
            "bitrate": metaBitrate,
            "duration": metaDuration,
            "filesize": metaFilesize,
            "samplerate": metaSamplerate,
            "album": metaAlbum,
            "albumartist": metaAlbumartist,
            "artist": metaArtist,
            "genre": metaGenre,
            "title": metaTitle,
            "track": metaTrack,
            "year": metaYear}

def fileTypeSupported():
    # Returns a tuple containing file extensions supported by TinyTag.
    return TinyTag.SUPPORTED_FILE_EXTENSIONS