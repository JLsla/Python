# Escreva um programa que leia do teclado o nome de um arquivo texto e uma string, abra o arquivo e inclua no início dele a string lida.
from geradorDeArquivos import geradorDeArquivos

# Nome do Arquivo
nomeArquivo = "test5"
arq = geradorDeArquivos(nomeArquivo, "w")

arq.write ("nsdgnsdjgsdgosjgoisg")
arq.close()


