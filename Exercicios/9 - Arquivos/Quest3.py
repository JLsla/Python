# 3. Escreva um programa que leia do teclado o nome de um arquivo de texto e uma string, abra o arquivo e inclua no final dele a string lida.
from geradorDeArquivos import geradorDeArquivos

nomearquivo = input(": ")

arq = geradorDeArquivos(nomearquivo, "a")
arq.write("gsfgdsgsgssfsfsgagass.")
arq.close()



