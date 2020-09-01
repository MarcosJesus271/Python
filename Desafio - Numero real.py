title ='Numero real'
print('{:=^50}'.format(title))

from math import trunc

num = float(input('Digite um valor: '))
print('O numero digitado foi: {} e sua porção inteira é {}'.format(num, trunc(num)))