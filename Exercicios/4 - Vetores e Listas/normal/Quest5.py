# 5. Escreva um programa que receba um vetor V de N números inteiros (N será lido), determine e exiba o maior e o menor elemento deste vetor e seus respectivos índices. Obs: suponha a inexistência de valores repetidos.
menor = [9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999, 0]
maior = [0, 0]
n = int(input(f"Digite um número para representar N: "))
v = [None]*n

for i in range(n):
    v[i] = int(input(f"Digite um número para representar os números do vetor: "))
    

for i in range (n):
    if (v[i] >= maior[0] ):
        maior[0] = v[i] 
        maior[1] = i
print(maior)

for i in range (n): 
    if (v[i] <= menor[0] ):
        menor[0] = v[i]
        menor[1] = i
print(menor)



