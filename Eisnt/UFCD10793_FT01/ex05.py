"""Sejam a e b os catetos de um triângulo retângulo, faz um programa que devolva o valor
da hipotenusa (deverá ser criado o ficheiro ex05.py)."""

import math

print("Vamos calcular a hipotenusa de um triângulo retângulo")

cateto1 = int(input("Digite o valor do cateto 1: \n"))
cateto2 = int(input("Digite o valor do cateto 2: \n"))

def valor_hipotenusa(cateto1, cateto2):
    hipotenusa = math.sqrt(cateto1 * 2 + cateto2 * 2)
    return hipotenusa

result = valor_hipotenusa(cateto1, cateto2)
print("O valor da hipotenusa é" , result)
