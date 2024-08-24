# 1. Escreva um programa que exiba na tela um arquivo de texto cujo nome será lido pelo teclado.

nomeArquivo = input(": ")
arq = open(f"Exercicios/9 - Arquivos/arquivos/{nomeArquivo}.txt", 'w')
