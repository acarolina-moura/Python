teste = [35,69,68,0,1,200]

# Ascendente
def sort_asc(teste):
   
    teste.sort(reverse=True)
    return teste

# Descendente
def sort_desc(teste):
   
    teste.sort(reverse=False)
    return teste


print(sort_asc(teste))
print(sort_desc(teste))