title = 'Modo aleatorio'
print('{:=^50}'.format(title))

import random

n1 = input("Primeiro Aluno: ")
n2 = input("segundo Aluno: ")
n3 = input("terceiro Aluno: ")
n4 = input("Quarto Aluno: ")

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A Ordem será: {}'.format(lista))