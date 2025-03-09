#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression.


def myfunc(n):
  return lambda a, b : a * b * n 

mydoubler = myfunc(2)

print(mydoubler(5))