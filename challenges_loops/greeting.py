# 1 - Define the function to accept a list of strings as a single parameter called names
# 2 - Create a new list of strings
# 3 - Loop through each name in names
# 4 - Within the loop, concatenate 'Hello, 
# ' and the current name together and append this new string to the new list of strin
# 5 - Afterwards, return the new list of strings

def add_greetings(names):
    new_list = []
    for name in names:
        new_list.append ("Hello, " + name)
    return new_list

print(add_greetings(["Owen", "Max", "Sophie"]))