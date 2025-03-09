"""Crie um programa para controlar listas, com as seguintes funções:"""

#Adicionar elemento no início; 
frutas = ["abacate", "banana", "maçã", "uva", "pera"]
frutas.insert(0, "laranja")
print(frutas)

# Adicionar elemento no fim;
supermercado = ["arroz", "feijao", "cafe", "azeite", "ovos"]
supermercado.append("massa")
print(supermercado)

# Remover elemento; 
roupas = ["casaco", "sapatilhas", "calças", "botas"]
roupas.pop(2)
print(roupas)

# Tamanho da lista;
carros = ["fiat", "wolkswagen", "bmw"]
print(len(carros))

# Imprimir elementos da lista;

for x in carros:
    print(x)
 

#Esvaziar lista;

sabores = ["chocolate", "morango", "uva", "limão"]
sabores.clear()
print(sabores)
