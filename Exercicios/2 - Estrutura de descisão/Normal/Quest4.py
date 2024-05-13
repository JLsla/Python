# 4. Escreva um programa que leia o nome e o sexo (M ou F) de uma pessoa e exiba a mensagem "Olá, Sr. Fulano!" ou "Olá, Sra. Fulana!", de acordo com o sexo da pessoa. Obs: Fulano e Fulana são nomes exemplos.

while True:
    nome = input("digite um nome: ")
    sexo = input("epecifique o sexo que essa pessoa se identifica: ").lower()
    if (sexo == "masculino" or sexo == "m"): 
        print(f"Olá, Sr.{nome}")
    elif (sexo == "feminino" or sexo == "f"):
        print(f"Olá, Sra.{nome}")
    else:
        print("Por favor digite um sexo existente")