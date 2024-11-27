import random
lista = []
megasena = []
tot = 1
resp = int(input('Quantos jogos você quer sorteados? '))
while tot <= resp:
    c = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            c += 1
        if  c == 6:
            break
    lista.sort()
    megasena.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(megasena):
    print(f'Jogo {i+1}: {l}')