#Fazer um programa para ler quatro números inteiros e positivos, calcular e devolver a sua média.


# primeiro_numero = int(input("Digite o primeiro número: \n"))
# segundo_numero = int(input("Digite o segundo número: \n"))
# terceiro_numero = int(input("Digite o terceiro número: \n"))
# quarto_numero = int(input("Digite o quarto número: \n"))

# if primeiro_numero or segundo_numero or terceiro_numero or quarto_numero < 0:
#     print("Digite um número válido")


i = 0
soma = 0
while i < 4:
    numero = int(input(f"Digite o número {i + 0}: \n"))
    soma +=  numero
    i += 1
    print(soma)
      
media = soma / i
print(f"A média é:", media)




# media = (primeiro_numero + segundo_numero + terceiro_numero + quarto_numero) / 4
# print(f"A média é", media)
