# 8. Faça um programa que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).

nome = input('Qual seria o nome do aluno: ')

nota = float(input('Qual a primeira nota: '))

nota2 = float(input('Qual a segunda nota: '))

nota3 = float(input('Qual a terceira nota: '))

media = (nota+nota2+nota3) /3

print(f"a nota do aluno {nome} é igual {media:.2f}")