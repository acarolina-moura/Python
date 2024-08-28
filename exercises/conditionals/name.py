
name = input ('Whats is your name?\n')

def welcome (name: str) -> str:  
    print(f'Hello, {name.upper()}!')

    return name

print(welcome(name))