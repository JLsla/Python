# Faça um programa que calcule e mostre o fatorial de um número N, fornecido pelo usuário. A definição de fatorial é mostrada a seguir:
# N ! = 1 x 2 x 3 x ... x N-1 x N
# 0 ! = 1

num1 = int(input("digite um número : "))

mult = 1

for i in range (num1, 1, -1):
    mult *= i 

print(mult)