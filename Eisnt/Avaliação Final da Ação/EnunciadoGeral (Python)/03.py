# 3. Escreve uma função em Python que dada uma lista de números imprime a soma dos 
# valores dessa lista, o número de elementos da lista e a media desses valores. Implementa 
# tratamento de exceções no teu código (try…except…else..finally). 

def calcular_lista(lista):
    soma = sum(lista)
    quantidade = len(lista)
    media = soma / quantidade
    print(f"Soma: {soma}, Quantidade: {quantidade}, Média: {media}")

numeros = [1, 2, 3, 4, 5]
calcular_lista(numeros)
