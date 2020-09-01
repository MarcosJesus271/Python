title = 'Modo musica'
print('{:=^50}'.format(title))

import emoji

print(emoji.emojize('Olá habitante do planta terra! :earth_americas:', use_aliases=True))

from pygame import mixer
mixer.init()
mixer.music.load('musi')
mixer.music.play()
input('Agora você escuta?')
