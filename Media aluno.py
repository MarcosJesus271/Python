title ='Calculo de média final para alunos'
print ('{:=^60}'.format(title))

aluno = str(input('\nInformar nome do Aluno(a): ')).strip()
nome = aluno.split()
n1 = float(input('Digite a primeira nota do aluno(a) {}:'.format(nome[0])))
n2 = float(input('Digite a segunda nota do aluno(a) {}:'.format(nome[0])))
n3 = float(input('Digite a terceira nota do aluno(a) {}:'.format(nome[0])))
n4 = float(input('Digite a quarta nota do aluno(a) {}:'.format(nome[0])))

media = (n1+n2+n3+n4)/4
print('\nA média de {}, é : {:.1f}'.format(nome[0], media))
if media >= 7:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')

