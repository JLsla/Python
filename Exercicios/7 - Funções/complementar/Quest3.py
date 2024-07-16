# 3. Escreva um programa que leia N números inteiros (máximo 20) e armazene em um vetor X. Calcule a média dos elementos do vetor e informe quantos elementos estão abaixo da média do conjunto.
# Crie as seguintes funções:
#   • Uma função que faça a leitura dos elementos de um vetor de inteiros. Essa função deve receber como parâmetro o número de elementos do vetor e deve retornar o vetor preenchido.
#   • Uma função que calcule a média dos elementos de um vetor. Essa função deve receber como parâmetro um vetor e retornar a média dos elementos dele.
#   • Uma função que receba um vetor e um número, e retorne quantos elementos do vetor estão abaixo desse número.

import random

def criacao_vetor(elementos):
    vetor = [None]*elementos
    for i in range(elementos):
        vetor[i] = random.randint(0, 10)

    return vetor

def media_vetor(vetor):
    soma = sum(vetor)
    media = soma // elementos

    return media

def abaixo_media(vetor, media):
    contador = 0
    for i in vetor:
        if i < media:
            contador += 1   

    return contador

# Main
elementos = 7
vetor = criacao_vetor(elementos)
media = media_vetor(vetor)
quant_abaixo_media = abaixo_media(vetor, media)
print(f'Para os valores dentro desse vetor {vetor}, a media deles é {media} e a quantidade de numeros abaixo da média é {quant_abaixo_media}')