"""Faz um programa que receba a distância em km e a quantidade em litros de
 combustível consumido por um carro num percurso. Calcula o consumo km/l e escreve
 uma mensagem de acordo com o resultado obtido. (deverá ser criado o ficheiro
 ex07.py)."""
 
dist_km = float(input("Digite quantos km percorridos: \n"))
combustivel = float(input("Digite o valor do combustível gasto: \n"))

def comb_gasto_km(dist_km,combustivel):
    gasto_percurso = dist_km / combustivel
    return gasto_percurso

result = comb_gasto_km(dist_km,combustivel)
print("Neste percurso gastou %.2f km por litro" % result)