class Artist(object):
    def __init__(self, name, song_dir = 'songs'):
        self.name = name
        p = Path(song_dir)
        self.songs = [Song.from_file(str(n)) for n in p.glob(str(Song.filename_fmt(self.name)))]