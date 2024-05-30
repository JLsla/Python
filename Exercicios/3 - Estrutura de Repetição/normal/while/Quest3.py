# 3. Faça um programa que leia vários números, determine e mostre o maior e o menor deles.
# Obs: a leitura do número 0 (zero) encerra o programa.

menor = 99999999999999999999999999999999999999
maior = 0
num1 = 1
while True:
    num1 = int(input("me de um número: "))
    if (num1 == 0):
        break
    if (num1 > maior):
        maior=num1
    elif (num1 < menor):
        menor = num1
print(maior, menor)