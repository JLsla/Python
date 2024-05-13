# 1. Escreva um programa que leia um número inteiro e determine se ele é par ou ímpar.

num1 = int(input("digite um número: "))

if (num1 % 2 == 0):
    print(f"{num1} é um número par ")
else:
    print(f"{num1} é um número ímpar")
