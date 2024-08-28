# Recusior has two steps

# Recursive step:

# The line of code under the else statement is the recursive step
# because it calls the function factorial().

def factorial(num):
   if num == 1:
       return 1
   else:
       return num * factorial(num-1)
   # retorna o numero e o fatorial do seu antecessor
print(factorial((10)))
   
# Base step:



