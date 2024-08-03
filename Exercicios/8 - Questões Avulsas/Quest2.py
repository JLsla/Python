# Classificação de Números em Lista: Escreva uma função classifica_numeros que receba uma lista de números inteiros e retorne uma tupla com três elementos: a quantidade de números pares na lista, a quantidade de números ímpares na lista e a soma de todos os números na lista.
def classifica_numeros(numero):
    par = 0
    impar = 0
    retorno = ()
    soma = 0
    for i in numero:
        if i % 2 == 0:
            par += 1
        else:
            impar += 1
        soma += i
    retorno += (par, ) 
    retorno += (impar, )
    retorno += (soma, )
    return retorno

# Main
lista_números = [5,13,12,2,8]
print(classifica_numeros(lista_números))