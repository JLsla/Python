# 4. Escreva um programa que leia a hora de início de um jogo e a hora do final do jogo (considerando apenas horas inteiras), calcula a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte. O programa deve mostrar o resultado obtido.

hora_comeco = int(input("Digite a hora em que o jogo de 0 a 23 começou: "))
hora_acabou = int(input("Digite a hora de em que o jogo de 0 a 23 acabou: "))



if (hora_comeco<hora_acabou):
    subtracao = hora_acabou - hora_comeco
    print(f"O jogo durou {subtracao} horas")

else:
    subtracao = 24 - hora_comeco
    soma_final = subtracao + hora_acabou
    print(f"O jogo durou {soma_final} horas")


