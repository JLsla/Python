# 2. Dados dois vetores A e B contendo N elementos inteiros cada (N, A e B serão lidos), gerar e exibir um vetor C (de tamanho N*2) cujos elementos sejam a intercalação dos elementos de A e B.
# Ex: N = 3, A = [18, 12, 20], B = [15, 10, 7], C = [18, 15, 12, 10, 20, 7]

n = int(input("Digite um número equivalente a N: "))

a = [18, 12, 20]
b = [15, 10, 7]
c = [None]*(n*2)

# for i in range (n):
#     a[i] = int(input("Digite um número equivalente ao espaço do vetor a: "))

# for i in range (n):
#     b[i] = int(input("Digite um número equivalente ao espaço do vetor b: "))

for i in range (n):
    c[i * 2] = a[i]
    c[i * 2 + 1] = b[i]

print(c)