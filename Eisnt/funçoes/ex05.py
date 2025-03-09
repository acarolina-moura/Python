"""5. Escreve uma função em Python que, dada uma lista de elementos, devolva 
essa mesma lista, mas sem elementos repetidos. """

def remove_repetidos(lista):
    lista_sem_repetidos = list(set(lista))
    return lista_sem_repetidos

lista = [1, 2, 2, 3, 4, 4, 5]
resultado = remove_repetidos(lista)
print(f"Primeira lista: {lista}")
print(f"Lista sem elementos repetidos: {resultado}")
