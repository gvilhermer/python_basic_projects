from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print()


contador(1, 10, 1)
contador(10, 0, 2)
ini = int(input('Início:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))
contador(ini, fim, passo)
