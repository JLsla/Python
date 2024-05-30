# 2. Faça um programa que leia vários números, calcule e exiba a média desses números.
# Obs: a leitura do número 999 indica o fim dos dados de entrada e não deve ser computado na média)

flag = 0
soma = 0
while True:
    num1 = int(input("Digite um número: "))
    if num1 == 999:
        break
    soma += num1
    flag += 1

media = soma / flag
print(media)