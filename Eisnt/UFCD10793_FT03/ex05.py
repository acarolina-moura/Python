"""Escreva um programa que verifique se um determinado número introduzido pelo
utilizador é nulo, positivo ou negativo."""

print("Vamos verificar um número")

numero = int(input("Digite o número: \n"))

if numero == 0:
    print(f"O número {numero} é nulo")
elif numero > 0:
    print(f"O número {numero} é positivo")
else:
    print(f"O número {numero} é negativo")