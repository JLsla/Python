# 4. Escreva um programa que abra um arquivo texto e o exiba na tela com todas as suas linhas numeradas sequencialmente.
from geradorDeArquivos import geradorDeArquivos
nomeArquivo = "test4"
arq = geradorDeArquivos(nomeArquivo, "w")
arq.write("Primeira linha do arquivo\n")
arq.write("Segunda linha do arquivo\n")
arq.write("Terceira linha do arquivo\n")
arq.write("Quarta linha do arquivo\n")
arq.write("Quinta linha do arquivo\n")
arq.close()


arq = geradorDeArquivos(nomeArquivo, "r")
texto = arq.read()
arq.close()

texto = texto.split("\n")

for i in range (1, len(texto)):
    print (i, "-", texto[i])
    
