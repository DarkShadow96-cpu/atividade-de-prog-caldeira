# o programa gera números randomicos que equivalem a temperatura de uma caldeira
# quando a temperatura for menor que 25°
""" Protótipo """
from random import randrange
from time import *

temperatura = [0]*20
ar = 0
media = 0
cont = 1


def apresentador(valmed, valcont):
    print(f'A caldeira foi desativada!\nSua temperatura média:{valmed:2.2f}'
          f'\nSeu tempo de funcionamento:{valcont * 20} segundos')


first_time = time()

while ar == 0:
    temperatura.insert(0, randrange(12, 40))
    temperatura.pop()
    try:
        media = sum(temperatura) / len(temperatura)
    except ZeroDivisionError:
        media = sum(temperatura) / 1
    print(f'Vetor das temperaturas: {temperatura}')
    print(f'Média:{media}')
    sleep(2)
    second_time = time()
    print(f'Tempo:{int(second_time - first_time)}')
    if int(second_time - first_time) == 20:
        if media >= 25:
            ar = 1
            apresentador(media, cont)
    elif int(second_time - first_time) > 20:
        first_time = time()
        cont += 1
        print('-------------------------------------------------------------------------------\n')


""" O programa pega as temperaturas em tempo real de uma caldeira e coloca-as em um vetor cíclico o qual tem 20
posições já estabelecidas e que quando um valor é inserido ele é colocado na posição zero do index
e o ultimo valor do vetor é removido, além disso o programa calcula as médias das temperaturas e ,a cada 20 segundos,
quando esta média ficar maior que 25 o programa para, simbolizando o desligamento da caldeira, caso a média de
menor que 25 o programa continua a adicionar valores no vetor até a proxima checagem."""
