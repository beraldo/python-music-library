from collections.abc import MutableSequence # ABC = Abastract Base Classes

class Library(MutableSequence):
    def __init__(self, songs = []):
        self._songs = songs
    
    def add_song(self, song):
        self._songs.append(song)
    
    def add_songs(self, songs):
        for song in songs:
            self._songs.append(song)

    def __delitem__(self, key):
        del self._songs[key]
    
    def __getitem__(self, key):
        return self._songs[key]
    
    def __len__(self):
        return len(self._songs)
        
    def __setitem__(self, key, item):
        self._songs[key] = item
    
    def insert(self, item):
        self._songs.append(item)
    
    def sort_by_song_title(self):
        self._songs = sorted(self._songs, key=lambda song: song.title)
    
    def sort_by_song_artist(self):
        self._songs = sorted(self._songs, key=lambda song: song.artist.name)
