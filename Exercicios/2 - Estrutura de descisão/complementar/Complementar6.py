# 6. Na primeira etapa de um concurso, o candidato tem que fazer duas provas. Dessas duas notas é tirada a média do candidato. Caso essa média seja maior ou igual a 7.0, ele estará apto a fazer a segunda etapa do concurso. Na segunda etapa, ele fará mais uma prova, onde deverá obter uma nota maior ou igual a 8.0 para ser aprovado no concurso.
# Escreva um programa que leia as notas da primeira etapa, calcule a média da primeira etapa, e se o candidato for aprovado na primeira etapa, leia a nota dele na segunda etapa e diga se ele foi aprovado ou não no concurso.

num1= float(input("Digite o primeiro número da média: "))
num2 = float(input("Digite o segundo número da média: "))

if ((num1 + num2) / 2 <= 6.99):
    print(f"O candidato não foi aprovado")

else:
    print(f"O aluno está apto a a fazer a segunda etapa do concurso")

    num3 = float(input("Digite a nota da terceira prova aqui: "))
    
    if (num3 <= 7.99):
        print(f"O aluno foi reprovado na segunda fase")
    else:
        print(f"O aluno foi aprovado na segunda fase")

