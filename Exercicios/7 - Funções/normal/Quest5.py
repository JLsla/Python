# 5. Escreva um programa que leia as 3 notas de um aluno, determine e exiba a sua média e seu conceito.
# O programa deve conter as seguintes funções:
#   • Uma função que recebe como parâmetros as 3 notas do aluno e retorne a sua média (aritmética).
#   • Uma função que receba como parâmetro a média do aluno e retorne o seu conceito, de acordo com a tabela abaixo:

def media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def conceito(media):
    if media >= 8:
        return 'A'
    elif media >= 5 and media < 8:
        return 'B'
    else:
        return "C"
    
media = media(5,5,5)
conceito = conceito(media)
print(f'A média {media} te dá o conceito {conceito}')