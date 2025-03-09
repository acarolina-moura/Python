"""  Escreve um programa que calcule o volume de uma esfera. O valor do raio deverá ser
 introduzido pelo utilizador (deverá ser criado o ficheiro ex04.py)"""
 
import math

pi = math.pi

print("Vamos calcular o volume de uma esfera")
raio = float(input ("Digite o valor do raio da esfera: \n"))
print("Você digitou" , raio)
if raio < 0 :
        print("Digite um número maior do que Zero")


def calc_volume_esfera(raio):
    volume_esfera = (4/3) * pi * (raio ** 3)
    return volume_esfera

result = calc_volume_esfera(raio)
print("O valor do volume da esfera é" , result)