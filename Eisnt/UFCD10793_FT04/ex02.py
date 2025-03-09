"""Implemente um programa que, dada uma letra (S, C ou V), indique o estado civil de 
uma pessoa."""

estado_civil = str(input("Indique seu estado civil: \n")).upper()

match estado_civil:
    case "S":
        print("SOLTEIRO")
    case "C":
        print("CASADO")
    case "V":
        print("VIÚVO")