from tinytag import TinyTag as tt

def fileMetadata(fileName):
    tag: tt = tt.get(fileName)
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

    return metaBitdepth, metaBitrate, metaDuration, metaFilesize, metaSamplerate, metaAlbum, metaAlbumartist, metaArtist, metaGenre, metaTitle, metaTrack, metaYear