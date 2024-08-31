# 2. Escreva um programa que copie um arquivo texto (cujo nome será lido pelo teclado) para um novo arquivo chamado COPIA.TXT, porém substituindo todos os brancos contidos no arquivo pelo ponto.
from geradorDeArquivos import geradorDeArquivos

# Nome do Arquivo
nomeArquivo = input(": ")

# Abrindo o arquivo com função
arq = geradorDeArquivos(nomeArquivo, "w")
arq.write("is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
arq.close()

# Lendo o Arquivo
arq = geradorDeArquivos(nomeArquivo, "r")
texto = arq.read()
arq.close()

texto_com_pontos = texto.replace(" ", ".")

# Recriando arquivo com pontos no lugar dos espaços
arq = geradorDeArquivos(nomeArquivo, "w")
arq.write(texto_com_pontos)
arq.close()