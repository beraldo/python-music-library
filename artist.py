class Artist:
    def __init__(self, name, songs = []):
        self._name = name
        self._songs = songs
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def songs(self):
        return self._songs
    
    @songs.setter
    def songs(self, songs):
        self._songs = songs
    
    def add_song(self, song):
        self._songs.append(song)
    
    def __str__(self):
        return f'Artista: {self._name} | {len(self._songs)} músicas disponíveis'
    
