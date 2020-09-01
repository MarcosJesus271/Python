title = 'Calcular Cateto'
print('{:=^50}'.format)

import math

co = float(input('Comprimento do cateto Oposto: '))
ca = float(input('Comprimento do cateto Adjacente: '))
hi = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))
