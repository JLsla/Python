# 1. Escreva um programa que leia um vetor A de N números inteiros (N será lido) e um outro inteiro K, construa e exiba um outro vetor B cujos elementos são os respectivos elementos de a multiplicados por K.
# Ex: A = [1,2,3], K = 5, B = [5,10,15].

n = int(input("Digite um número equivalente ao espaço do vetor: "))

a = [None]*n
for i in range (n):
    a[i] = int(input("Digite um número: "))
k = 5
b = [None]*n
for e in range (n):
    b[e]= a[e] * k

print(b, a)
    