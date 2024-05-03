# 4. Um motorista anota a marcação do hodômetro do seu veículo antes e após uma viagem, bem como o número de litros de combustível gastos.                                                                                                    Escreva um programa que leia os 3 dados acima, o preço do litro de combustível, a               capacidade do tanque e mostre:                                                                                                   a) Quilometragem rodada.                                                                                                   b) Quantos quilômetros por litro faz o veículo.                                                         c) Autonomia do veículo.                                                                                d) Custo da viagem.

hodometro_antes = float(input(' Qual a marcação do seu hodometro (em km) antes da viagem? '))
hodometro_apos = float(input(' Qual a marcação do seu hodometro (em km) depois da viagem? '))
litros_gastos = float(input('Quantos litros de combustível foram gastos na viajem?'))
preco_gasolina = float(input('Quanto custa a gasolina onde você pretende comprar? '))

km_rodados = hodometro_antes-hodometro_apos
km_por_litro = km_rodados/litros_gastos


