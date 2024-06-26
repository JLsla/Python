# 3. Escreva um programa que gere aleatoriamente uma matriz quadrada A (cuja ordem será lida) e gere uma matriz B (da mesma ordem de A), onde cada elemento de B corresponderá ao respectivo elemento de A somado a ele os seus índices, sendo que se o elemento for de alguma diagonal (principal ou secundária) deverá ser colocado 0 (zero).


import random

ncolunas = 3  
nlinhas = 3
Amatriz = [[None]*ncolunas for i in range (nlinhas)]
Bmatriz = [[None]*ncolunas for i in range (nlinhas)]

for i in range (nlinhas):
    for j in range (ncolunas):
        Amatriz[i][j] = random.randint(0,9)
        Bmatriz[i][j] = Amatriz[i][j] + (i + j) 

for i in range (nlinhas):
    for j in range (ncolunas):
        if i + j == nlinhas - 1 or i == j:
            Bmatriz[i][j] = 0


for i in range (nlinhas):
    for j in range (ncolunas):
        print(f'{Amatriz[i][j]:4}', end='')        
    print()

print()

for i in range (nlinhas):
    for j in range (ncolunas):
        print(f'{Bmatriz[i][j]:4}', end='')    
    print()
