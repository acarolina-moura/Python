""" Escreve um programa que receba dois números reais e indique qual o maior dos dois 
números. Considera a possibilidade de o utilizador indicar dois números iguais. """


print("Digite dois números:")

numero1 = int(input("Digite o número1: \n"))
numero2 = int(input("Digite o número2: \n"))

if numero1 > numero2:
    print(f"O número {numero1} é maior do que o {numero2}")
elif numero2 > numero1:
    print(f"O número {numero2} é maior  do que o número {numero1}")
else:
    print(f"Os números são iguais")