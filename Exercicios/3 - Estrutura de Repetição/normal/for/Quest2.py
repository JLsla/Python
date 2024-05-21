# 2. Faça um programa que leia um número N, inteiro, e some todos os números de 1 até N, mostrando o resultado.

num1 = int(input("digite um número : "))

soma = 0

for i in range (1, num1 + 1, 1):
    soma += i

print(soma)