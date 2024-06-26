# 2. Escreva um programa que:
# • Leia (ou gere aleatoriamente) uma matriz quadrada de ordem N contendo elementos inteiros (N será lido);
# • Exiba a matriz lida (no formato de matriz);
# • Exiba os elementos da diagonal principal, isto é, os elementos onde I = J.

import random
principal = []
ncolunas = 3
nlinhas = 3
Amatriz = [[None]*ncolunas for i in range (nlinhas)]

for i in range (nlinhas):
    for j in range (ncolunas):
        Amatriz[i][j] = random.randint(0,9)

for i in range (nlinhas):
    for j in range (ncolunas):
        print(f'{Amatriz[i][j]:4}', end='')
        if i == j:
            principal.append(Amatriz[i][j])         
    print()

print (principal)    
   