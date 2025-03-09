# """O Índice de Massa Corporal (IMC) é utilizado para medir o peso ideal de uma pessoa.

# Escreve um programa que peça o nome, a idade, o peso e a altura do utilizador e que,
# de seguida, calcule e mostre o resultado do seu IMC e classifique esse resultado de
# acordo com as seguintes condições:

# • IMC<17 - Muito abaixo do peso ideal
# • 17<=IMC<18,5 - Abaixo do peso
# • 18,5<=IMC<25 - Peso normal
# • 25<=IMC<30 - Acima do peso
# • 30<=IMC<35 - Obesidade I
# • 35<=IMC<40 - Obesidade II (severa)
# • IMC>=40 - Obesidade III (mórbida) """

# name =str(input("Digite seu nome: \n"))
# age = int(input("Digite sua idade: \n"))
# height = float(input("Digite sua altura: \n"))

# imc = weight / (height ** 2)

# weight = float(input("Digite seu peso: \n")):
# match = weight:
# if imc < 17:
#     category = "Muito abaixo do peso"
# case 1: 17 <= imc < 18.5:
#     category = "Abaixo do peso"
# case 2: 18.5 <= imc < 25:
#     category = "Peso normal"
# case 3:  25 <= imc < 30:
#     category = "Acima do peso"
# case 4: 30 <= imc < 35:
#     category = "Obesidade I"
# case 5:  35 <= imc < 40:
#     category = "Obesidade II"
# case 6:
#     category = "Obesidade III"

# print(f"\n{name}, com {age} anos, seu IMC é {imc:.2f} e sua categoria é '{category}'.")


# def weekday(n):
#    match n:
#       case 0: return "Monday"
#       case 1: return "Tuesday"
#       case 2: return "Wednesday"
#       case 3: return "Thursday"
#       case 4: return "Friday"
#       case 5: return "Saturday"
#       case 6: return "Sunday"
#       case _: return "Invalid day number"
# print (weekday(3))
# print (weekday(6))
# print (weekday(7))

# # if imc < 17:
# #     category = "Muito abaixo do peso"
# # elif 17 <= imc < 18.5:
# #     category = "Abaixo do peso"
# # elif 18.5 <= imc < 25:
# #     category = "Peso normal"
# # elif 25 <= imc < 30:
# #     category = "Acima do peso"
# # elif 30 <= imc < 35:
# #     category = "Obesidade I"
# # elif 35 <= imc < 40:
# #     category = "Obesidade II"
# # else:
# #     category = "Obesidade III"

# # print(f"\n{name}, com {age} anos, seu IMC é {imc:.2f} e sua categoria é '{category}'.")





# # muito_abaixo = <17
# # normal = < 18,5 <25
# # acima_do_peso = <= 25 or <30 
# # obesidade_I = <= 30 and < 40
# # obesidade_II = < 35 or <40
# # obesidade_III=  >=40 