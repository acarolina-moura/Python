lista_alimentos = ["arroz", "feijão", "macarrão"]
produto = input("Digite um produto: ").strip()

if produto in lista_alimentos:
    print(f"Este produto {produto} existe na lista")
else:
    print(f"Este produto {produto} não existe na lista")