n1 = int(input('Digite um número\nCálculo de fatorial:'))
c = n1
fato = 1
print('Calculando {}! = '.format(n1), end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    fato *= c
    c -= 1
print(fato)