# FUNCTION SOMA

def soma(a, b):
    a += 1

    return a + b
  
 #USANDO A FUNÃO SOMA
print("This is first TEST:")
print(soma(5,2))  


# PYTHON TEM TIPAGEM DINÂMICA OU SEJA, PODEMOS DECLARAR VARIÁVEL COM UM TIPO

def testeSoma(a:int, b:int) -> int:

    return a + b
print("This is second TEST:")
print(testeSoma(5,10))