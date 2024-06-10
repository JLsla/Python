# 5. Faça um programa para ler as 8 dezenas apostadas por 20 apostadores e verificar se a aposta é válida (cada dezena está entre [1, 80] e não pode haver repetição). O programa deverá calcular e exibir a quantidade de números acertados em cada aposta.
# Atenção! As dezenas sorteadas são: 06, 07, 13, 14 e 26.


quant_jogadores = int(input('Insira a quantia de jogadores: '))
jogadores = []
print(jogadores)

flag=0
while flag < quant_jogadores:
    numeros = []

    while len(numeros) < 8:
        a = int(input("Insira um número para apostar (os números não podem ser repetidos e devem estar entre 1 e 80): "))

        if a < 1 or a > 80:
            print("O número deve estar entre 1 e 80. Tente novamente.")
            continue
        if a in numeros:
            print("Este número já foi escolhido. Tente novamente.")
            continue
        numeros.append(a)
        
    jogadores.append(numeros)
    flag += 1

for i in jogadores:
    print(i)