# 4. Faça um programa que leia os seguintes dados de um conjunto de alunos: matrícula, nome e as duas notas que ele obteve em suas avaliações. A condição de parada será a digitação de uma matrícula igual 0 (zero). O programa deverá mostrar, para cada aluno, as seguintes informações: matrícula, nome, média e situação (aprovado, se a média for igual ou superior a 7 e, reprovado, se a média for inferior a 7).


matricula = 1
nota = 0
nota2 = 0
soma = nota + nota2

while (matricula == 0):
    matricula = input("Qual o número da matricula: ")
    nome = input("Qual o nome do aluno: ")
    nota = float(input("me de a nota: "))
    nota2 = float(input("me de a segunda nota: "))
    if (soma <= 7):
        print(f"O aluno(a) {nome} foi aprovado com a nota {soma}")
    else: 
        print(f"O aluno(a) {nome} foi reprovado ficou com {soma}")