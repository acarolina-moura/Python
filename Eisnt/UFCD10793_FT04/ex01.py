"""Faz um programa que escreva o nome do mês que é introduzido, pelo utilizador, na 
forma numérica. """

mes = str(input("Escreva o mês: \n")).upper()

match mes:
    case "JANEIRO":
        print(1)
    case "FEVEREIRO":
        print(2)
    case "MARÇO":
        print(3)
    case "ABRIL":
        print(4)
    case "MAIO":
        print(5)
    case "JUNHO":
        print(6)
    case "JULHO":
        print(7)
    case "AGOSTO":
        print(8)
    case "SETEMBRO":
        print(9)
    case "OUTUBRO":
        print(10)
    case "NOVEMBRO":
        print(11)
    case "DEZEMBRO":
        print(12)
    case _:
        print("Verifique a palavra digitada")
        