    
my_list = [20, 85, 26, 32, 89, 65]   
    
def odd_nums(my_list):
  for item in my_list:
    if item % 2 == 1:
        print(item, "Odd number")
    elif item % 2 == 0:
        print(item, "Even number")
      
print(odd_nums(my_list))