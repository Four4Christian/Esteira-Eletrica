import time

"""
P1 = Velocidade aumenta e diminui Vel1 Vel2 Vel1
P2 = Velocidade aumenta 2x e diminui  Vel1 Vel2 Vel3 Vel2 Vel1
P3 = Velocidade alternada V1 V2 V3 V2 V3 V2 V1
P4 = Distância - Quando chegar na distância máxima, a corrida acaba
"""
vel1 = vel2 = velmax = tempo = None


def inicial():
    m = int(input('Selecione o módulo: \n(1)P1 (2)P2 (3)P3 (4)P4 \n> '))

    if m == 1:
        P1()
    elif m == 2:
        P2()
    elif m == 3:
        P3()
    elif m == 4:
        P4()
    else:
        print(f'Opção Inválida "{m}"')
        inicial()

def consVel():
    global velmax
    try:
        velmax = float(input('Insira Velocidade Máxima: '))
        if velmax > 10:
            velmax = 10
    except ValueError:
        print('Apenas Números')
        consVel
        

def P1():
    global vel1
    global velmax
    global tempo 

    consVel()
    tempo = int(input('Insira o tempo em minutos: '))

    vel1 = (velmax/2) + (velmax/3)

    print(f'v1{vel1}')
    print(f'Iniciando v{velmax} por {tempo}m')


inicial()
