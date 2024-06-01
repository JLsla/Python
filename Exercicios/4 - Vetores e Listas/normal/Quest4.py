# Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
#• Os números que estão nos índices pares; 
#• Os números que estão nos índices ímpares.

sla = 0
n= 10
numero = [None]*n

# Preenchendo o Vetor
for i in range(n):
    numero[i] = int(input(f"Digite um número: "))

# Mostrando os elementos que estão em índices pares
print('Os elementos que estão nos índices pares são: ', end='')
for i in range (n):
    if (i % 2 == 0):
        print(f'{numero[i]} ', end='')

print()

# Mostrando os elementos que estão em índices ímpares
print('Os elementos que estão nos índices ímpares são: ', end='')
for i in range (n):
    if (i % 3 == 0):
        print(f'{numero[i]} ', end='')