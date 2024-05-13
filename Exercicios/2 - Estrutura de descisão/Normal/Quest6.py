# 6. Recomendam-se estudantes para bolsas de estudo em função de seu desempenho. A natureza das recomendações é baseada na seguinte tabela:                                           A = Fortemente recomendado \\ B ou C = Recomendado \\ D = Não recomendado                                                                                                       Escreva um programa que leia o nome e o conceito de um estudante e exiba o nome do estudante e sua respectiva recomendação.

nome = input("Digite o nome do estudante: ")
conceioto = input("Digite a letra que esse estudante se encaixa: ").upper()

if conceioto == "A":
    print(f"O estudante {nome} é fortemente recomendado")

elif conceioto == "B" or conceioto == "C":
    print(f"O estudante {nome} é recomendado")

elif conceioto == "D":
    print(f"O estudante {nome} não é recomendado")

else:
    print(f"{conceioto} é uma letra inválida, escreva uma letra válida como A, B, C ou E")

