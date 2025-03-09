""" Dentro deste ficheiro escreve um programa que receba, como parâmetro um inteiro, e
 devolva o se dobro."""


n = int(input("Digite um número: "))

def recebe_int(n):
    if n < 0:
        print("Digite um número maior do que Zero")
    return n * 2

result = recebe_int(n)
print ("O dobro de %d é %d " % ( n , result))
     


