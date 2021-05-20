a = int(input("Primeiro bimestre: "))
while a > 10:
    a = int(input('Digite um numero menor ou igualque 10: '))

b = int(input("Segundo bimestre: "))
while b > 10:
    b = int(input('Digite um numero menor ou igual que 10: '))

c = int(input("Terceiro bimestre: "))
while c > 10:
    c = int(input('Digite um numero menor ou igual que 10: '))

d = int(input("Quarto bimestre: "))
while d > 10:
    d = int(input('Digite um numero menor ou igual 10: '))

media = (a + b + c + d) / 4
print('media: {}'.format(media))

# a = int(input("Digite o primeiro valor: "))
# b = int(input("Digite o segundo valor: "))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or not resto_b > 0:
#
#     print('Foi digitado um numero par')
#
# else:
#     print('Nenhum numero par foi digitado')




# a = int(input("Digite o primeiro valor: "))
# b = int(input("Digite o segundo valor: "))
# c = int(input("Digite o terceiro valor: "))
#
# if a > b and a > c:
#     print('O maior valor é {}'.format(a))
# elif b > a and b > c:
#     print('O maiot valor é {}'.format(b))
# else:
#     print('O maior valor é {}'.format(c))
#
# print('Fim do programa.')
