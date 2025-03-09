""" Elabora um programa que pede ao utilizador para inserir dois números inteiros. 
O programa deve escrever todos os números inteiros entre os dois limites por ordem crescente. Utiliza o ciclo for. """

numero1 = int(input("Insira o primeiro número: \n"))
numero2 = int(input("Insira o segundo número: \n\n"))

if numero1 < numero2:
    for x in range(numero1, numero2+1):
        print(x)
elif numero2 < numero1:
    for y in range (numero2, numero1+1):
        print(y)
else:
    print("Os números são iguais")