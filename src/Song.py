class Song(object):    
    def __init__(self, title, artist):
        self._title = title
        self._artist = artist
        path = self.filename_fmt(self._artist, self._title)
        print(f"SONG: {self._title} / {self._artist} / {path}")
        self._file = open(path, "r")
        self.words = nltk.word_tokenize(self._file.read())
            
    @classmethod
    def from_file(cls, filename):
        m = re.match(r"([^_]+)(?:_)([^_]+)(?:\.song)", filename)
        g = m.groups()
        return cls(g[1], g[0])
        
    def filtered(self):
        return [t.lower() for t in self.words if t.isalnum() and (t.lower() not in stop_words) and (t not in punctuation)]
    
    def freq_dist(self):
        return nltk.FreqDist(self.filtered())
    
    @staticmethod
    def filename_fmt(artist, title = None,):
        titlestr = str(title) if title is not None else "*"
        return Path(f"{artist}_{titlestr}.song")
