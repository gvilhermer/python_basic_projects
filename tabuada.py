from time import sleep
while True:
    n = int(input('Digite um valor para ver sua tabuada:'))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    sleep(1)
print('Programa encerrado.')