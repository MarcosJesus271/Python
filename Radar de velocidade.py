title = 'Radar de velocidade'
print('{:=^50}'.format(title))

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado! Você exedeu o limite de 80Km/h.')
    multa = (velocidade - 80) * 7
    print('Você deverá pagar R${:.2f} de multa'.format(multa))
print('Tenha um bom dia, dirija com segurança')

