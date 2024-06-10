# 3. Escreva um programa para ler 6 números. Após a leitura dos números, verifique, para cada um deles, se é distinto, ou seja, não possui repetição.

# [1, 2, 3, 6, 6, 1]
#  0  1  2  3  4  5

distintos = []
n = 6

a = [None]*n

for i in range (n):
    a[i] = int(input("Digite um número: "))

for i in range(n):
    for j in range(n):
        if j == i:
            continue
        if a[j] == a[i]:
            distintos.append(a[i])
print(distintos)