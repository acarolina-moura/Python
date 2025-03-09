"""Escreve um programa que solicite duas notas ([nota1] e [nota2]) ao utilizador e
apresente a média das mesmas da seguinte forma:
“A média das notas [nota1] e [nota2] é [média].”"""
nota1 = int(input("Digite o número1: \n"))
nota2 = int(input("Digite o número2: \n"))

def calcula_media(nota1,nota2):
    media = nota1 / nota2