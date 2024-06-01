# 3. Escreva um programa que leia um vetor V contendo N elementos inteiros (N será lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver, informe em que posição (índice).
#Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K aparece.

ocorrencias = 0

n = int(input("digite um número para n representa-lo: "))
k = int(input("digite um número para k representa-lo: "))
v = [None]*n
for i in range (n):
    v[i] = int(input("digite um número para representar cada número do vetor: "))

for i in range (n):
    if (v[i]==k):
        print(f"K aparece em {i}")