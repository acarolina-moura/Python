"""7. Implemente um programa que, recebendo um valor inteiro, introduzido pelo utilizador,
informe se o número é positivo, negativo ou zero."""

numero = int(input("Digite um número inteiro: \n"))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
