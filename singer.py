from artist import Artist

class Singer(Artist):
    pass

    def __str__(self):
        return f'Cantor(a): {self._name} | {len(self._songs)} músicas disponíveis'