# Faça um programa que, para um grupo de N pessoas (obs: N será lido):
# • Leia o sexo (M ou F) de cada pessoa;
# • Calcule e escreva o percentual de homens;
# • Calcule e escreva o percentual de mulheres.

todos = 0
mulher = 0
homem = 0 

num1 = int(input("digite o número total de pesssoas: "))

for i in range (1, num1 + 1, 1):
    homem1 = input("Qual o sexo da pessoa?: ").lower()
    if (homem1 == "masculino" or homem1 == "m" or homem1 == "homem"):
        homem += 1
    elif (homem1 == "feminino" or homem1 == "f" or homem1 == "mulher"):
        mulher += 1
    else:
        print(f"Esse sexo não existe, por favor digite um existente como M ou masculino ou F ou femimino")
todos = homem + mulher  
    
homem_porc = (homem / todos) * 100
mulher_porc = (mulher / todos) * 100
print(f" a porcentagem de homens é de {homem_porc} e a porcentagem de mulheres é de {mulher_porc}")
