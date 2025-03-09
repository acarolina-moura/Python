"""8. Escreve um programa para classificar um triângulo de acordo com o comprimento dos
seus lados.

Considere as seguintes informações:
• Triângulo equilátero: todos os lados possuem o mesmo comprimento;
• Triângulo escaleno: todos os lados possuem comprimento diferente;
• Triângulo isósceles: caracterizado por ter dois lados com o mesmo comprimento"""

print("Vamos classificar o triângulo")
ladoA = float(input("Digite o lado A: "))
ladoB = float(input("Digite o lado B: "))
ladoC = float(input("Digite o lado C: "))

if ladoA < 0 or ladoB < 0 or ladoC < 0:
    print("Não é um triangulo")
else:
    if ladoA == ladoB and ladoB == ladoC:
        print("É um triangulo EQUILÁTERO")
    elif ladoA != ladoB and ladoB != ladoC:
        print("É um triangulo ESCALENO")
    else:
        print("É um triangulo ISÓSCELES")
