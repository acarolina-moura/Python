"""Implemente uma calculadora simples com as operações aritméticas básicas. O utilizador
deverá especificar a operação desejada (+,-,*,/) e, em seguida, inserir dois valores.
Caso, o utilizador escolha divisão e insira como valor do denominar 0 mostra uma
mensagem personalizada. Para os restantes casos, mostra no ecrã o resultado da
operação desejada."""

print("Escolha a operação desejada: +, -, *, /")
operacao = input("Digite a operação: ")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))


if operacao == '+':
    resultado = valor1 + valor2
    print(f"O resultado é: {valor1} + {valor2}")
elif operacao == '-':
    resultado = valor1 - valor2
    print("O resultado é:")
elif operacao == '*':
    resultado = valor1 * valor2
    print("O resultado é:")
elif operacao == '/':
    resultado = valor1 / valor2
    print(f"O resultado de {valor1} {operacao} {valor2} é: {resultado:.2f}")
else:
    print(f"O valor é inválido")


