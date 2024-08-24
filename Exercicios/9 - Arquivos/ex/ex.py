# arq = open("Exercicios/9 - Arquivos/arquivo.txt", 'w')
# arq.write('Primeira Linha\nSegunda Linha\nTerceira Linha\n')
# arq.close

# arq = open("Exercicios/9 - Arquivos/arquivo.txt", 'a')
# arq.write('Nova Linha\n')
# arq.close

arq = open("Exercicios/9 - Arquivos/arquivo.txt", 'r')
# caracteres = arq.read()

todesLinhas = arq.readlines()
linha = arq.readline()
arq.close

# print(linha)
# print(todesLinhas)
# print(caracteres)

arq = open("Exercicios/9 - Arquivos/arquivo.txt", 'r')
linha = arq.readline()
while linha:
	print(linha, end='')
	linha = arq.readline()
arq.close()
