class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b
    def sub(self):
        return self.valor_a - self.valor_b
    def mult(self):
        return self.valor_a * self.valor_b
    def divi(self):
        return self.valor_a / self.valor_b

calculadora = Calculadora(10,2)
print(calculadora.soma())
print(calculadora.sub())
print(calculadora.mult())
print(calculadora.divi())


#Metodos
# def soma(a, b):
#     return a + b
# def sub(a, b):
#     return a - b
# def mult(a, b):
#     return a * b
# def divi(a, b):
#     return a / b

# print(mult(2, 10))
# print(divi(10, 2))
# print(sub (10, 8))
# print(soma (3, 2))