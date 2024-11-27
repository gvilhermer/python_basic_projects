from random import randint


def sorteio(lista):
    for c in range(0, 5):
        numeros.append(randint(1, 10))



def pares(lista):
    somapares = 0
    for v in numeros:
        if v % 2 == 0:
            somapares += v
    print(f'A soma dos numeros pares é {somapares}')



numeros = []
sorteio(numeros)
print(f'Os valores sorteados foram {numeros}')
pares(numeros)
