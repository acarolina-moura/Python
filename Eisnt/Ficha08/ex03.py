"""3. Considera a lista
idades=[25, 15, 19, 22, 37, 78, 46, 2, 67]
Cria um programa, em python, que:
a. Indique quantas pessoas são menores de idade
b. Ordene a lista por ordem decrescente
c. Pede ao utilizador uma idade e verifica se essa idade está na lista.
#- Se estiver faz print("A idade está na lista")
#- Caso contrário faz o print("não existe ninguém com essa idade na lista")"""

idades=[25, 15, 19, 22, 37, 78, 46, 2, 67]

# LETRA A
soma = 0

for i in idades:
    if i < 18:
        soma+= 1
print("O número de pessoas menor de idade é: ", soma)
        
# LETRA B

idades.sort(reverse=True)
print(idades)

# LETRA C

idade = int(input("Escreva uma idade: \n"))

if idade in idades:
    print("A idade está na lista")
else: 
    print("A idade não está na lista")