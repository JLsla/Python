# 4. Faça um programa que leia 20 números inteiros, determine e mostre o maior deles.

maior = 0

for i in range (1, 6, 1):
    num1 = int(input("digite um número : "))
    if (num1 >= maior):
        print("oi")
        maior = num1
print(maior)
