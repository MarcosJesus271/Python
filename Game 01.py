title = 'Jogo da Advinhação'
print('{:=^50}'.format(title))

from time import sleep
import random
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
lista = [0, 1, 2, 3, 4, 5]
computador = random.choice(lista)
print ('Pensando...Hmmm....')
sleep(2)
player = int(input('Em que número pensei? '))
if player == computador:
    print('\nBrabo, você me venceu!')
else:
    print('\nErrrrroooou! Eu pensei em: {}'.format(computador))

