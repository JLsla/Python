# 1. Escreva um programa que leia um vetor contendo N elementos inteiros (N será lido), calcule e exiba:
# • A quantidade de elementos pares;
# • A quantidade de elementos ímpares;
# • A soma de todos os elementos;
# • A média dos elementos do vetor.

soma = 0
impar = 0
pares = 0
n = int(input("Digite um número equivalente a N: "))
v = [None]*n
for i in range (n):
    v[i] = int(input("Digite um número equivalente ao espaço do vetor: "))

for i in range (n):
    if v[i] % 2 == 0:
        pares += 1
    else:
        impar += 1
    soma += v[i]
media = soma // n
print(f"Quantia de pares {pares}")
print(f"Quantia de impares {impar}")
print(f"Soma de todos os elementos {soma}")
print(f"Média de todos os elementos {media}")
