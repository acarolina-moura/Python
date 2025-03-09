"""Escreve um programa que receba três números reais e indique qual o maior dos três
números. """


print("Vamos verificar qual o maior número")

numero1 = float(input("Digite o primeiro número: \n"))
numero2 = float(input("Digite o segundo número: \n"))
numero3 = float(input("Digite o terceiro número:\n"))

if numero1 == numero2 and numero2 == numero3:
    print("Os números são iguais")
else:
    if numero1 > numero2 and numero1 > numero3 :
        print(f"O número {numero1} é o maior número")
    elif numero2 > numero1 and numero2 > numero3:
        print(f"O número {numero2} é o maior número")
    else:
        print(f"O número {numero3} é o maior número")
        
