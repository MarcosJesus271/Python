title = 'Modo musica'
print('{:=^50}'.format(title))

import emoji

print(emoji.emojize('Olá habitante do planta terra! :earth_americas:', use_aliases=True))
print('Vamos ouvir uma musiquita? Segue o play....')

import pygame
pygame.init()
pygame.mixer.music.load('musi')
pygame.mixer.music.play()
paygame.event.wait()


