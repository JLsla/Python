# 5. Faça um programa que leia um número inteiro e determine se ele é par ou ímpar. Ao final, o programa deve perguntar se o usuário deseja continuar (digitar outro número) ou sair. Se o usuário quiser continuar, o programa deve repetir tudo de novo, caso contrário o programa deve ser encerrado.

continuar = 0

while True:
    num1 = int(input("Digite um número: "))
    if num1 % 2 == 0:
        print(f"{num1} é um número par")
    else:
        print(f"{num1} é um número impar")
    continuar = input("Deseja continuar? Sim ou Não: ")
    if (continuar == "não" or continuar == "nao" or continuar == "n" or continuar == "Não" or continuar == "Nao"):
        break
    else:
        print(f"Continuar, ok")