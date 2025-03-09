"""Escreve um programa que solicite um número inteiro ao utilizador e verifique se o 
mesmo é par ou ímpar. A mensagem no ecrã deverá ter o seguinte formato; 
"O número [número] é [par/ímpar]" """


print("Vamos verificar se o número é par ou ímpar:")

numero = int(input("Digite o número: \n"))


if numero % 2 == 0:
    print("Este número é par")
else:
    print(f"O número {numero} é ímpar")