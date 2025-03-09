import numpy as np

# a. Criar array de números 1 com shape (8, 2)
array_shape= np.shape((8, 2))
print(array_shape)

# b. Criar array de zeros com shape (5, 7)
array_zeros = np.zeros((5, 7))
print(array_zeros)

# c. Subtrair um array com números aleatórios
array_random = np.random.random((5, 7))
subarray = array_random - array_zeros
print(subarray)

# d. Calcular a média dos valores do subarray
print(subarray.mean())
