# 2. Escreva um programa que leia dois números e exiba-os em ordem crescente.

num1 = float(input("digite um número: "))
num2 = float(input("digite outro número: "))

if (num1 < num2):
    print(f"{num1} {num2}")
else:
    print(f"{num2} {num1}")