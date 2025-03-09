# 1. Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, mês e ano para três variáveis inteiras. 

data = "15/01/2025"
dia, mes, ano = data.split('/')
print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")
