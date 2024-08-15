# Else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
  
# If the Loops Break the else keyword its not execute
for x in range(10):
    print(x)
    if x == 8: break
else:
    print("You can")
