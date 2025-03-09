"""2. Escreve uma função em Python que, dados a medida do comprimento do lado de  
um quadrado imprima os valores do seu perímero e da sua área (area=lado x 
lado; perimetro = 4 x lado)."""

def calcula_perimetro_area(lado):
    area = lado * lado
    print(f"A área do quadrado é {area}")
    perimetro = lado * 4
    print(f"O perímetro do quadrado é {perimetro}")
 
calcula_perimetro_area(30)