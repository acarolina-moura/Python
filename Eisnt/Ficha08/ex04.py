"""4. Considera a seguinte lista:
nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]
Efetua um programa em python que:
a. Imprima a quantidade de inteiros, floats, strings e boleanos na lista;
b. Efetua a média de todos os valores inteiros na lista.
c. Crie e retorne uma nova lista só com os valores inteiros"""

nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]


inteiros = 0
floats = 0
strings = 0
booleanos = 0

soma = 0
arr_int= []

for x in nums:
    if type(x)== int:
        inteiros+= 1
        soma+= x
        arr_int.append(x)
    elif type(x)== float:
        floats+=1
    elif type(x)== str:
        strings+=1
    elif type(x)== bool:
        booleanos+= 1
    
print("Existem", inteiros, "inteiros")
print("Existem", floats, "floats")
print("Existem", strings, "strings")
print("Existem", booleanos, "booleanos")
print("A média é: ", soma)
print("Os inteiros são:", arr_int)

