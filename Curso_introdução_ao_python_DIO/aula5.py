lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
# print(sum(lista))
# print(min(lista_animal))
nova_lista = lista_animal * 3
print(nova_lista)

if 'lobo' in lista_animal:
    print('existe um lobo na lista')
else:
    print('não existe lobo na lista, irei add: \n')
    lista_animal.append('lobo')
    print(lista_animal)

lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(tupla))


# # lista_animal.pop(1)
# # print(lista_animal)
#
# lista_animal.remove('elefante')
# print(lista_animal)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print (soma)