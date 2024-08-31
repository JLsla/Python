# 6. Escreva um programa que crie um arquivo texto resultante da concatenação de dois outros arquivos.

from geradorDeArquivos import geradorDeArquivos

# Nome do Arquivo
AnomeArquivo = "test6"
BnomeArquivo = "test6.5"
CnomeArquivo = "test6.6"

arq = geradorDeArquivos(AnomeArquivo, "w")
arq.write("asfoiajhofijhaofhoahfha")
arq.close()
arq = geradorDeArquivos(BnomeArquivo, "w")
arq.write("exto_com_pontos")
arq.close()

arq = geradorDeArquivos(AnomeArquivo, "r")
a = arq.read()
arq.close()

arq = geradorDeArquivos(BnomeArquivo, "r")
b = arq.read()
arq.close()

c = a + b

arq = geradorDeArquivos(CnomeArquivo, "w")
arq.write(f"{c}")
arq.close()