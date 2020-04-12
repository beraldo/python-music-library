class Song:
    def __init__(self, title, artist, url):
        self._title = title
        self._artist = artist
        self._url = url
    
    @property
    def title(self):
        return self._title
    
    @property
    def artist(self):
        return self._artist
    
    @property
    def url(self):
        return self._url
    
    @url.setter
    def link(self, url):
        self._url = url
    
    def __str__(self):
        return f'{self._title}, de {self._artist.name}: {self._url}'
