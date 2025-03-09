"""1. Escreve uma função em Python que, dados a medida do comprimento dos três 
lados de um triângulo diga se o mesmo é equilátero, isósceles ou escaleno. """

def classifica_triangulos(lado1,lado2,lado3):
    if lado1 == lado2 and lado2 == lado3:
        print("Equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Isósceles")
    else:
        print("Escaleno")

classifica_triangulos(15,15,15)
classifica_triangulos(30,15,15)
classifica_triangulos(15,45,50)