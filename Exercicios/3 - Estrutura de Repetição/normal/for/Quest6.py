# Faça um programa que leia 3 números inteiros (N, X, Y) e mostre todos os números múltiplos de N entre X e Y.

n = int(input("digite um primeiro: "))
x = int(input("digite um segundo: "))
y = int(input("digite um terceiro número: "))

multiplo = 0

for i in range (x, y + 1, 1):
    print(i * n)    