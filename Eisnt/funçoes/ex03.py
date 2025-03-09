"""3. Escreve uma função em Python que dada uma lista de números imprime a soma 
dos valores dessa lista, o número de elementos da lista e a media desses 
valores. """

lista = [10,15,20]

def calcula_valores_lista(lista):
    soma = sum(lista)
    numero_elementos = len(lista)
    media = soma  / numero_elementos
    return soma , numero_elementos,  media
    
soma, numero_elementos, media = calcula_valores_lista(lista)

print(f"Soma dos valores: {soma}")
print(f"Número de elementos: {numero_elementos}")
print(f"Média dos valores: {media:.2f}")