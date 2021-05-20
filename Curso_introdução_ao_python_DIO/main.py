a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

soma = a+b
subtracao = a-b
multiplicacao = a*b
divisao = a/b
resto = a%b

resultado = ("Soma: {soma} \nSubtração: {sub}"
      "\nMultiplicação: {mult}"
      "\nDivisão: {div} "
      "\nResto: {resto}".format(soma=soma,sub=subtracao,mult=multiplicacao,
                                div=divisao,resto=resto))
print(resultado)