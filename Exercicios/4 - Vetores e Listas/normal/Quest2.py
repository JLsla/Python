# 2. Escreva um programa que leia um vetor V (contendo 8 inteiros) e um valor inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.

ocorrencias = 0
v = [None]*8
k = int(input("Digite um número para ser o valor da variavel K: "))

for i in range (8):
    v[i] = int(input("Digite um número para ser o valor de cada número do vetor: "))

for i in v:
    if (v[i] == k):
        ocorrencias += 1
        
print(f"{ocorrencias}")   