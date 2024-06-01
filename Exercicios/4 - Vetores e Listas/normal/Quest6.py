# 6. Escreva um programa que leia um vetor de N números inteiros (N será lido), inverta a ordem dos elementos do vetor e exiba o vetor invertido.
# Ex: V = [1, 3, 5, 7], após a inversão: V = [7, 5, 3, 1].
# Obs: É necessário inverter os elementos do vetor, não basta imprimi-los em ordem inversa!

n = int(input(f"Digite um número para representar N: "))

b = [None]*n
v = [None]*n

for i in range (n):
    v[i] = int(input(f"Digite um número para representar os números do vetor: "))

for i in range (n-1,  -1, -1):
    b[(i - (n-1)) * (-1)] = v [i]

print(b)