"""Escreva um programa que peça ao utilizador 20 números reais e no final mostre a soma e a média 
dos números introduzidos. """

# numero = int(input("Escreva o número: \n"))
# soma = 0
# for x in range (20):
#     soma += numero
#     print("A soma dos números é: ", soma)
#     media = soma / 20
#     print("A média é: ", media)



soma=0
Contador=20
for i in range(Contador):
    num = float(input("Introduza um número real: "))
    soma += num
media = soma/Contador
print("Soma:",soma)
print("Media:",media)