# 1. Escreva um programa que exiba na tela um arquivo de texto cujo nome será lido pelo teclado.
from geradorDeArquivos import geradorDeArquivos

nomeArquivo = input(": ")
arq = geradorDeArquivos(nomeArquivo, 'w')