from band import Band
from singer import Singer
from song import Song
from library import Library

rush = Band('Rush')
rush_songs = [
    Song('Tom Sawyer', rush, 'https://www.youtube.com/watch?v=auLBLk4ibAk'),
    Song('YYZ', rush, 'https://www.youtube.com/watch?v=LdpMpfp-J_I')
]
rush.songs = rush_songs

transatlantic = Band('Transatlantic')
transatlantic_songs = [
    Song('Duel With The Devil', transatlantic, 'https://www.youtube.com/watch?v=Phl57XmsPQ8'),
]
transatlantic.songs = transatlantic_songs

bocelli = Singer('Andrea Bocelli')
bocelli_songs = [
    Song('Con Te Partirò', bocelli, 'https://www.youtube.com/watch?v=TdWEhMOrRpQ'),
    Song('Vivo Per Lei', bocelli, 'https://www.youtube.com/watch?v=ciawICBvQoE'),
    Song('Il Mare Calmo Della Sera', bocelli, 'https://www.youtube.com/watch?v=Xjl156IBVGY'),
]
bocelli.songs = bocelli_songs


library = Library()
library.add_songs(rush.songs)
library.add_songs(transatlantic.songs)
library.add_songs(bocelli.songs)

print('Lista de Músicas:')

for song in library:
    print(song)

print('')
print('=================')
print('')


print('Lista ordenada por título')

library.sort_by_song_title()

for song in library:
    print(song)

print('')
print('=================')
print('')

print('Lista ordenada por artista')

library.sort_by_song_artist()

for song in library:
    print(song)
