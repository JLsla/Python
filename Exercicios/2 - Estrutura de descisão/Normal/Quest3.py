# 3. Escreva um programa que leia 3 números inteiros, determine e mostre o maior deles.

num1 = float(input("digite um número: "))
num2 = float(input("digite outro número: "))
num3 = float(input("digite um terceiro número: "))

if (num1 < num2 > num3):
    print(f"{num2} é o maior número entre {num1} {num2} e {num3}")

elif (num1 < num3 > num2):
    print(f"{num3} é o maior número entre {num1} {num2} e {num3 }")

else:
    print(f"{num1} é o maior número entre {num1} {num2} e {num3}")
