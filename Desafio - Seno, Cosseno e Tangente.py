title = 'Calculo de seno, cosseno e tangente'
print('{:=^50}'.format(title))

import math

an = float(input('Digite o angulo que você deseja: '))

sen = math.sin(math.radians(an))
print('O angulo de {} tem o Seno de {:.2f}'.format(an, sen))
cos = math.cos(math.radians(an))
print('O angulo de {} tem o Cosseno de {:.2f}'.format(an, cos))
tan = math.tan(math.radians(an))
print('O angulo de {} tem a Tangente de {:.2f}'.format(an, tan))

