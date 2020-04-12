from artist import Artist

class Band(Artist):
    pass

    def __str__(self):
        return f'Banda: {self._name} | {len(self._songs)} músicas disponíveis'