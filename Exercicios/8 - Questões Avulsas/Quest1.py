# Contagem de Caracteres Específicos: Escreva uma função conta_caracteres que receba uma string e um caractere como parâmetros e retorne quantas vezes o caractere aparece na string.

def conta_caracteres (frase,caracter, contador):
    frase = frase.split()
    for palavra in frase:
        if caracter in palavra:
            contador += 1
    return contador

frase = "Contagem de Caracteres Específicos: Escreva uma função conta_caracteres que receba uma string e um caractere como parâmetros e retorne quantas vezes o caractere aparece na string."
caracter = "ar"
contador = 0
print(conta_caracteres(frase, caracter, contador))