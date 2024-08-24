# 2. Escreva um programa que copie um arquivo texto (cujo nome será lido pelo teclado) para um novo arquivo chamado COPIA.TXT, porém substituindo todos os brancos contidos no arquivo pelo ponto.

nomeArquivo = input(": ")
arq = open(f"Exercicios/9 - Arquivos/arquivos/{nomeArquivo}.txt", 'w')
arq.write("is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
arq.close()

arq = open(f"Exercicios/9 - Arquivos/arquivos/{nomeArquivo}.txt", 'r')
texto = arq.read()
arq.close()

texto_com_pontos = texto.replace(" ", ".")

arq = open("Exercicios/9 - Arquivos/arquivos/copia.txt", 'w')
arq.write(texto_com_pontos)
arq.close()