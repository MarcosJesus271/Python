title = 'Preço de passagem'
print('{:=^50}'.format(title))

distancia = float(input('Qual a distancia de sua viagem? '))
print('Você esta prestes a realizar uma viagem de {}Km'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de {:.2f}'.format(preço))