import time

"""
P1 = Velocidade aumenta e diminui Vel1 Vel2 Vel1
P2 = Velocidade aumenta 2x e diminui  Vel1 Vel2 Vel3 Vel2 Vel1
P3 = Velocidade alternada V1 V2 V3 V2 V3 V2 V1
P4 = Distância - Quando chegar na distância máxima, a corrida acaba
"""
#vel1 = vel2 = vel3 = tempo = None
def P1():
    global vel1
    global vel2
    global tempo 
    
    vel2 = int(input('Velocidade Máxima: '))
    tempo = int(input('Insira o tempo em minutos: '))

    vel1 = (vel2/2) + (vel2/3)

    print(f'v1{vel1}')
    print(f'Iniciando v{vel2} por {tempo}m')

P1()