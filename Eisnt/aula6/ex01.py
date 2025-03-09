# Receba nome e preço e retorna preço total

produto = str(input('Digite o aparelho: '))
valor = int(input('Digite o valor do aparelho:'))
match produto:
        case "smartphone":
            desconto = 0.1
            print(f"O valor final do {produto} com desconto é: {valor - desconto * 100}")
        case "tablet":
            desconto = 0.1
            print(f"O valor final do {produto} com desconto é: {valor - desconto * 100}") 
        case "laptop":
            desconto = 0.2
            print(f"O valor final do {produto} com desconto é: {valor - desconto * 100}")  
        case _:
            desconto = 0.05
            print(f"O valor final do {produto} com desconto é: {valor - desconto * 100}") 
        
        
        