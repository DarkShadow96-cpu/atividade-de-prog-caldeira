# o programa gera números randomicos que equivalem a temperatura de uma caldeira
# quando a temperatura for menor que 25°
""" Protótipo """
from random import randrange
from time import *

temperatura = []
ar = 0
media = 0
cont = 1


def apresentador(valmed, valcont):
    print(f'A caldeira foi desativada!\nSua temperatura média:{valmed:2.2f}'
          f'\nSeu tempo de funcionamento:{valcont * 20} segundos')


first_time = time()

while ar == 0:
    temperatura.append(randrange(12, 40))
    try:
        media = sum(temperatura) / len(temperatura)
    except ZeroDivisionError:
        media = sum(temperatura) / 1
    print(temperatura)
    print(media)
    sleep(2)
    second_time = time()
    print(int(second_time - first_time))
    if int(second_time - first_time) == 20:
        if media >= 25:
            ar = 1
            apresentador(media, cont)
    elif int(second_time - first_time) > 20:
        temperatura.clear()
        first_time = time()
        cont += 1
        print('-------------------------------------------------------------------------------\n')


""" O programa pega a temperatura em tempo real da caldeira e com esse tempo calcula a
média das temperatura que é checada e caso passe da estipuçada, no caso 25°, o programa é encerrado,
significando que a caldeira é desligada."""
