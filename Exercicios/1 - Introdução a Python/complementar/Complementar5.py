# 5. Escreva um programa que, dado um número inteiro representando uma quantidade de segundos, calcule quantas horas, minutos e segundos estão contidos nesta quantidade. Ex: 7.388 segundos = 2 horas, 3 minutos e 8 segundos.

segundos = float(input("Digite uma quantidade de segundos: "))
horas = segundos // 3600 # 1 hora igual a 3600 segundos
minutos = (segundos % 3600) // 60 
segundos_restantes = segundos % 60
print(f" A quantidade de {segundos} convertidos em horas e minutos é igual a {horas} horas {minutos} minutos {segundos_restantes} segundos")

