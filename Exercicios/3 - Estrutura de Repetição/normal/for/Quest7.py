# 7. Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Faça um programa que leia um número e determine se ele é ou não primo.

num1 = int(input("Digite um número: "))
resto = 0

for num in range (1, num1 + 1, 1):
    if (num1 % num == 0):
        resto+=1
        
if (resto == 2):
    print(f"O número {num1} é primo")
else:
    print(f"O número não é primo")
