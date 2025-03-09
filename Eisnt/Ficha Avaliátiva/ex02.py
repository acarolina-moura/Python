# 2. Escreve um programa que faça a conversão para kms, de um dado valor em metros.

dist_metros = float(input("Digite a distância percorrida em metros: \n"))
dist_km = dist_metros / 1000

print(f"A distância percorrida em quilômetros é {dist_km:.2f} km")